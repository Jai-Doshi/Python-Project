# IMPORTING LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import warnings

# IMPORTING DATASET
warnings.filterwarnings('ignore')
df = pd.read_csv('..//assets/data.csv')

# Line Plot
x = df['age']
y = df['year']

plt.figure(figsize=(10,10))

plt.xlabel('AGE')
plt.ylabel('YEAR')

plt.xlim((15,55))
plt.ylim((2020,2022))

plt.title('AGE PREDICTION')

sns.lineplot(x,y, color='blue')

plt.legend('A')
plt.show()

x = df['year']
y = df['age']

plt.figure(figsize=(10,10))

plt.xlabel('YEAR')
plt.ylabel('AGE')

plt.xlim((2020,2022))
plt.ylim((15,55))

plt.title('AGE PREDICTION')

sns.lineplot(x,y, color='blue')

plt.legend('Y')
plt.show()

# HISTOGRAM (DISPLOT)

plt.figure(figsize=(10,10))
sns.distplot(df['age'],bins=15)
plt.axvline(df['age'].mean(),color='red')
plt.axvline(df['age'].median(),color='green')
plt.show()

# BAR PLOT (COUNT PLOT)

plt.figure(figsize=(10,10))
sns.countplot(data=df,x='age')
plt.show()

plt.figure(figsize=(10,10))
sns.countplot(data=df,y='name')
plt.show()

plt.figure(figsize=(10,10))
sns.countplot(data=df,x='subcategory',hue='category')
plt.xticks(rotation=90)
plt.yticks(rotation=45)
plt.show()

# PIE CHART

plt.figure(figsize=(10,10))
plt.pie(data=df,x='year',autopct='%1.2f%%')
plt.show()

# SCATTER PLOT

plt.figure(figsize=(10,10))
sns.scatterplot(data=df,x='name',y='age')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10,10))
sns.scatterplot(data=df,x='category',y='subcategory',color='red')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(20,20))
sns.scatterplot(data=df,x='name',y='category',hue='subcategory')
plt.xticks(rotation=90)
plt.yticks(rotation=45)
plt.title('CATEGORY - SUBCATEGORY')
plt.show()

# HEAP PLOT

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),annot=True)
plt.show()

# BOX PLOT

plt.figure(figsize=(10,10))
sns.boxplot(data=df,x='year',y='age')
plt.show()
