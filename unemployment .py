#!/usr/bin/env python
# coding: utf-8

# # IMPORTING LIBRARIES

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# In[7]:


unemployment = pd.read_csv('unemployement.csv',low_memory=False)


# In[8]:


unemployment.head()


# In[9]:


unemployment.tail()


# In[10]:


unemployment.info()


# In[11]:


#now, we are checking start with a pairplot, and check for missing values
sns.heatmap(unemployment.isnull(),cbar=False)


# In[20]:


#Which state has the most data
color = sns.color_palette()
cnt_srs = unemployment.Region.value_counts()

plt.figure(figsize=(8,5))
sns.barplot(x=cnt_srs.index, y=cnt_srs.values, alpha=0.8, color=color[1])
plt.ylabel('Number of Occurrences', fontsize=15)
plt.xlabel('Region', fontsize=15)
plt.title('Count the Region', fontsize=15)
plt.xticks(rotation='vertical')
plt.show()


# In[32]:


grouped_df = unemployment.groupby(["Region"])["longitude"].aggregate("mean").reset_index()

plt.figure(figsize=(8,5))
sns.pointplot(x=grouped_df['Region'].values, y=grouped_df['longitude'].values, color=color[2])
plt.ylabel('Mean rate', fontsize=12)
plt.xlabel('States', fontsize=12)
plt.title("Average of mean", fontsize=15)
plt.xticks(rotation='vertical')
plt.show()


# In[33]:


unemployment.Region.nunique()


# In[37]:


make_total = unemployment.pivot_table("longitude",index=['Region'],aggfunc='mean')
topstate=make_total.sort_values(by='longitude',ascending=False)[:47]
print(topstate)


# In[ ]:




