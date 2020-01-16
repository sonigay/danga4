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
async def JointheVC(VCchannel, TXchannel):
	global chkvoicechannel
	global voice_client1

	if VCchannel is not None:
		if chkvoicechannel == 0:
			voice_client1 = await VCchannel.connect(reconnect=True)
			if voice_client1.is_connected():
				await voice_client1.disconnect()
				voice_client1 = await VCchannel.connect(reconnect=True)
			chkvoicechannel = 1
			#await PlaySound(voice_client1, './sound/hello.mp3')
		else :
			await voice_client1.disconnect()
			voice_client1 = await VCchannel.connect(reconnect=True)
			#await PlaySound(voice_client1, './sound/hello.mp3')
	else:
		await TXchannel.send('음성채널에 먼저 들어가주세요.', tts=False)
		
		
			if message.content.startswith('단가'):
				if message.author.voice == None:
					await client.get_channel(channel).send('음성안내는 각 매장에 입장하셔야 안내합니다.', tts=False)
				else:
					voice_channel = message.author.voice.channel

					if voice_channel.id == "":
						file_data_voiceCH = base64.b64decode(inidata_voiceCH.content)
						file_data_voiceCH = file_data_voiceCH.decode('utf-8')
						inputData_voiceCH = file_data_voiceCH.split('\n')

						for i in range(len(inputData_voiceCH)):
							if inputData_voiceCH[i] == 'voicechannel = \r':
								inputData_voiceCH[i] = 'voicechannel = ' + str(voice_channel.id) + '\r'
								

						result_voiceCH = '\n'.join(inputData_voiceCH)

						contents = int(voice_channel.id)
						
						

					elif voice_channel.id != int(voice_channel.id):
						file_data_voiceCH = base64.b64decode(inidata_voiceCH.content)
						file_data_voiceCH = file_data_voiceCH.decode('utf-8')
						inputData_voiceCH = file_data_voiceCH.split('\n')

						for i in range(len(inputData_voiceCH)):
							if inputData_voiceCH[i] == 'voicechannel = ' + str(voice_channel.id) + '\r':
								inputData_voiceCH[i] = 'voicechannel = ' + str(voice_channel.id) + '\r'
								

						result_voiceCH = '\n'.join(inputData_voiceCH)
						contents = int(voice_channel.id)
						
						
						

					await JointheVC(voice_channel, channel)
					await client.get_channel(channel).send('< 거래처 [' + client.get_channel(voice_channel.id).name + '] 이동완료>', tts=False)    


                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
