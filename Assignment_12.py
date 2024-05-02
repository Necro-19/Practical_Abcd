#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("records.csv")


# In[3]:


df


# In[4]:


df.info()


# In[5]:


data = df
data['Salary'] = data['Salary'].fillna(data['Salary'].mean())


# In[6]:


data


# In[7]:


data = df
data['SalaryMissing'] = data['Salary'].isnull()


# In[8]:


data


# In[9]:


testdf = df[df['Salary'].isnull()==True]
traindf = df[df['Salary'].isnull()==False]
traindf.drop("Salary",axis=1,inplace = True)
testdf.drop("Salary",axis=1,inplace = True)


# In[10]:


traindf


# In[ ]:




