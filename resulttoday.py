
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[177]:


url="https://www.theguardian.com/football/results"


# In[178]:


r=requests.get(url)


# In[179]:


soup=BeautifulSoup(r.content,"html5lib")


# In[199]:


alltables=soup.findAll("div",{"football-matches__day"})


# In[213]:


allleagues1=[]
p=[]
for i in range(len(alltables)):
    pleaguetable=alltables[i].findAll('div',{"class":"football-table__container"})
    for j in range(len(pleaguetable)):
        leaguename=pleaguetable[j].findAll("caption",{"class":"table__caption table__caption--top"})
        p.append(leaguename[0].findAll('a')[0].text)
        body=pleaguetable[j].findAll('tbody')
        for k in range(len(body)):
            rows=body[k].findAll('tr',{"class":"football-match football-match--result"})
            for l in range(len(rows)):
                s={}
                ##print(rows[l].findAll('span',{"class":"team-name__long"})[0].text)
                ##print(rows[l].findAll('span',{"class":"team-name__long"})[1].text)
                ##print(rows[l].findAll('div',{"class":"football-team__score"})[0].text)
                ##print(rows[l].findAll('div',{"class":"football-team__score"})[1].text)
                s["match"]=rows[l].findAll('span',{"class":"team-name__long"})[0].text+" "+rows[l].findAll('div',{"class":"football-team__score"})[0].text+"-"+rows[l].findAll('div',{"class":"football-team__score"})[1].text+" "+rows[l].findAll('span',{"class":"team-name__long"})[1].text
                s['link']=rows[l].findAll('a')[0]['href']
                p.append(s)
                s={}
        allleagues1.append(p)
        p=[]

##if __name__ == '__main__':
##    print(allleagues1)
