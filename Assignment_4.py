#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


plt.plot([1,2,3,4])
plt.ylabel("Ankit")
plt.xlabel("Sai")
plt.show()


# In[5]:


names=['a','b','c']
values=[5,20,100]


# In[6]:


plt.bar(names,values)
plt.show()


# In[8]:


cars = ["AUDI","MERCEDISE","LAMBORGINI","JAGUAR"]
data = [12,34,56,76]
fig = plt.figure(figsize = (12,6))
plt.pie(data,labels = cars)
plt.show()


# In[ ]:




