
import requests
from bs4 import BeautifulSoup


# In[177]:


url="http://www.bbc.com/sport/football/spanish-la-liga/top-scorers"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[17]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[16]:

l=[]
topscorerlaliga=[]
topscorerlaliga.append('La Liga')
topscorerlaliga.append('http://www.bbc.com/sport/football/spanish-la-liga/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)


url="http://www.bbc.com/sport/football/german-bundesliga/top-scorers"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[22]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[23]:
topscorerlaliga=[]
topscorerlaliga.append('bundesliga')
topscorerlaliga.append('http://www.bbc.com/sport/football/german-bundesliga/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)

url="http://www.bbc.com/sport/football/league-one/top-scorers"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[37]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[38]:

topscorerlaliga=[]
topscorerlaliga.append('League One')
topscorerlaliga.append('http://www.bbc.com/sport/football/league-one/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)

url="http://www.bbc.com/sport/football/french-ligue-one/top-scorers"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[25]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[26]:

topscorerlaliga=[]
topscorerlaliga.append('ligue 1')
topscorerlaliga.append('http://www.bbc.com/sport/football/french-ligue-one/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)
url="http://www.bbc.com/sport/football/premier-league/top-scorers"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[19]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[20]:
topscorerlaliga=[]
topscorerlaliga.append('premier league')
topscorerlaliga.append('http://www.bbc.com/sport/football/premier-league/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)

url="http://www.bbc.com/sport/football/scottish-championship/top-scorers"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[34]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[35]:

topscorerlaliga=[]
topscorerlaliga.append('Scottish Championship')
topscorerlaliga.append('http://www.bbc.com/sport/football/scottish-championship/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)

url='http://www.bbc.com/sport/football/scottish-premiership/top-scorers'


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[40]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[41]:

topscorerlaliga=[]
topscorerlaliga.append('Scottish premiership')
topscorerlaliga.append('http://www.bbc.com/sport/football/scottish-premiership/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)

url="http://www.bbc.com/sport/football/italian-serie-a/top-scorers"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[28]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[29]:


topscorerlaliga=[]
topscorerlaliga.append('Serie A')
topscorerlaliga.append('http://www.bbc.com/sport/football/italian-serie-a/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)


url="http://www.bbc.com/sport/football/fa-cup/top-scorers"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[28]:


alltables=soup.findAll("div",{'class':'top-player-stats__body'})


# In[29]:


topscorerlaliga=[]
topscorerlaliga.append('fa cup')
topscorerlaliga.append('http://www.bbc.com/sport/football/fa-cup/top-scorers')
for i in range(len(alltables)):
    name=alltables[i].findAll('h2',{'class':'top-player-stats__name gel-double-pica'})[0].text
    team=alltables[i].findAll('span',{'class':'gel-long-primer team-short-name'})[0].text
    goal=alltables[i].findAll('span',{'class':'top-player-stats__goals-scored-number'})[0].text
    assist=alltables[i].findAll('span',{'class':'top-player-stats__assists-number gel-double-pica'})[0].text
    topscorerlaliga.append([name,team,goal,assist])
l.append(topscorerlaliga)