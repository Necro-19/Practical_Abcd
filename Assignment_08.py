#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[5]:


df=pd.read_csv("house.csv")


# In[6]:


df


# In[7]:


df.head(10)


# In[8]:


df.info()


# In[9]:


df.columns


# In[10]:


df.describe


# In[11]:


df.shape


# In[12]:


df.isnull().sum()


# In[14]:


sns.relplot(x='households',y='median_income',hue='total_rooms',data=df)
plt.show()


# In[19]:


sns.relplot(x='population',y='median_income',hue='total_rooms',data=df)
plt.show()


# In[20]:


sns.relplot(x='median_house_value',y='median_income',hue='total_rooms',data=df)
plt.show()


# In[ ]:




