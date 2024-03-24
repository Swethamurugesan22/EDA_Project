#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt                       
from tabulate import tabulate                         
import matplotlib as mat                             
import seaborn as sns                                 
import pandas as pd                                
import numpy as np                                    


# In[3]:


df=pd.read_csv(r'C:\Users\yuvi\Downloads\data_NEW.csv')
df


# In[4]:


#Level0
df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


#level1
df_cat=df.select_dtypes(include='object')
df_num=df.select_dtypes(exclude='object')
df_cat.dtypes
df_num.dtypes


# In[44]:


df_cat.isnull().sum()


# In[10]:


#Removing the null values of catgorical data
df['NAME_TYPE_SUITE'].fillna(df['NAME_TYPE_SUITE'].mode()[0],inplace=True)
df['OCCUPATION_TYPE'].fillna(df['OCCUPATION_TYPE'].mode()[0],inplace=True)
df_cat=df.select_dtypes(include='object')
df_cat.isnull().sum()


# In[11]:


df_num.isnull().sum()


# In[12]:


#Removing the null values of numerical data
df_num['AMT_GOODS_PRICE'].fillna(df_num['AMT_GOODS_PRICE'].median(),inplace=True)
df_num['CNT_FAM_MEMBERS'].fillna(df_num['CNT_FAM_MEMBERS'].median(),inplace=True)
df_num.isnull().sum()


# In[27]:


#Analysis on Target
fig,ax = plt.subplots(1, 2, figsize = (15, 7))
ax[0].set_title("Difficulties in playing loans")
percentage = df["TARGET"].value_counts()
labels = list(df["TARGET"].value_counts().index)
explode=[0.1,0.1]
sns.countplot(x = df["TARGET"],ax = ax[0],palette='viridis',linewidth=2,linestyle='-.')
ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation = 0 , ha = "right")
plt.pie(percentage,labels = labels,explode=explode, shadow=True,autopct= "%0.1f%%")
plt.legend()
plt.show()


# In[50]:


fig,ax = plt.subplots(1,2,figsize = (16, 7))
data = df["MOBILE_REACHABLE"].value_counts()
labels = data.keys()
sns.countplot(x = df["MOBILE_REACHABLE"],palette='viridis',edgecolor='black',linewidth=2,ax=ax[0])
explode=[0.2,0]
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels,explode=explode, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[15]:


#Analysis on NAME_CONTRACT_TYPE
fig,ax = plt.subplots(1, 2, figsize = (15, 7))
ax[0].set_title("NAME_CONTRACT_TYPE")
percentage = df["NAME_CONTRACT_TYPE"].value_counts()
labels = list(df["NAME_CONTRACT_TYPE"].value_counts().index)
explode=[0.3,0]
sns.countplot(x = df["NAME_CONTRACT_TYPE"],ax = ax[0],edgecolor='black',linewidth=2,linestyle='-.')
ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation = 0 , ha = "right")
plt.pie(percentage,labels = labels,explode=explode, shadow=True,autopct= "%0.2f%%")
plt.show()


# In[34]:


#Analysis on GENDER
fig,ax = plt.subplots(1, 2, figsize = (15, 7))
data = df["GENDER"].value_counts()
labels = data.keys()

sns.countplot(x = df["GENDER"],ax = ax[0],linewidth=2,linestyle='-.')
explode=[0,0.2,0]
plt.pie(x = data, autopct = "%.1f%%",explode=explode,labels = labels,shadow=True)
plt.show()


# In[ ]:


#Analaysis of car
fig,ax = plt.subplots(1, 2, figsize = (15, 7))
data = df["Car"].value_counts()
labels = data.keys()

sns.countplot(x = df["Car"],palette='dark',ax = ax[0],linewidth=2,linestyle='--')
explode=[0,0.2]
plt.pie(x = data, autopct = "%.1f%%",explode=explode,labels = labels,shadow=True)
plt.show()


# In[ ]:


#Analysis of House
fig,ax = plt.subplots(1, 2, figsize = (15, 7))
data = df["House"].value_counts()
labels = data.keys()

sns.countplot(x = df["House"],ax = ax[0],)
explode=[0,0.2]
plt.pie(x = data, autopct = "%.1f%%",labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:


#Analysis 0f CNT_Children
fig,ax = plt.subplots(1, 2, figsize = (16, 7))
data = df["CNT_CHILDREN"].value_counts()
labels = data.keys()

sns.countplot(x = df["CNT_CHILDREN"],ax = ax[0],palette='pastel',edgecolor='black',linewidth=2)
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.show()


# In[ ]:


#Analysis of Name type suite
fig,ax = plt.subplots(1, 2, figsize = (16, 7))
data = df["NAME_TYPE_SUITE"].value_counts()
labels = data.keys()
sns.countplot(x = df["NAME_TYPE_SUITE"],ax = ax[0],palette='viridis',edgecolor='black',linewidth=2)
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[40]:


#Analysis of Name income type
fig,ax = plt.subplots(1, 2, figsize = (16, 7))
data = df["NAME_INCOME_TYPE"].value_counts()
labels = data.keys()
sns.countplot(x = df["NAME_INCOME_TYPE"],ax = ax[0],palette='magma',edgecolor='black',linewidth=2)
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:


#Analysis of Name education type
fig,ax = plt.subplots(1, 2, figsize = (16, 7))
data = df["NAME_EDUCATION_TYPE"].value_counts()
labels = data.keys()
sns.countplot(x = df["NAME_EDUCATION_TYPE"],ax = ax[0],palette='dark',edgecolor='black',linewidth=2)
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:


#Analysis of Name family status
fig,ax = plt.subplots(1, 2, figsize = (16, 7))
data = df["NAME_FAMILY_STATUS"].value_counts()
labels = data.keys()
sns.countplot(x = df["NAME_FAMILY_STATUS"],ax = ax[0],palette='pastel',edgecolor='black',linewidth=2)
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:


#Analysis of occupation_type
fig,ax = plt.subplots(figsize = (16, 7))
data = df["OCCUPATION_TYPE"].value_counts()
labels = data.keys()
sns.countplot(x = df["OCCUPATION_TYPE"],palette='magma',edgecolor='black',linewidth=2)
#plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:


#Analysis of CNT FAM MEMBERS
fig,ax = plt.subplots(figsize = (16, 7))
data = df["CNT_FAM_MEMBERS"].value_counts()
labels = data.keys()
sns.countplot(x = df["CNT_FAM_MEMBERS"],palette='pastel',edgecolor='black',linewidth=2)
#plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:


#Analysis of TOTAL DOC SUBMITED
fig,ax = plt.subplots(1,2,figsize = (16, 7))
data = df["TOTAL_DOC_SUBMITTED"].value_counts()
labels = data.keys()
sns.countplot(x = df["TOTAL_DOC_SUBMITTED"],palette='magma',edgecolor='black',linewidth=2,ax=ax[0])
explode=[0.2,0,0,0,0]
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:


#Analysis of WORK_PHONE
fig,ax = plt.subplots(1,2,figsize = (16, 7))
data = df["WORK_PHONE"].value_counts()
labels = data.keys()
sns.countplot(x = df["WORK_PHONE"],palette='pastel',edgecolor='black',linewidth=2,ax=ax[0])
explode=[0.2,0]
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:


#Analysis of MOBILE_REACHABLE
fig,ax = plt.subplots(1,2,figsize = (16, 7))
data = df["MOBILE_REACHABLE"].value_counts()
labels = data.keys()
sns.countplot(x = df["MOBILE_REACHABLE"],palette='viridis',edgecolor='black',linewidth=2,ax=ax[0])
explode=[0.2,0]
plt.pie(x = data, autopct = "%.1f%%", shadow=True,labels = labels,explode=explode, pctdistance = 0.5)
plt.tight_layout()
plt.show()


# In[ ]:





# In[52]:





# In[ ]:





# In[53]:





# In[71]:


#Analysis of car
plt.pie(x=df['GENDER'].value_counts().values,labels=df['GENDER'].value_counts().index,autopct='%.1f%%')
plt.show()


# In[72]:


#Analysis of House
plt.pie(x=df['House'].value_counts().values,labels=df['House'].value_counts().index,autopct='%.1f%%')
plt.show()


# In[ ]:




