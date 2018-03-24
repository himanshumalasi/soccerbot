import apiai
import json
from table import alltables
from fixtures import allleagues
from resulttoday import allleagues1
from world import allteams
from livescore import allleagues2
from playerranking import allplayers
from isl import islteams
from ileague import ileague
from topscorers import l
# api.ai client 
APIAI_ACCESS_TOKEN = "apiai access token"
ai = apiai.ApiAI(APIAI_ACCESS_TOKEN)

league_categories=[("Laliga","Top scorer of Laliga"),("Serie A","Top Scorer of Serie A"),("Ligue 1","Top Scorer of league 1"),("Scottish Premiership","Top Scorer of Scottish Premiership"),
("Scottish Championship","Top Scorer for Scottish Championship"),("League one","Top Scorer of league one"),("Fa Cup","Top Scorer of Fa cup"),("Bundesliga","Top scorer of Bundesliga"),("Premier league","Top scorer of premier league")]
HELP_MSG = """
Hey! I am ScoreBot. 
I can provide you score,result,table from all around the worlds leagues :)
This app will show you today result and fixture.
"""


def func(params):
	league=params.get('league')
	if league=='isl'or league=='ISL' or league=='Indian Super League' or league=='indian super league' or league=='INDIAN SUPER LEAGUE':
		st='Indian Super League'+'\n'
		st=st+'Pos  Club        P  W  D  L  GD  Pts'+'\n'
		for i in range(len(islteams)):
			for j in range(len(islteams[i])):
				st=st+islteams[i][j]+'  '
			st=st+'\n'
		return st
	elif league=='ileague' or league=='il' or league=='IL' or league=='I LEAGUE' or league=='I league':
		st='Indian I League'+'\n'
		st=st+'Pos  Name       P  W  D  L  +/-  PTS'+'\n'
		for i in range(len(ileague)):
			for j in range(len(ileague[i])):
				st=st+ileague[i][j]+' '
			st=st+'\n'
		return st
	else:
		for i in range(len(alltables)):
			if league.lower() in alltables[i][0].lower():
				st=alltables[i][0]+'\n'
				for j in range(1,len(alltables[i])):
					for k in range(len(alltables[i][j])):
						st=st+alltables[i][j][k]+'  '
					st=st+'\n'
		return st
		return "error"


def livescore(params):
	st=''
	for i in range(len(allleagues)):
		for j in range(len(allleagues[i])):
			if j==0:
				st=st+allleagues[i][j]+'\n'
			else:
				st=st+allleagues[i][j]['match']+'\n'
	if len(st)==0:
		return 'no ongoing matches'
	else:
		return st



def fixture(params):
	st=[]
	league=params.get('league')
	for i in range(len(allleagues)):
		if league.lower() in allleagues[i][0].lower():
			for j in range(1,len(allleagues[i])):
				element={}
				element['title'] = allleagues[i][0]
				#element['image_url'] = allteams[i][4]
				element['subtitle']='FIXTURE:'+allleagues[i][j]['match']
				#element['item_url'] =allteams[i][3]
				element['buttons'] = [{
				"type":"web_url",
				"title":"Read more about match",
				"url":allleagues[i][j]['link']}]
				st.append(element)
			break
	if len(st)==0:
		return "No Matches today"
	return st[:10]


"""def resultstoday(params):
	st=''
	for i in range(len(allleagues1)):
		for j in range(len(allleagues1[i])):
			if j==0:
				st=st+allleagues1[i][j]+'\n'
			else:
				st=st+allleagues1[i][j]['match']+'\n'
	if len(st)==0:
		return 'no ongoing matches'
	else:
		return st
"""

def resultstoday(params):
	st=[]
	league=params.get('league')
	for i in range(len(allleagues1)):
		if league.lower() in allleagues1[i][0].lower():
			for j in range(1,len(allleagues1[i])):
				element={}
				element['title'] = allleagues1[i][0]
				#element['image_url'] = allteams[i][4]
				element['subtitle']='RESULT:'+allleagues1[i][j]['match']
				#element['item_url'] =allteams[i][3]
				element['buttons'] = [{
				"type":"web_url",
				"title":"Read more about match",
				"url":allleagues1[i][j]['link']}]
				st.append(element)
			break
	if len(st)==0:
		return "No Matches today"
	return st[:10]


def worldranking(params):
	st=[]
	for i in range(0,10):
		element={}
		element['title'] = allteams[i][0]+'  '+allteams[i][1]
		element['image_url'] = allteams[i][4]
		element['subtitle']='POINTS: '+allteams[i][2]
		element['item_url'] =allteams[i][3]
		element['buttons'] = [{
				"type":"web_url",
				"title":"Read more",
				"url":allteams[i][3]}]
		st.append(element)
	return st


def worldrankingforteam(params):
	countryname=params.get('geo-country')
	st=[]
	for i in range(len(allteams)):
		if allteams[i][1]==countryname:
			element={}
			element['title'] = 'RANK: '+allteams[i][0]+'  '+'TEAM NAME: '+allteams[i][1]
			element['image_url'] = allteams[i][4]
			element['subtitle']='POINTS: '+allteams[i][2]
			element['buttons'] = [{
				"type":"web_url",
				"title":"Read more",
				"url":allteams[i][3]}]
			st.append(element)
			break

	return st

'''def worldranking(params):
	st=''
	for i in range(0,10):
		for j in range(len(allteams[i])):
			if(j!=4 and j!=3):
				st=st+allteams[i][j]+' '
		st+='\n'
	return st
'''


def playerranking(params):
	st=[]
	for i in range(0,10):
		element={}
		element['title'] = allplayers[i][0]+'  '+allplayers[i][1]
		element['image_url'] = allplayers[i][3]
		element['subtitle']=allplayers[i][2]
		element['item_url'] =allplayers[i][4]
		element['buttons'] = [{
					"type":"web_url",
					"title":"Read more",
					"url":allplayers[i][4]}]
		st.append(element)
	
	return st


def scorer(params):
	st=[]
	league=params.get('league')
	for i in range(len(l)):
		if league.lower() in l[i][0].lower():
			for j in range(2,len(l[i])):
				element={}
				element['title'] = l[i][j][0]+' , '+l[i][j][1]
					#element['image_url'] =l[i][3]
				element['subtitle']='Goals :'+l[i][j][2]+' '+'Assists :'+l[i][j][3]
					#element['item_url'] =allplayers[i][4]
				element['buttons'] = [{
					"type":"web_url",
					"title":"Read more",
					"url":l[i][1]}]
				st.append(element)
			break
	
	return st[:10]

def apiai_response(query, session_id):
	"""
	function to fetch api.ai response
	"""
	request = ai.text_request()
	request.lang = 'en'
	request.session_id = session_id
	request.query = query
	response = request.getresponse()
	return json.loads(response.read().decode('utf8'))


def parse_response(response):
	"""
	function to parse response and 
	return intent and its parameters
	"""
	result = response['result']
	params = result.get('parameters')
	intent = result['metadata'].get('intentName')
	return intent, params

	
def fetch_reply(query, session_id):
	"""
	main function to fetch reply for chatbot and 
	return a reply
	"""
	response = apiai_response(query, session_id)
	#print(response)
	intent, params = parse_response(response)
	reply = {}
	if response['result']['action'].startswith('smalltalk'):
		reply['type'] = 'smalltalk'
		reply['data'] = response['result']['fulfillment']['speech']
	

	elif intent == "points_table":
		reply['type']="points_table"
		reply['data']=func(params)
		if reply['data']=="error":
			reply['type']='none'
	

	elif intent=="live_score":
		reply['type']='live_score'
		reply['data']=livescores(params)
		if reply['data']=="error":
			reply['type']='none'
	

	elif intent=='fixture':
		reply['type']='fixture'
		reply['data']=fixture(params)
		print(reply['data'])
		if reply['data']=="error":
			reply['type']='none'
	

	elif intent=='result_today':
		reply['type']='resulttoday'
		reply['data']=resultstoday(params)
		if reply['data']=="error":
			reply['type']='none'
	

	elif intent=='world_ranking':
		reply['type']='worldranking'
		reply['data']=worldranking(params)
		if reply['data']=="error":
			reply['type']='none'

	
	elif intent=='worldranking_team':
		reply['type']='worldrankingforteam'
		reply['data']=worldrankingforteam(params)
		if reply['data']=="error":
			reply['type']='none'
	

	elif intent=='live_score':
		reply['type']='livescore'
		reply['data']=livescore(params)
		if reply['data']=="error":
			reply['type']='none'
	
	
	elif intent=='playerranking':
		reply['type']='playerranking'
		reply['data']=playerranking(params)
		if reply['data']=="error":
			reply['type']='none'
	
	
	elif intent=='scorer':
		reply['type']='scorer'
		reply['data']=scorer(params)
		if reply['data']=="error":
			reply['type']='none'
	
	else:
		reply['type'] = 'none'
		reply['data'] = 'sorry'
		
	return reply
