import requests
import json
from time import sleep

last_update = 0
token = '135332404:AAH69WBxJHKDlrrN3cxiG9f5_VUtbqpHGOk'
url = 'https://api.telegram.org/bot%s/' % token

while True:
	# We request for new messages in the telegram server
	get_updates = json.loads(requests.get(url + 'getUpdates', params=dict(offset=last_update+1)).text)
	for update in get_updates['result']:
		if last_update < update['update_id']:
			last_update = update['update_id']
			if update.get('message') != None:
				# Here we handle the new messages content
				if update['message'].get('text') != None:
					if update['message']['text'] == 'crazyV':
						data = {'chat_id': update['message']['chat']['id']}
						files = {'photo': ('/Users/christianperez/Dropbox/bot_images/the_hound.jpg', open('/Users/christianperez/Dropbox/bot_images/the_hound.jpg', 'rb'))}
						requests.post(url + 'sendPhoto', data=data, files=files)
					else:
						requests.get(url + 'sendMessage', params=dict(chat_id=update['message']['chat']['id'], text=update['message']['text']))
						# print("texto: " + update['message']['text'])
	sleep(3)