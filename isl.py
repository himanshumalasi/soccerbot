
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[36]:


url='https://www.sportskeeda.com/go/isl/standings'


# In[37]:


r=requests.get(url)


# In[38]:


soup=BeautifulSoup(r.content,'html5lib')


# In[67]:
body1=soup.findAll('tr')


islteams=[]
l=[]
for i in range(1,len(body1)):
    l.append(body1[i].findAll('span',{'class':'value'})[0].text)
    l.append(body1[i].findAll('span',{'class':'keeda_football_table_team_name'})[0].text)
    data=body1[i].findAll('td')
    for i in range(len(data)):
        if i!=0 and i!=1:
            l.append(data[i].text)
    islteams.append(l)
    l=[]


