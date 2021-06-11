import numpy as np
import pandas as pd
import re
import Preprocessing as p
#import Dataset
#import Dawn
#import Jazeera
import connection as Project
from math import log
data_set = Project.GetValuesFromDatabase()
#data_set = Dataset.Get_data_list()
#aray = np.array(data_set)
#print(aray)
pd_Data_Set = pd.DataFrame(data_set,columns=['Description','Newspaper'])
#print(pd_Data_Set)

pattern = [(r'\'d',' would'),
            (r'\'s',' is'),
            (r'don\'t','do not')
            ,(r'didn\'t','did not'),(r'\'m',' am')
            ,(r'you\'re',' you are')
            ,(r'\'ve',' have')
            ,(r'\'ll',' will ')
           ,(r'\\xad','')
           ,(r'-','')]
def ReplaceMethod(patterns, text):
    for (to_replace, replace_by) in patterns:
        regex = re.compile(to_replace)
        text = regex.sub(replace_by ,text)
    return text
def GetCorpus():
    dict_vlues = pd_Data_Set.to_dict('records')
    corpus = {}
    count = 0
    for x in dict_vlues:
        #text = ReplaceMethod(pattern,x["Description"])
        corpus.update({"%s"%str(count):"%s"%x["Description"]})
        count = count+1
    return corpus
corpus = GetCorpus()
# print(corpus)

QUERY_TERMS = ['US-Taliban','Kashmir']
def tf(term, doc, normalize=True):
    doc = p.Pre_Process(doc.lower())
    if normalize:
        return doc.count(term.lower()) / float(len(doc))
    else:
        return doc.count(term.lower()) / 1.0

def idf(term, corpus):
    num_texts_with_term = len([True for text in corpus if term.lower()
                               in text.lower().split()])

    # tf-idf calc involves multiplying against a tf value less than 0, so it's
    # necessary to return a value greater than 1 for consistent scoring.
    # (Multiplying two values less than 1 returns a value less than each of
    # them.)

    try:
        return 1.0 + log(float(len(corpus)) / num_texts_with_term)
    except ZeroDivisionError:
        return 1.0


def tf_idf(term, doc, corpus):
    return tf(term, doc) * idf(term, corpus)

for (k, v) in sorted(corpus.items()):
     print(k, ':', v)
def GetQueryScores():
    query_scores = {}
    for (k,v) in corpus.items():
        query_scores.update({k:0})
    return query_scores
query_scores = GetQueryScores()
for term in [t.lower() for t in QUERY_TERMS]:
    #for doc in sorted(corpus):
        #print (corpus[doc])
        #print('TF(%s): %s' % (doc, term), tf(term, corpus[doc]))
        #print('IDF: %s' % (term), idf(term, corpus.values()))
        #Term_Freq = tf(term,corpus[doc])
    for doc in sorted(corpus):
        score = tf_idf(term, corpus[doc], corpus.values())
        #print('TF-IDF(%s): %s' % (doc, term), score)
        query_scores[doc] += score
append_doc=[]
print("Overall TF-IDF scores for query '%s'" % (' '.join(QUERY_TERMS)))
print(query_scores)
for (doc, score) in sorted(query_scores.items()):
    if score <= 0.0:
        continue
        #print(doc + " : " + str(score))
    else:
        append_doc.append(doc)

print(append_doc)
# print(len(pd_Data_Set))
def GetValuesForDisplay(values):
    dict_vlues = pd_Data_Set.to_dict('records')
    list = []
    count = 0
    # print(dict_vlues)
    for x in dict_vlues:
        for val in values:
            # print(count == int(val))
            if int(val) != count:
                 continue
            else:
                list.append([x["Description"], x["Newspaper"]])
        count = count + 1
    return list
array_of_Selected_Terms =np.array(GetValuesForDisplay(append_doc))
print(array_of_Selected_Terms[0:])