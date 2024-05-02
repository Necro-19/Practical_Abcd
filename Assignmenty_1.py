#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[2]:


d1={"Name":['Ankit','Saisagar','Paras'],"Country":['Gondia','Umerkhed','Yavatmal']}


# In[5]:


df1 = pd.DataFrame(d1)


# In[7]:


print(df1)


# In[8]:


d2 = {"ID":[1,2,3],"Name":['Ankit','Saisagar','Paras']}


# In[9]:


df2 = pd.DataFrame(d2)


# In[10]:


df2


# In[11]:


df_merged = df1.merge(df2)


# In[12]:


df_merged


# In[ ]:




