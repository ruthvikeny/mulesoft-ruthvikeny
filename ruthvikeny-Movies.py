#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import Libraries
import pandas as pd
import sqlite3 as db


# In[3]:


conn = db.connect('sqlite.db')


# In[4]:


cn = conn.cursor()


# In[13]:


cn.execute("create table Movies(name_of_movie VARCHAR(50) PRIMARY KEY, lead_actor VARCHAR(50), lead_actress VARCHAR(50), year_of_release DATE, director_name VARCHAR(50))")


# In[14]:


cn.execute("SELECT name FROM sqlite_master WHERE type='table';")


# In[15]:


cn.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cn.fetchall())


# In[17]:


cn.execute("INSERT INTO Movies VALUES('THE KASHMIR FILES', 'ANUPAM KHER', 'BHASHA SUMBLI', '2022', 'VIVEK AGNIHOTRI')")
cn.execute("INSERT INTO Movies VALUES('GANGUBAI KATHIAWADI', 'SHANTANU MAHESHWARI', 'ALIA BHAT', '2022', 'SANJAY LEELA BHANSALI')")
cn.execute("INSERT INTO Movies VALUES('3 IDIOTS', 'AMIR KHAN', 'KAREENA KAPOOR KHAN', '2009', 'RAJKUMAR HIRANI')")
cn.execute("INSERT INTO Movies VALUES('BAJIRAO MASTANI', 'RANVEER SINGH', 'DEEPIKA PADUKONE', '2015', 'SANJAY LEELA BHANSALI')")
cn.execute("INSERT INTO Movies VALUES('KUCH KUCH HOTA HAI', 'SHAH RUKH KHAN', 'RANI MUKHARJEE', '1998', 'KARAN JOHAR')")


# In[19]:


new_Movies = [('DHAMAAL', 'SANJAY DUTT', 'MALLIKA SHERAWAT', '2007', 'INDRA KUMAR')]
cn.executemany('INSERT INTO Movies VALUES(?,?,?,?,?)' , new_Movies)


# In[20]:





# In[22]:


conn.commit()


# In[23]:


cn.close()
conn.close()


# In[25]:


conn = db.connect('sqlite.db')
df_Movies = pd.read_sql_query('SELECT * FROM Movies', conn)


# In[26]:


df_Movies


# In[27]:


conn = db.connect('sqlite.db')
df_Movies = pd.read_sql_query("SELECT * FROM Movies WHERE lead_actor = 'AMIR KHAN' ", conn)


# In[28]:


df_Movies


# In[29]:


conn.close()


# In[ ]:




