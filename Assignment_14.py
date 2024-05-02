#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install textblob


# In[3]:


from textblob import TextBlob


# In[4]:


Feedback1 = "The Food at Radison was awesome"
Feedback2 = "The Food at Radison was very good"


# In[5]:


blob1=TextBlob(Feedback1)
blob2=TextBlob(Feedback2)


# In[6]:


blob1.sentiment


# In[7]:


blob2.sentiment


# In[ ]:




