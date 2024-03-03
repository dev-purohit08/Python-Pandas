#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url='https://en.wikipedia.org/wiki/List_of_highest-grossing_films'


# In[3]:


page=requests.get(url)


# In[4]:


page


# In[7]:


soup=BeautifulSoup(page.text, 'html')


# In[36]:


table=soup.find_all('table')[0]


# In[40]:


title=table.find_all('th')


# In[41]:


title_world=[titles.text.strip() for titles in title[0:5]]


# In[42]:


title_world


# In[43]:


import pandas as pd


# In[44]:


df=pd.DataFrame(columns=title_world)


# In[57]:


df.drop('Title',axis=1,inplace=True)


# In[47]:


column_data=table.find_all('tr')


# In[58]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    row_world=[rows.text.strip() for rows in row_data[0:-1]]
    
    length=len(df)
    df.loc[length]=row_world
    


# In[59]:


df


# In[60]:


title=table.find_all('th')


# In[65]:


movie_title=[titles.text.strip() for titles in title[6:]]


# In[66]:


df['Title']=movie_title


# In[79]:


columns = df.columns.tolist()  # Get column names as a list
last_column = columns.pop()  # Remove the last column
middle_index = len(columns) // 2  # Find the middle index
columns.insert(middle_index, last_column)  # Insert the last column at the middle index

# Reassign columns to DataFrame
df = df[columns]


# In[83]:


df


# In[85]:


df.to_csv('Highest Grossing Movies.csv',index=False)


# In[84]:


cd E:/Pandas

