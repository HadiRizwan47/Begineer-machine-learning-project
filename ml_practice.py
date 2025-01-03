# -*- coding: utf-8 -*-
"""ML Practice

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13wpiJDIemTB1KPfzzJYx1I0d_EaUg21X
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

fd = pd.read_csv('/content/student_data.csv')

fd.head(5)

fd.describe()

fd.info()

fd.tail(5)

sns.boxplot(x=fd['age'])

sns.boxplot(x=fd['freetime'])

fd.isnull().sum()

sns.boxplot(x=fd['famrel'])

sns.histplot(data=fd,x='G3', kde='True')

sns.barplot(data=fd, x='school', y='G3')

sns.boxplot(data=fd,x='sex', y='G3')

sns.scatterplot(data=fd,x='studytime',y='G3')

fd[['G1','G2','G3']].mean().plot(kind='line',marker='o')
plt.show

from sklearn.preprocessing import LabelEncoder
categorical_columns = ['sex','school','address','famsize','Pstatus','Mjob','Fjob','reason','guardian','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic']
label_encoder = LabelEncoder()
for col in categorical_columns:
  fd[col] = label_encoder.fit_transform(fd[col])

corr = fd.corr()
print(corr)

fd.head(5)

fd.drop(columns=['address','traveltime','guardian','health','famsize','Pstatus','nursery'],inplace=True)

plt.figure(figsize=(20,20))
sns.heatmap(corr, annot=True, cmap='coolwarm',fmt='.2f', linewidth=0.5)
plt.title('Heatmap')
plt.show()

fd.info()

fd['G3'] = fd['G3'].apply(lambda x: 1 if x >= 10 else 0)
print(fd['G3'].value_counts())

X = fd.drop(columns='G3')
y = fd['G3']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_reg.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
y_pred = log_reg.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:",accuracy)

