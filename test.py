import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('jungsanfile-e5ae2dbc8879.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM/edit#gid=0')

sheet1 = doc.worksheet('재고주문')


client = discord.Client()


@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='주문재고 전달', type=1))




@client.event
async def on_message(message):
	if message.content.startswith('!단가'):
		if message.author.voice == None:
			await client.send_message(message.channel, '음성안내는 각 매장에 입장하셔야 안내합니다.')
    


                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
