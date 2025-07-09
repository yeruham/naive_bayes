import pandas as pd
import naive_bayesian.naive_bayesian_model as naive_m
import naive_bayesian.naive_calc as naive_c

df = pd.read_csv('data/buy_computer_data.csv')

df = df.drop('id', axis=1)
# print(df)

naive_model = naive_m.Naive_bayesian_model(df, 'Buy_Computer')

percent_classified = naive_model.get_percent_classified()
data_by_classified = naive_model.get_data_by_classified()
print(percent_classified)
print(data_by_classified)

naive_calc = naive_c.Naive_calc(percent_classified, data_by_classified)
naive_calc.naive_calc_by_column({'age': 'middle_age', 'income': 'low', 'student': 'yes', 'credit_rating': 'excellent'})

sum = 0

for index, row in df.iterrows():
    # print("\nanswer: ", row.Buy_Computer)
    answer = naive_calc.naive_calc_by_column({'age': row.age, 'income': row.income, 'student': row.student, 'credit_rating': row.credit_rating})
    if answer == row.Buy_Computer:
        sum += 1

print(sum)
print(sum / df.shape[0])