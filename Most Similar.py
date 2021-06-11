import numpy as np
import math
import pandas as pd
import Preprocessing as p
def dotProduct(D1, D2):
    Sum = 0.0
    for key in D1:
        if key in D2:
            Sum += (D1[key] * D2[key])
    return Sum

# returns the angle in radians
# between document vectors
def vector_angle(D1, D2):
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1) * dotProduct(D2, D2))

    return math.acos(numerator / denominator)
#cosine = vector_angle({14:0.6663},{12:0.9766})
#print(cosine)
doc1 = "My name is aleem and student of graduate  "
doc2 = " He is a boxer and his task is very hard"
doc3 = "My name is awais and student of graduate"
bow1 = p.Pre_Process(doc1)
bow2 = p.Pre_Process(doc2)
bow3 = p.Pre_Process(doc3)
Wordset = set(bow1).union(set(bow2))

Wordset = set(Wordset).union(set(bow3))

word_dict_A = dict.fromkeys(Wordset,0)
word_dict_B = dict.fromkeys(Wordset,0)
word_dict_C = dict.fromkeys(Wordset,0)
print(word_dict_A)
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
        return 1.0 + math.log(float(len(corpus)) / num_texts_with_term)
    except ZeroDivisionError:
        return 1.0

def tf_idf(term, doc, corpus):
    return tf(term, doc) * idf(term, corpus)
for word in word_dict_A:
    print(word)
    print(bow1)
    word_dict_A[word] = tf_idf(word,doc1,word_dict_A)
print(word_dict_A)
for word in word_dict_B:
    print(word)
    print(bow2)
    word_dict_B[word] = tf_idf(word,doc2,word_dict_B)
for word in word_dict_C:
    print(word)
    print(bow3)
    word_dict_C[word] = tf_idf(word,doc3,word_dict_C)
print(word_dict_B)
DataFrame = pd.DataFrame([word_dict_A,word_dict_B,word_dict_C])

print(vector_angle(word_dict_A,word_dict_B))

print(vector_angle(word_dict_A,word_dict_C))
print(DataFrame)