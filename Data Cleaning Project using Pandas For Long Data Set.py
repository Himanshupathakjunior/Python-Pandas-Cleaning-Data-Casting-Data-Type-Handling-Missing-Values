#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# navalue = ['NA','Missing']
# df = pd.read_csv("survey_results_public.csv",index_col="Respondent",na_values= navalue)


# In[3]:


df = pd.read_csv("survey_results_public.csv",index_col="Respondent")
schema_df = pd.read_csv("survey_results_schema.csv")


# In[4]:


pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)


# In[5]:


df.head()


# In[6]:


df.replace('NA',np.nan,inplace=True)
df


# In[7]:



df.replace('None',np.nan,inplace=True)
df


# In[8]:


df.replace('Missing',np.nan,inplace=True)
df


# In[ ]:





# In[9]:


df


# In[10]:


df['YearsCode'].head(10)


# In[ ]:





# In[11]:


df['YearsCode'].unique()


# In[12]:


df['YearsCode'].replace('Less than 1 year',0,inplace = True)
df['YearsCode'].replace('More than 50 years',51,inplace = True)


# In[13]:


df['YearsCode'] = df['YearsCode'].astype(float)
df['YearsCode'].mean()


# In[14]:


df['YearsCode'].median()


# In[15]:


expavg = df['YearsCode'].mean()
expavg


# In[36]:


# df['YearsCode'].replace('Less than 1 year',0,inplace = True)

df['YearsCode'].fillna(0,inplace=True)
df['YearsCode'].replace(0.0,expavg,inplace=True)


# In[37]:


df['YearsCode'].replace(0.0,expavg)


# In[38]:


df['YearsCode'].unique()


# In[40]:


df.head()


# In[42]:


df.tail()


# In[46]:


df['Age1stCode'].unique()


# In[54]:


df['Age1stCode'].replace('Younger than 5 years',5,inplace = True)
df['Age1stCode'].replace('Older than 85',86,inplace = True)

df['Age1stCode'].unique()


# In[69]:


df['Age1stCode'] = df['Age1stCode'].astype(float)
fcodeavg=df['Age1stCode'].mean()
fcodeavg


# In[70]:


df['Age1stCode'].fillna(0,inplace=True)
df['Age1stCode'].unique()


# In[71]:


df['Age1stCode'].replace(0.0,fcodeavg,inplace=True)


# In[72]:


df['Age1stCode'].unique()


# In[75]:


df.head()


# In[77]:


df.tail()


# In[ ]:


Remainig Same  

