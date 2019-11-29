# -*- coding: utf-8 -*-
"""17EC10062_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iMrdknxmAXuBIJ4WOT-XEEAUZIiszow7
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.

train = pd.read_csv('/kaggle/input/kmeanss/data4_19.csv')
y = train['Iris-setosa']
# train = train.drop('Iris-setosa',axis=1)
train

from random import seed
from random import *
np.random.seed(12)
# seed random number genera
# random()

def dist(a1, a2):
    sum=0
    for i in range(len(a1)):
        sum+=np.sqrt((a1[i]-a2[i])*(a1[i]-a2[i]))
    return sum

y.value_counts()

data = train

def kmeans(data, iterations=10):
    y_train = data.iloc[:, 4]
    data = data.drop('Iris-setosa', axis=1)
    idx1 = y_train[y_train=='Iris-setosa'].index
    idx2 = y_train[y_train=='Iris-versicolor'].index
    idx3 = y_train[y_train=='Iris-virginica'].index

    centroid = [data.iloc[idx1, :].sum()/len(data.iloc[idx1, :]), data.iloc[idx2, :].sum()/len(data.iloc[idx2, :]), data.iloc[idx3, :].sum()/len(data.iloc[idx3, :])]
    
#     for clustering data purely in unsupervised fashion we uncomment following code lines (uncomment them)
    clust = [randint(0, len(data)-1), randint(0, len(data)-1), randint(0, len(data)-1)]
    centroid = [data.iloc[clust[0], :], data.iloc[clust[1], :], data.iloc[clust[2], :]] 

    d=[0]*len(data)
    for k in range(iterations):
        for i in range(len(data)):
            d[i] = [dist(data.iloc[i, :], centroid[0]),dist(data.iloc[i, :], centroid[1]),dist(data.iloc[i, :], centroid[2])]
        new_cen=[0]*len(data)
        for i in range(len(data)):
            new_cen[i] = np.argmin(d[i])
        new_cen = pd.DataFrame(new_cen)
        idx1 = new_cen[new_cen[0]==0].index
        centroid[0] = data.iloc[idx1,:].sum()/len(data.iloc[idx1, :])

        idx2 = new_cen[new_cen[0]==1].index
        centroid[1] = data.iloc[idx2,:].sum()/len(data.iloc[idx2, :])

        idx3 = new_cen[new_cen[0]==2].index
        centroid[2] = data.iloc[idx3,:].sum()/len(data.iloc[idx3, :])

    new_cen.replace(0, 'Iris-setosa', inplace=True)
    new_cen.replace(1, 'Iris-versicolor', inplace=True)
    new_cen.replace(2, 'Iris-virginica', inplace=True)
    return new_cen[0], centroid



y_new, centroid = kmeans(train)
y_new

print("value_colunts = ")
print(y_new.value_counts())

y1 = [ y[y=='Iris-setosa'], y[y=='Iris-versicolor'], y[y=='Iris-virginica']]
# y1[0]

y_new1 = [ y_new[y_new=='Iris-setosa'], y_new[y_new=='Iris-versicolor'], y_new[y_new=='Iris-virginica']]
# y_new1[2]

def jq_dist(a1, a2):
    idx1 = np.array(a1.index)
    idx2 = np.array(a2.index)
    n=len(idx1)
    m = len(idx2)
    sim=0;j=0
    dis=0;i=0
    while(i < n and j < m):
        if idx1[i] == idx2[j]:
            sim+=1
            i+=1
            j+=1
        elif idx1[i] < idx2[j]:
            i+=1
            dis+=1
        elif idx1[i] > idx2[j]:
            j+=1
            dis+=1
            
    while(i < n):
        dis+=1;i+=1
    while(j < m):
        dis+=1;j+=1
    
    return 1-sim/(sim+dis)



col = [0]*3
for i in range(3):
    col[i] = y_new1[i].value_counts().index[0]



col = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
col = ['clust 1', 'clust 2', 'clust 3',]
colp = ['pred clust 1', 'pred clust 2', 'pred clust 3',]

jq = pd.DataFrame(index = colp, columns=col)
jq

for i in range(3):
    for j in range(3):
        jq.iloc[i, j] = jq_dist(y1[i], y_new1[j])
jq

print("jq matrix is :")

print(jq)

print("centroids are :")

print(np.array(centroid))

print("centroids are :")

print(centroid)





