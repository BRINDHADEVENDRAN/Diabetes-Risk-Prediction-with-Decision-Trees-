# -*- coding: utf-8 -*-
"""introduction to data-diabetesdataset

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ddB4C1mNgWkuBlJd_CuxHiCl0-NlBOtR
"""

import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/diabetes (1).csv")



df.head(50)

df.tail()

df.shape

df.info()

df.describe()

df.isnull().sum()

a=df['Glucose']
print(a)

plt.plot(a)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

b=df['BloodPressure']
print(b)

c=df['Insulin']
print(c)

plt.scatter(b,c)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

d=df['Outcome']
print(d)

plt.bar(d,height=10)
plt.xlabel('x-axis')
plt.ylabel('y-axis')



e=df['Pregnancies']
print(e)
f=df['Glucose']
plt.bar(e,f)

f=df['Age']
plt.hist(f,color='red')

g=df['Outcome']
plt.pie(g)

X=[1,2,3]
plt.pie(X)

i=df["BMI"]
sns.lineplot(i,color='blue')

j=df['SkinThickness']
h=df['Insulin']

sns.scatterplot(x=j,y=h,data=df)

sns.barplot(x=df['BloodPressure'],y=df['BMI'],data=df)

sns.pairplot(df,hue='Outcome')

K=[5,3,10,7,6,11,11,59]
L=[10,20,30,40,50,60,70,80]

sns.distplot(K,L)

x=df.drop('Outcome',axis=1)

x

y=df['Outcome']

y

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

x_train

y_train

from sklearn.preprocessing import StandardScaler

d=StandardScaler()

x_train=d.fit_transform(x_train)

x_train=d.fit_transform(x_train)

from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier(criterion="entropy")
clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)

y_pred

from sklearn.metrics import accuracy_score

accuracy_score(y_pred, y_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_pred, y_test)

from sklearn.tree import export_graphviz
import graphviz

graphviz.Source(export_graphviz(clf,feature_names=x.columns,filled=True))