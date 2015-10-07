import requests
import json
from time import sleep

last_update = 0
token = '135332404:AAH69WBxJHKDlrrN3cxiG9f5_VUtbqpHGOk'
url = 'https://api.telegram.org/bot%s/' % token

while True:
	get_updates = json.loads(requests.get(url + 'getUpdates', params=dict(offset=last_update+1)).text)
	for update in get_updates['result']:
		if last_update < update['update_id']:
			last_update = update['update_id']
			if update.get('message') != None:
				# print("mensaje: " + str(update['update_id'])
				if update['message'].get('text') != None:
					# es un mensaje con texto, enviemos una respeusta
					requests.get(url + 'sendMessage', params=dict(chat_id=update['message']['chat']['id'], text=update['message']['text']))
					# print("texto: " + update['message']['text'])
	sleep(3)