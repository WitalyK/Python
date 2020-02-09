import pandas as pd
'''
Это надо срочно понять!
'''

url = 'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx'
sheet_1 = pd.read_excel(url, sheet_name=0, index_col=0).fillna(0)
sheet_2 = pd.read_excel(url,	sheet_name=1, index_col=[0])
for day in sheet_2.index.unique():
  ration = pd.concat([sheet_2.loc[day].groupby('Продукт').sum(), sheet_1], axis=1, join='inner')
  print(*ration.apply(lambda x: x.iloc[1:] * x.iloc[0] / 100, axis=1).sum(axis=0).astype('int'))
