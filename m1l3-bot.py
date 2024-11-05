import discord
import random   
from bot_mantik import gen_pass

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():#bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):#Sunucudaki herhangi bir kanalda bir mesaj gönderildiğinde tetiklenir.
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    
    elif message.content.startswith('$sifre'):
        await message.channel.send(gen_pass(5))
    else:
        await message.channel.send(message.content)

client.run("token")
