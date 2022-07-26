# -*- coding: utf-8 -*-
"""Diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18E_ZJxgsnq2Ju0V1K4Tt7_pIREqUUNJT
"""

import pandas as pd
import numpy as np

data=pd.read_csv("/content/diabetes.csv")

type(data)

data.head()

data.columns

data.shape

data.describe()

data['Pregnancies'].describe()

data.isnull().any()

data.isnull().sum()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

plt.hist(data['Glucose'],color='blue')
plt.show()

sns.distplot(data['Glucose'],color='grey')

numeric_columns=data.select_dtypes(include=[np.number])
print(numeric_columns.dtypes)

corr=numeric_columns.corr()

print(corr['Glucose'].sort_values(ascending=False))

plt.scatter(data['Pregnancies'],data['SkinThickness'])
plt.xlabel('Pregnancies')
plt.ylabel('SkinThickness')
plt.show()