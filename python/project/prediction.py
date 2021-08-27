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

## **PREDICTIONS**

### *STATES*

# TOTAL STATES
states = df['location'].unique()
print('TOTAL LENGTH :',len(states))
print('\n')

# SUMMARY AS PER STATES
states_summary = df['location'].value_counts()
print('SUMMARY :\n',states_summary)
print('\n')

# TOP 5 RESPONSES
print('TOP 5 \n',states_summary.nlargest(5))

fig,axes = plt.subplots(1,2,figsize=(25,10))
df['location'].value_counts().plot(kind='bar',ax=axes[0], color='green')
df['location'].value_counts().plot(kind='pie', autopct='%1.2f%%', ax=axes[1], explode=(0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
plt.title('HIGHEST STATE')
plt.show()

### *CATEGORY*

df.groupby('location')['category'].value_counts()

cat = df[df['location'] == 'GUJARAT'].groupby('location')['category']
# Toatl CATEGORIES 
print('TOTAL :',cat.unique())
print('\n')

# SUMMARY AS PER CATEGORIES
print('SUMMMARY : \n',cat.value_counts())
print('\n')

# TOP 5 RESPONSES
print('TOP 5 : \n',cat.value_counts().nlargest(5))

vis_cat = df[df['location'] == 'GUJARAT'].groupby('location')['category'].value_counts()
fig,axes = plt.subplots(1,2,figsize=(25,10))
vis_cat.plot(kind='bar',ax=axes[0], color='lightgreen')
vis_cat.plot(kind='pie', autopct='%1.2f%%', ax=axes[1], explode=(0.1,0,0,0,0,0,0,0))
plt.title('HIGHEST CATEGORY')
plt.show()

### *SUB CATEGORY*

subcat = df[(df['location'] == 'GUJARAT') & (df['category'] == 'Celebration')].groupby(['location','category'])['subcategory']
# TOTAL SUBCATEGORY
print('TOTAL :',subcat.unique())
print('\n')

# SUMMARY AS PER SUB CATEGORY
print('SUMMMARY : ')
print(subcat.value_counts())
print('\n')

# TOP 5 RESPONSES
print('TOP 5 : \n',subcat.value_counts().nlargest(5))

vis_subcat = df[(df['location'] == 'GUJARAT') & (df['category'] == 'Celebration')].groupby(['location','category'])['subcategory'].value_counts()
fig,axes = plt.subplots(1,2,figsize=(25,10))
vis_subcat.plot(kind='bar',ax=axes[0], color='lightgreen')
vis_subcat.plot(kind='pie', autopct='%1.2f%%', ax=axes[1])
plt.title('HIGHEST SUB CATEGORY')
plt.show()

### *USER*


df[(df['location'] == 'GUJARAT') & (df['category'] == 'Celebration') & (df['subcategory'] == 'Pub')].groupby(['location','category','subcategory'])['name'].value_counts()


df[(df['location'] == 'GUJARAT') & (df['category'] == 'Celebration') & (df['subcategory'] == 'Pub')].groupby(['location','category','subcategory'])['age'].value_counts()

df[(df['location'] == 'GUJARAT') & (df['category'] == 'Celebration') & (df['subcategory'] == 'Pub')]

dis = df[(df['location'] == 'GUJARAT') & (df['category'] == 'Celebration') & (df['subcategory'] == 'Pub')]
plt.figure(figsize=(10,10))
sns.displot(data=dis,x='age')
# sns.displot(data=dis,x='age',hue='name')
plt.show()

a = df[(df['location'] == 'GUJARAT') & (df['category'] == 'Celebration') & (df['subcategory'] == 'Pub')]

b = []
one = []
two = []
three = []
four = []
for i in a['age']:
    b.append(i)
for i in b:
    # print(i)
    if (i <= 25):
        one.append(i)
    elif (i <= 50):
        two.append(i)
    else:
        print('Done')

print('AGE BETWEEN 0-25 : {}'.format(len(one)))
print('AGE BETWEEN 25-50 : {}'.format(len(two)))
print('TOTAL : ',len(b))

df[(df['location'] == 'GUJARAT') & (df['category'] == 'Celebration') & (df['subcategory'] == 'Pub')].groupby(['location','category','subcategory'])['age'].value_counts().plot(kind='pie',autopct='%1.2f%%')

### *ADDITIONAL*

df.groupby('location')['category'].value_counts()

cat_gph = df.groupby('location')['category'].value_counts()
plt.figure(figsize=(10,10))
sns.scatterplot(data=cat_gph,x='location',y='category')
plt.xticks(rotation=90)
plt.yticks(rotation=45)
plt.title('CATEGORIES')
plt.show()

df.groupby('category')['subcategory'].value_counts()

subcat_gph = df.groupby('category')['subcategory'].value_counts()
plt.figure(figsize=(10,10))
sns.scatterplot(data=subcat_gph,x='subcategory',y='category',color='green')
plt.xticks(rotation=90)
plt.yticks(rotation=45)
plt.title('SUB CATEGORIES')
plt.show()

df.groupby(['location','category'])['subcategory'].value_counts()

subcat_gph = df.groupby(['location','category'])['subcategory'].value_counts()
plt.figure(figsize=(25,15))
sns.scatterplot(data=subcat_gph,x='subcategory',y='category',color='red',hue='location')
plt.xticks(rotation=90)
plt.yticks(rotation=45)
plt.title('SUB CATEGORIES')
plt.show()

