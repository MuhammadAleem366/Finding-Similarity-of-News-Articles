import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sr1 = pd.Series(np.random.randint(0,100,10))
# print(sr1)
sr1.index = [1,2,3,4,5,6,7,8,9,10]
# print(sr1.head())
# slicing with pandas
# sr1.iloc[3]='Aleem'
# print(sr1.iloc[3])
'''print(sr1[:2])
print('--------------------')
print(sr1[5:2])

print('--------------------')
print(sr1[:-2])

print('--------------------')
print(sr1[-2:])

print('--------------------')
print(sr1[:8])

print('--------------------')
# s = pd.Series(['Aleem','Awan'])
# print(s)
# print(pd.__version__)
# print(sr1[:-4])
sr2 = pd.Series(['Aleem','Saleem','Raheem','Azeem'],index=['Name','Name','Name','Name'])
sr3 = sr1.append(sr2)
# print(sr3[-7:])
sr3 = sr3.drop('Name')
print(sr3)
sr1 = pd.Series([1,2,3,4,5,6])
sr2 = pd.Series([2,3,4,5,6,7,8,9,0])
add_sr = sr1.add(sr2)
sub_sr = sr1.sub(sr2)
mul_sr = sr1.mul(sr2)
div_sr = sr1.mul(sr2)
# print('Adding:',add_sr,' => sub_sr : ',sub_sr,'=>Multiply:',mul_sr,' => Divide_sr : ',div_sr)
print('Minimum value: ',sr1.min())
print('Maximum value: ',sr1.max())
print('Average value: ',sr1.median())
dates = pd.date_range('today',periods=6)
random_arr = np.random.randint(0,1000,36)
# print(random_arr,dates)
arr = random_arr.reshape(6,6)
columns = ['A','B','C','D','E','F']
df1 = pd.DataFrame(arr,index=dates,columns=columns)
 print(df1)
dict1 = {'Animals':['dog','cat','snake','beer','Lion','Tiger'],
         'Age':[20,30,45,65,23,21],
         'Country':['Australia','India','America','China','Japan','Africa']}
# labels = ['A','B','C','D','E','F']
df2 = pd.DataFrame(dict1)
print(df2) '''
data = {'Maths':[89,90,76,89,23],
        'English':[89,90,76,99,23],
        'Chemisrty':[89,90,76,67,23],
        'Science':[89,90,76,56,23],
        'Biology':[89,90,76,86,23],
        'English':[89,90,76,98,23]
}
names = ['Aleem','Raheem','Aziz','Husnain','Taimoor']
df3 = pd.DataFrame(data,index=names)
# print(df3.iloc[2].median())
# index_in_lower = df3.index.str.lower()
# print(index_in_lower.str.upper())
marks = pd.read_csv('Marks.csv')
# marks = marks.set_index(inplace=True)
marks = marks.rename(columns={'Unnamed: 0':'Names'})
marks = marks.set_index('Names')
print(marks.loc['Aleem',['Maths','Biology']])
marks = marks.drop('Aleem')
print(marks)
marks = marks.drop('Raheem')
print(marks)
del marks['Science']
print(marks)
marks['Chemistry']=None
print(marks)
marks.iloc[0,4] = 10
Bio_numbers = marks['Biology']
print(Bio_numbers)
Bio_numbers += 2
no_greater_than_eighty = marks.where(marks['Chemistry'] == 10)
print(no_greater_than_eighty)
marks = marks.reset_index()
print(marks)
no_greater_than_eighty=no_greater_than_eighty.fillna(method='ffill')
print(no_greater_than_eighty)