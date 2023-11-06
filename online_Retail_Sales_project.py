import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

features=pd.read_csv("online_Retail_sales\Features data set.csv")
sales=pd.read_csv("online_Retail_sales\sales data-set.csv")
stores=pd.read_csv("online_Retail_sales\stores data-set.csv")

print(type(features))
print(type(sales))
print(type(stores))

print("Features: ",features.shape)
print("sales: ",sales.shape)
print("stores: ",stores.shape) 

print(features.info())
print(sales.info())
print(stores.info())

print("columns in Features table: ",features.columns)
print("column in sales table: ",sales.columns)
print("column in stores table: ",stores.columns)


print("\n First 5 elements of Features \n",features.head(5))
print("\n First 5 elements of sales \n",sales.head(5))
print("\n First 5 elements of store \n",stores.head(5))

print("\n Bottom 5 elements of Features \n",features.tail(5))
print("\n Bottom 5 elements of sales \n",sales.tail(5))
print("\n Bottom 5 elements of store \n",stores.tail(5))


df=pd.merge(sales,features,on=['Store','Date','IsHoliday'],how='left')
df=pd.merge(df,stores,on=['Store'],how='left')
df=df.fillna(0)
df.sort_values(['Date','Weekly_Sales'],ascending=[True,False],inplace=True)
print(df.head(7))

print(df.shape(7))

print(df.columns)

print(df.describe())

print(df.index)

print(df.values)

subset=df[['store','Date','Weekly_Sales','Fuel_Price','CPI','Umemployment']]
print(df.head())

print(df.loc[0])

print(df.loc[[0,99]])

print(df.iloc[0])

print(df.iloc[[0,99]])

print(df.iloc[-1])

print(df.ix[0])

subset=df.loc[:['Stores','Date','Weekly_Sale']]
print(subset.head())

subset=df.iloc[:[2,4]]
print(subset.head())

subset=df.iloc[-5::2,:]
print(subset.head())

print(df.head())

print(df.groupby('Date')['CPI'].mean().head(10))

print(df.groupby(['Store','Date'])[['Weekly_Sales','Unemployment']].mean().head(10))

print(df.groupby(['Store','Date'])[['Weekly_Sales','Unemployment']].mean().reset_index().head(10))

df.groupby(['Store'])[['Weekly_Sales']].mean().plot()
plt.show()

df.plot(kind='scatter',x='Store',y='Weekly_Sales',rot=70)
plt.show()

df.boxplot(column='Weekly_Sales',by='Store')
plt.show()