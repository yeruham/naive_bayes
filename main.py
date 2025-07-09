import pandas as pd
import naive_bayesian.naive_bayesian_model as naive_m
import naive_bayesian.naive_calc as naive_c
import naive_bayesian.exam_naive_model as exam
df = pd.read_csv('data/buy_computer_data.csv')
# df = pd.read_csv('data/phishing.csv')

df = df.drop('id', axis=1)
# df = df.drop('Index', axis=1)
# print(df)
classified = 'Buy_Computer'
# classified = 'class'
from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)

naive_model = naive_m.Naive_bayesian_model(df_train, classified)

percent_classified = naive_model.get_percent_classified()
data_by_classified = naive_model.get_data_by_classified()
print(percent_classified)
print(data_by_classified)

naive_calc = naive_c.Naive_calc(percent_classified, data_by_classified)

exam_df = df.tail(5)

exam_naive = exam.Exam_naive_model(exam_df, classified, naive_calc)
print(exam_naive.run_test())
