#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[21]:


data={'x':[1,2,3,4,5], 'y':[3,5,7,2,1]}


# In[22]:


df=pd.DataFrame(data)


# In[23]:


sns.lineplot(x='x',y='y',data=df)
plt.show()


# In[24]:


data={'category':["A","B","C"],'value':[20,40,60]}
df=pd.DataFrame(data)
sns.barplot(x='category',y='value',data=df)
plt.show()


# In[25]:


tips=sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=tips,hue='smoker')
plt.show()


# In[ ]:




