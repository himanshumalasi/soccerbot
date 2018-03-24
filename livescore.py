
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[11]:


url="https://www.theguardian.com/football/live"


# In[87]:


r=requests.get(url)


# In[88]:


soup=BeautifulSoup(r.content,"html5lib")


# In[89]:


allleague=soup.findAll("div",{"class":"football-table__container"})


# In[90]:


allleagues2=[]
l=[]
for i in range(len(allleague)):
    pleague=allleague[i].findAll("table",{"class":"table table--football football-matches table--responsive-font"})
    leaguename=pleague[0].findAll("caption",{"class":"table__caption table__caption--top"})
    l.append(leaguename[0].findAll('a')[0].text)
    for j in range(len(pleague)):
        allmatches=pleague[j].findAll("tr",{"class":"football-match football-match--live"})
        s={}
        for k in range(len(allmatches)):
            match=allmatches[k].findAll('span',{"class":"team-name__long"})
            score=allmatches[k].findAll('div',{"class":"football-team__score"})
            s["match"]=match[0].text+" "+score[0].text+"-"+score[1].text+" "+match[1].text
            s['link']=allmatches[k]['data-link-to']
            l.append(s)
            s={}
    allleagues2.append(l)
    l=[]






