
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[13]:


url='http://www.firstpost.com/isl-2017-18/schedule/'


# In[14]:


r=requests.get(url)


# In[15]:


soup=BeautifulSoup(r.content,'html5lib')


# In[45]:


body=soup.findAll('div',{'class':'fixture-list'})


# In[44]:


l=[]
fixtureisl=[]
for i in range(1,len(body)):
    name1=body[i].findAll('h2',{'class':'team-a'})[0].text
    name2=body[i].findAll('h2',{'class':'team-b'})[0].text
    name=l.append(name1+' VS '+name2)
    time=body[i].findAll('span',{'class':'time'})[0].text
    d=body[i].findAll('p',{'class':'venue'})[0].text.split(',')
    date=d[0]+' '+d[1]
    l.append(time)
    l.append(date)
    fixtureisl.append(l)
    l=[]
print(fixtureisl)

