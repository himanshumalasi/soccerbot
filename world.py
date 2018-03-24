import requests
from bs4 import BeautifulSoup
url='http://www.fifa.com/fifa-world-ranking/ranking-table/men/index.html'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')
body=soup.findAll('tbody')
allteams=[]
l=[]
for i in range(len(body)):
    teams=body[i].findAll('tr',{'class':'anchor'})
    for j in range(len(teams)):
        l.append(teams[j].findAll('td',{'class':'tbl-rank'})[0].text)
        l.append(teams[j].findAll('td',{'class':'tbl-teamname'})[0].text)
        l.append(teams[j].findAll('td',{'class':'tbl-points'})[0].text)
        l.append('www.fifa.com'+ teams[j].findAll('a')[0]['href'])
        l.append(teams[j].findAll('img')[0]['src'].split('//')[1])
        
        allteams.append(l)
        l=[]

