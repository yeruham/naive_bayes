from itertools import count

import pandas as pd


df = pd.read_csv('data/buy_computer_data.csv')

data = {}


df = df.drop('id', axis=1)
print(df)
# print(df.shape)
# print(df.columns)

for value in df.iloc[:, -1].unique():
    percent = float(df.iloc[:, -1][df.iloc[:, -1] == value].count())# / df.shape[0]
    data[value] = [percent, {}]

print(data)



for column in df.columns:
    d = {}
    if column != 'Buy_Computer':
        for v in df[column]:
            d[v] = float((df[column][(df[column] == v) & (df.iloc[:, -1] == 'yes')].count()) / data['yes'][0])

        data['yes'][1][column] = d
    # print(d)

for column in df.columns:
    d = {}
    if column != 'Buy_Computer':
        for v in df[column]:
            d[v] = float(df[column][(df[column] == v) & (df.iloc[:, -1] == 'no')].count() / data['no'][0])

        data['no'][1][column] = d
    # print(d)

print(data)

def naive(data: dict, **kwargs):
        result = {}
        for d in data.values():
            result[d[0]] = 1
            for k in d[1].keys():
                if k in kwargs.keys():
                    for v in d[1][k].keys():
                        if v in kwargs.values():
                            # print("*********")
                            # print(d[1][k][v])
                            result[d[0]] *= d[1][k][v]
        print(result)
        print(f"result: ")
        for r in result.items():
            print(r)
            print(r[1] * (r[0] / df.shape[0]))


naive(data, age= 'senior', income= 'medium', student= 'no', credit_rating= 'excellent')
