
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[72]:


url='http://www.goal.com/en-in/i-league/table/4pohvulrkgzx38eoqse6b5cdg'


# In[73]:


r=requests.get(url)


# In[74]:


soup=BeautifulSoup(r.content,'html5lib')


# In[85]:


body=soup.findAll('div',{'class':'table__body'})


# In[84]:


ileague=[]
for i in range(len(body)):
    rows=body[i].findAll('div',{'class':'table__row'})
    for j in range(len(rows)):
        ileague.append(rows[j].text.split())
ileague

