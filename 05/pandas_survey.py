import os, re
import pandas as pd
df2 = pd.read_csv(r'C:\Users\skytr\Documents\GitHub\do-it-python\05\survey.csv')
print(df2.head())

print(df2.describe())

print(df2['income'].sum())

print(df2['income'].median())

print(df2['sex'].value_counts())

print(df2.groupby('sex').mean())