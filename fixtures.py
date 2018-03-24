
import requests


from bs4 import BeautifulSoup



url="https://www.theguardian.com/football/live"


r=requests.get(url)

soup=BeautifulSoup(r.content,"html5lib")
allleague=soup.findAll('div',{'class':'football-table__container'})

allleagues=[]
l=[]
for i in range(len(allleague)):
    xyz=allleague[i].findAll('tr',{'class':'football-match football-match--fixture'})
    name=allleague[i].findAll('caption',{'class':'table__caption table__caption--top'})[0].findAll('a')[0].text
    l.append(name)
    for j in range(len(xyz)):
        abc=xyz[j].findAll('td',{'class':'football-match__teams table-column--main'})
        s={}
        for k in range(len(abc)):
            match=abc[k].findAll('span',{'class':'team-name__long'})
            link=abc[k].findAll('a')[0]['href']
            s['match']=match[0].text+"  VS  "+match[1].text
            s['link']=link
            l.append(s)
            s={}
    allleagues.append(l)
    l=[]

