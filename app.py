import requests
import json
from time import sleep
import dropbox
import json
import random

last_update = 0
token = '135332404:AAH69WBxJHKDlrrN3cxiG9f5_VUtbqpHGOk'
url = 'https://api.telegram.org/bot%s/' % token
dropbox_token = 'VhIK7FuIZGcAAAAAAAB9f_pJX4cPwM3usUVNiPw7JRXpDka9Vp1TZXnR8ftvlh0m'


def get_dropbox_url(subject):
	client = dropbox.client.DropboxClient(dropbox_token)
	path = '/bot_images/' + subject + '/'
	folder_metadata = client.metadata(path, list=True)
	lucky_path = random.choice(folder_metadata['contents'])
	path_to_share = lucky_path['path']
	share_link = client.share(path_to_share)
	return share_link['url']




while True:
	# We request for new messages in the telegram server
	get_updates = json.loads(requests.get(url + 'getUpdates', params=dict(offset=last_update+1)).text)
	for update in get_updates['result']:
		if last_update < update['update_id']:
			last_update = update['update_id']
			if update.get('message') != None:
				# Here we handle the new messages content
				if update['message'].get('text') != None:
					subject = update['message']['text']
					if subject in ('eli', 'rudy', 'kawa', 'piero', 'mazzini', 'ubillus', 'yayo', 'otros'):
						# armar request a dropbox
						dropbox_url = get_dropbox_url(subject)
						requests.get(url + 'sendMessage', params=dict(chat_id=update['message']['chat']['id'], text=dropbox_url))
					else:
						requests.get(url + 'sendMessage', params=dict(chat_id=update['message']['chat']['id'], text='sup?'))
	sleep(3)

