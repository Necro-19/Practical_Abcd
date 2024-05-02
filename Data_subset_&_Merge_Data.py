#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


students={"name": ['rohit','roshan','aniket','sanskar','sham','swanand','saket','nikhil'] , 'Marks': [78,88,25,88,97,84,66,55]}


# In[5]:


stud=pd.DataFrame(students)


# In[6]:


print("DataFrame:\n",stud)


# In[7]:


print(stud.loc[[0,1,6]])


# In[8]:


print(stud.loc[0:4])


# In[9]:


print(stud.loc[0:2,['name']])


# In[10]:


print(stud.iloc[[0,1,6],[1]])


# In[11]:


#merging


# In[12]:


d1={"Name":["rohit","sham","om"],"Country":["India","india","Usa"]}


# In[13]:


df1=pd.DataFrame(d1)


# In[14]:


print('DataFrame1:\n',df1)


# In[15]:


d2={"ID":[1,2,3],"Name":["rohit","pankaj","nikhil"]}


# In[16]:


df2=pd.DataFrame(d2)


# In[17]:


print('DataFrame2:\n',df2)


# In[18]:


df_merge=df1.merge(df2)


# In[19]:


print("inner join:\n",df_merge)


# In[20]:


print("left join:\n",df1.merge(df2,how='left'))


# In[21]:


print("right join:\n",df1.merge(df2,how='right'))


# In[22]:


print("outer join:\n",df1.merge(df2,how='outer'))


# In[ ]:




