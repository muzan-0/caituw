import discord
import os
import requests
import errors


client = discord.Client()



@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('?ping'):
    await message.channel.send(f'pong dumbass :upside_down: \n**{round(client.latency) * 1000}ms**')

  if message.content.startswith('?insult'):
    await message.channel.send(requests.get('https://insult.mattbas.org/api/insult').text)

  if message.content.startswith('?bully'):
    if message.author.guild_permissions.administrator:
      for i in range(10):
        await message.channel.send('@everyone')
    else:
      await message.channel.send(errors.NO_PERMISSION)

client.run(os.getenv('TOKEN'))

