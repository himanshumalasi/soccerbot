
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


url="http://www.skysports.com/football/tables"


# In[4]:


r=requests.get(url)


# In[5]:


soup=BeautifulSoup(r.content,'html5lib')


# In[45]:

allleagues=soup.findAll('div',{"class":"page-filters__offset"})
alltables=[]
p=[]
for i in range(len(allleagues)):
    pleague=allleagues[i].findAll('a',{"class":"standing-table block"})
    for j in range(len(pleague)):
    	p.append(pleague[j].findAll('caption',{"class":"standing-table__caption"})[0].text.replace('\n',''))
    	body=pleague[j].findAll('tbody')
    	for k in range(len(body)):
    		rows=body[k].findAll('tr',{"class":"standing-table__row"})
    		for l in range(len(rows)):
    			q=[]
    			q.append(rows[l].findAll("td",{"class":"standing-table__cell"})[0].text)
    			q.append(rows[l].findAll("td",{"class":"standing-table__cell"})[1].text)
    			q.append(rows[l].findAll("td",{"class":"standing-table__cell"})[2].text)
    			q.append(rows[l].findAll("td",{"class":"standing-table__cell"})[3].text)
    			q.append(rows[l].findAll("td",{"class":"standing-table__cell"})[4].text)
    			p.append(q)
    	alltables.append(p)
    	p=[]
