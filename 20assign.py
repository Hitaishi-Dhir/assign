#Ques1

import pandas as pd

data = {'Name': ['HITAISHI', 'MAHAK', 'JASKIRAN'], 'Age': [20, 20, 21],
        'mail_id': ['dhirhitaishi@gmail.com', 'mahak12@gmail.com', 'kaurjaskiran@gmail.com'],
        'phone_no': [9888076023, 9888774524, 9876542310]}
df = pd.DataFrame(data, index=[1, 2, 3])
print(df)

#Ques2

a = pd.read_csv("test.csv")
df = pd.DataFrame(a)

print("part a")
print(df.head(5))

print("part b")
print(df.head(10))

print("part c")
print(df.axes)
print(df.T)

print("part d")
print(df.tail(5))

b = pd.read_csv("test.csv")
df = pd.DataFrame(b, index=[1])
print(df.head)
print(df.axes)
print(df.shape)
print(df['MinTemp'].head)
print(df['MinTemp'].dtypes)
print(df['MinTemp'].shape)