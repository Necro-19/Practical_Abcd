#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nltk
nltk.download('punkt')


# In[3]:


nltk.download('stopwords')


# In[4]:


from nltk.corpus import stopwords
stop_words = stopwords.words('english')


# In[6]:


stop_words


# In[7]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


# In[17]:


stemmer = PorterStemmer()
str1= "There are so many players in ground"
str2= nltk.word_tokenize(str1)


# In[18]:


str1


# In[14]:


for word in str1:
   print(stemmer.stem(word))


# In[15]:


nltk.download('wordnet')


# In[16]:


from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()


# In[19]:


str2 = "Playing and Singing both with Two girls and stop the running mice"
str2 = nltk.word_tokenize(str2)


# In[20]:


str2


# In[23]:


for word in str2:
    print(lemmatizer.lemmatize(word))


# In[ ]:




