
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


url='https://www.ranker.com/list/best-current-soccer-players/ranker-sports'


# In[4]:


r=requests.get(url)


# In[5]:


soup=BeautifulSoup(r.content,'html5lib')


# In[6]:


soup


# In[27]:

allplayers=[]
l=[]
body1=soup.findAll('h2',{'class':'listItem listItem__h2 listItem__h2--grid listItem__h2--popUp pointer listItem--topBorder flex relative robotoC'})
try:
	l.append(body1[0].findAll('strong',{'class':'listItem__rank block center instapaper_ignore'})[0].text)
except:
	pass
try:
	l.append(body1[0].findAll('a',{'class':'listItem__title listItem__title--link black'})[0].text)
except:
	pass
try:
	l.append(body1[0].findAll('span',{'class':'listItem__properties black default'})[0].text)
except:
	pass
try:
	l.append(body1[0].findAll('img')[0]['src'])
except:
	pass
try:
	l.append(body1[0].findAll('a',{'class':'listItem__title listItem__title--link black'})[0]['href'].split('//')[1])
except:
	pass



allplayers.append(l)
l=[]

# In[29]:


body=soup.findAll('h2',{'class':'listItem listItem__h2 listItem__h2--grid listItem__h2--popUp pointer flex relative robotoC'})


# In[35]:



for i in range(len(body)):
	try:
		l.append(body[i].findAll('strong',{'class':'listItem__rank block center instapaper_ignore'})[0].text)
		l.append(body[i].findAll('a',{'class':'listItem__title listItem__title--link black'})[0].text)
		l.append(body[i].findAll('span',{'class':'listItem__properties black default'})[0].text)
		l.append(body[i].findAll('img')[0]['src'])
		l.append(body[i].findAll('a',{'class':'listItem__title listItem__title--link black'})[0]['href'].split('//')[1])
		allplayers.append(l)
		l=[]
	except:
		pass


