#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data=pd.read_csv("records.csv")


# In[4]:


data


# In[5]:


data.sort_values(["Salary"],axis=0,ascending=[True],inplace=True)


# In[6]:


data


# In[7]:


data.T


# In[8]:


data.shape


# In[9]:


data.size


# In[ ]:





# In[ ]:




