from flask import Flask, request
import requests
import json 
from pymessenger import Bot
from utils import fetch_reply, worldranking,HELP_MSG,league_categories
app = Flask(__name__)

FB_ACCESS_TOKEN = "EAACLbZBL02vkBAJN8G9BBQsgILD1wJkwTpL9vM4JVsxZBAYBBhQNlLKifxYOJ47iROwZBnd5xo25ZCqaZAHVlNdRGEN6UTR0cE5QLLoJhZAIRYdFTjFiqrohLbygjRMtEsqk5MxH2EblCzpWLgzTGorZAlEmdNKmXYoycFmsiNm3AZDZD"
bot = Bot(FB_ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	print(request.data)
	data = request.get_json()

	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:

				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# HANDLE NORMAL MESSAGES HERE
					if messaging_event['message'].get('text'):
						# HANDLE TEXT MESSAGES
						query = messaging_event['message']['text']
						# ECHO THE RECEIVED MESSAGE
						################ BUTTON EXAMPLE #######################
						if query == "button":
							buttons = [{"type":"web_url",
										"url": "https://youtube.com/IndianPythonista",
										"title":"My channel"}]
							bot.send_button_message(sender_id, "Check out this link!", buttons)

							return "ok", 200
						#######################################################


						if messaging_event['message'].get('quick_reply'):
							# HANDLE TEXT MESSAGE WITH QUICK REPLY
							payload = messaging_event['message']['quick_reply']['payload']
							if payload in list(zip(*league_categories))[1]:
								query = payload
						try:
							reply = fetch_reply(query, sender_id)
						except Exception as e:
							reply={}
							reply['data']="Sorry Can't Understand"
							reply['type']="none"
						try:
							if reply['type'] == 'points_table':
								bot.send_text_message(sender_id, reply['data'])

							elif reply['type'] == 'none':
								bot.send_text_message(sender_id, reply['data'])

							elif reply['type']=='fixture':
								if type(reply['data'])==str:
									bot.send_text_message(sender_id, reply['data'])
								bot.send_generic_message(sender_id, reply['data'])
							
							elif reply['type']=='resulttoday':
								if type(reply['data'])==str:
									bot.send_text_message(sender_id, reply['data'])
								bot.send_generic_message(sender_id, reply['data'])
							
							elif reply['type']=='worldranking':
								bot.send_generic_message(sender_id, reply['data'])
							
							elif reply['type']=='worldrankingforteam':
								if reply['data']:
									bot.send_generic_message(sender_id, reply['data'])
								else:
									bot.send_text_message(sender_id,'No Such Country')
							
							elif reply['type']=='livescore':
								if type(reply['data'])==str:
									bot.send_text_message(sender_id,reply['data'])
								bot.send_generic_message(sender_id,reply['data'])
							
							elif reply['type']=='playerranking':
								bot.send_generic_message(sender_id,reply['data'])
							
							elif reply['type']=='scorer':
								bot.send_generic_message(sender_id,reply['data'])
							else:
								bot.send_text_message(sender_id, reply['data'])	

						except Exception as e:
							bot.send_text_message(sender_id, 'sorry2')			

						
				elif messaging_event.get('postback'):
					# HANDLE POSTBACKS HERE
					payload = messaging_event['postback']['payload']
					if payload ==  'SHOW_HELP':
						bot.send_text_message(sender_id, HELP_MSG)
						bot.send_text_message(sender_id,"points table of <league name> for getting points table of league")
						bot.send_text_message(sender_id,"points table of laliga for getting points table of laliga")
						bot.send_text_message(sender_id,"fixture of <league name> for the fixture of league.\nshow me result of <league name> for getting result of league.")
						#enter extra messages
					elif payload=='w_ranking':
						data=worldranking("")
						bot.send_generic_message(sender_id, data)
					elif payload=='topscorer':
						bot.send_quickreply(sender_id,"Choose one",league_categories)
	return "ok", 200


def set_greeting_text():
	headers = {
		'Content-Type':'application/json'
		}
	data = {
		"setting_type":"greeting",
		"greeting":{
			"text":"Hi {{user_first_name}}! I am SoccerBot.I show you the details of fixture,points table and today's result and details of any ongoing matches of league..You can also see top scorer using menu or by writing top scorer of a particular league.."
			}
		}
	ENDPOINT = "https://graph.facebook.com/v2.8/me/thread_settings?access_token=%s"%(FB_ACCESS_TOKEN)
	r = requests.post(ENDPOINT, headers = headers, data = json.dumps(data))
	print(r.content)


def set_persistent_menu():
	headers = {
		'Content-Type':'application/json'
		}
	data = {
		"setting_type":"call_to_actions",
		"thread_state" : "existing_thread",
		"call_to_actions":[
			{
				"type":"web_url",
				"title":"Meet the developer",
				"url":"https://www.facebook.com/malasihimanshu" 
			},{
				"type":"postback",
				"title":"World Ranking",
				"payload":"w_ranking"
			},
			{
				"type":"postback",
				"title":"Top Scorer",
				"payload":"topscorer"
			},
			{
				"type":"postback",
				"title":"Help",
				"payload":"SHOW_HELP"
			}]
		}
	ENDPOINT = "https://graph.facebook.com/v2.8/me/thread_settings?access_token=%s"%(FB_ACCESS_TOKEN)
	r = requests.post(ENDPOINT, headers = headers, data = json.dumps(data))
	print(r.content)


set_persistent_menu()
set_greeting_text()
def get_started():
    headers = {
        'Content-Type':'application/json'
        }
    data = {
        "setting_type":"call_to_actions",
        "thread_state" : "new_thread",
        "call_to_actions":[{
            "type":"postback",
            "payload":"SHOW_HELP"
            }]
        }
    ENDPOINT = "https://graph.facebook.com/v2.8/me/thread_settings?access_token=%s"%(FB_ACCESS_TOKEN)
    r = requests.post(ENDPOINT, headers = headers, data = json.dumps(data))
get_started()

if __name__ == "__main__":
	app.run(port=8000, use_reloader = True,debug=True)
