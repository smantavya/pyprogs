import pandas as pd
import numpy as np

df = pd.read_csv('annual-enterprise-survey-2018-financial-year-provisional-csv.csv')
# print(df.head())
# print(df.columns)

# print(df.iloc[0,4])
# print(df.loc[0,"Units"])

# print(df.loc[[1,3,4,6,8],'Units'])


# for q in df:
#     print(df[q])


# print(df.head(10))

# print(df[['Units',"Year"]])

print(df[(df['Value'] == '83') & (df['Year'] == 2018)])
