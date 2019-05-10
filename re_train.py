#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from os.path import join as osjoin
import numpy as np


# In[9]:


#Load dữ liệu từ database
import pickle

PATH_NEW_DATABASE = osjoin(os.getcwd(), 'newdatabase')
PATH_DATABASE = osjoin(os.getcwd(), 'database')
PATH_DATABASE_IMAGE = osjoin(PATH_DATABASE, 'image')

with open(osjoin(PATH_DATABASE, 'x_vector.pkl'), 'rb') as f:
    x_vector = np.array(pickle.load(f))
with open(osjoin(PATH_DATABASE, 'x_label.pkl'), 'rb') as f:
    x_label = np.array(pickle.load(f))
with open(osjoin(PATH_DATABASE, 'x_name.pkl'), 'rb') as f:
    x_name = np.array(pickle.load(f))


# In[10]:


idx = np.random.permutation(len(x_label))
x_vector = x_vector[idx]
x_label = x_label[idx]
x_name = x_name[idx]


# In[11]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score, accuracy_score

knn = KNeighborsClassifier(n_neighbors=5, metric = 'euclidean')
svc = LinearSVC()

knn.fit(x_vector, x_label)
svc.fit(x_vector, x_label)


# In[ ]:


with open('models/knn.pkl', 'wb') as f:
    pickle.dump(knn, f)
with open('models/svm.pkl', 'wb') as f:
    pickle.dump(svc, f)

