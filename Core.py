import asyncio
import discord
import random
import time

aflag = False 
mafia = True

client = discord.Client()

token='NTQxNTU5MDk4NDgzNjcxMDgx.XOoM5w.U19UPEPAL0jBfNoejFoDNyaJsJE'


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("="*10)
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("심각한 고뇌중"))

@client.event
async def on_message(message):
    channel = message.channel
    global aflag

#네로와의 티키타카
    if message.content.startswith('네로야'):
        await channel.send("왜")
        aflag = True

    if message.content.startswith('네로쟝'):
        await channel.send("우흥?")
        aflag = True   
    

    if aflag and message.content.endswith(('지?', '까?','니?')):
        await channel.send(random.choice(["아닌데?","당연하지","잘 몰라"]))
        aflag = False
        return None
    
    if aflag and message.content.endswith(('자', '구', '래?')):
        await channel.send(random.choice(['좋다','싫어']))
        aflag = False
        return None

#마피아 게임
#    if aflag and mafia and message.content.startwith('마피아')
#        await channel.send('마피아 게임을 시작합니다')
#        mafia = False
        

#    else:
#        return None




client.run(token)