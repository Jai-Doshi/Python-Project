# IMPORTING LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import warnings

# IMPORTING DATASET

df = pd.read_csv('..//assets/data.csv')

# FEATURES

# Basic

df.head()
df.tail()
df.info()
df.describe()
df.columns

# Intermediate

df['name'].unique()
df['name'].value_counts()

df['age'].unique()
df['age'].value_counts()

df['location'].unique()
df['location'].value_counts()

df['category'].unique()
df['category'].value_counts()

df['subcategory'].unique()
df['subcategory'].value_counts()

df['year'].unique()
df['year'].value_counts()

# Advance

df[df['location'] == 'GUJARAT'].groupby('location')['category'].value_counts()

# Expert

df[(df['year'] == 2021) & (df['location'] == 'GUJARAT')].groupby(['year','location'])['category'].value_counts()

# Expert ++

col = []
d = {}
c = []

def exp(): 

    for i in df:
        col.append(i)  
        
        for k in col:
            d.setdefault(k)

        length = len(i)    
        val = []

        for j in df[i]:
            val.append(j)

            d[k] = val

    return func()

def func():

    for i in range(len(d)):
        for j in range(len(d[col[i]])):
            c.append(df[(df[col[i]] == d[col[i]][j]) & (df[col[i-1]] == d[col[i-1]][j])].groupby([col[i],col[i-1]])[col[i-2]].value_counts())

    return c

print(exp())

# Particular User

def user(user_name):
    print(df[df['name'] == un.capitalize()].groupby('category')['subcategory'].describe())
    print('\n \n')
    print(df[df['name'] == un.capitalize()].groupby('subcategory')['category'].describe())
    print('\n \n')
    print(df[df['name'] == un.capitalize()].value_counts())

un = input('Enter : ')
user(un)
