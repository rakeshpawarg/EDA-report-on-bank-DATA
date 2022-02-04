#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv('bank-1.csv',sep=';')


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.loc[(df.education=='tertiary')]


# In[8]:


df[['balance','education']].max()


# In[9]:


df['balance'].min()


# In[10]:


df.loc[(df.balance<0)].count()


# In[11]:


df.loc[(df.marital=='single'),"loan"].count()


# In[12]:


df.loc[(df.age>60)&(df.loan=='no')]


# In[13]:


df['age'].min()


# In[30]:


#round(100*(df.isnull().sum()/len(df.index)),2)


# In[17]:


import seaborn as sns
sns.countplot(y="job", data=df)
plt.xlim(0,1000)


# In[100]:


sns.histplot(df.age,kde=True)


# In[5]:


df.loc[(df.age>31)&(df.age<35)]


# In[9]:


df.loc[(df.age<60)]


# In[11]:


4347+127


# In[10]:


df.loc[(df.age>60)]


# In[17]:


plt.figure(figsize=(17, 6))
sns.barplot(x='job', y='balance', data=df)


# In[9]:


df.loc[(df.age>60)&(df.loan=='yes')]


# In[21]:


df.loc[(df.education=='primary'),'loan']


# In[24]:


sns.displot(df['housing'])


# In[25]:


sns.displot(df['loan'])


# In[45]:


a=(df.loc[(df.housing=='yes'),'age'])


# In[48]:


plt.figure(figsize=(19, 6))
sns.barplot(x='job', y=a, data=df)


# In[77]:


plt.pie(x=df['job'],y=df['balance'])


# In[92]:


df.loc[(df.marital=='married')&(df.housing=='yes')].count()


# In[103]:


df.info()


# In[11]:


df[['month','duration']]


# In[20]:


df.groupby(by='month'),['duration'])


# In[30]:


plt.pie(df.groupby(by='housing')['job'].count())
plt.show()


# In[31]:


df.groupby(by='housing')['job'].count()


# In[32]:


df.groupby(by='marital')['housing'].count()


# In[50]:


df.groupby(by='job')['loan'].count()


# In[51]:


df.groupby(by='job').count()


# In[62]:


df[['campaign','poutcome']]


# In[70]:


df.loc[(df.poutcome=='success')].count()


# ### 
# 3705+197+490+129

# In[91]:


3705+197+490+129


# In[85]:


plt.pie(df.groupby(by='poutcome')['poutcome'].count())
plt.show()


# In[90]:


a=df.groupby(by='poutcome')['campaign']


# In[95]:


df.groupby(by='poutcome').count()


# In[4]:


df.describe()


# In[7]:


df.hist(figsize=(21,17))


# In[11]:


import seaborn as sns
sns.boxplot(x='education',y='age',data=df)


# In[ ]:




