import apiai
import json
import os

APIAI_ACCESS_TOKEN = os.environ.get('api_token')	

#make agent of apiai
ai =  apiai.ApiAI(APIAI_ACCESS_TOKEN) # for connecting agent and api.ai

def apiai_response(query, sender_id):

	request = ai.text_request()
	request.lang = 'en'
	request.session_id="1234"
	request.query = query
	#response = request.getresponse()

	#print (response.read())
	response = json.loads(request.getresponse().read().decode('utf-8'))
	print response


	result = response['result']
	params = result.get('parameters')
	intent = result['metadata'].get('intentName')

	default = response['result']['fulfillment']['messages'][0]['speech']
	#default  ='messi is the best'
	return intent, params , default
	#print intent, params


#print apiai_response("hi",1234)