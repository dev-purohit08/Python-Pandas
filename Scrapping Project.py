#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url=('https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue')


# In[4]:


page=requests.get(url)


# In[5]:


soup=BeautifulSoup(page.text, 'html')


# In[8]:


soup.find_all('table')[1]


# In[9]:


soup.find('table', class_='wikitable sortable')



# In[18]:


table=soup.find_all('table')[1]


# In[19]:


world_titles=table.find_all('th')


# In[20]:


world_table_titles= [title.text.strip() for title in world_titles]


# In[21]:


print(world_table_titles)


# In[26]:


import pandas as pd


# In[27]:


df=pd.DataFrame(columns=world_table_titles)


# In[28]:


df


# In[30]:


column_data = table.find_all('tr')


# In[35]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    world_table_rows= [data.text.strip() for data in row_data]
    
    length=len(df)
    df.loc[length]=world_table_rows


# In[36]:


df


# In[37]:


cd E:/Pandas


# In[40]:


df.to_csv('Companies1.csv',index=False)


# In[44]:


table2=soup.find_all('table')[3]


# In[45]:


table2


# In[51]:


world_titles=table2.find_all('th')


# In[53]:


world_title= [title2.text.strip() for title2 in world_titles]


# In[54]:


world_title


# In[55]:


df2=pd.DataFrame(columns=world_title)


# In[56]:


df2


# In[60]:


column_data=table2.find_all('tr')


# In[61]:


column_data


# In[69]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    row_world= [rows.text.strip() for rows in row_data]
    length=len(df2)
    df2.loc[length]=row_world


# In[70]:


df2

