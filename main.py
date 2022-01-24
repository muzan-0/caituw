import discord
import os
import requests
import errors
import random
import re

prefix = '?'

client = discord.Client()

dscregex = re.compile('?')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}\n')


@client.event
async def on_message(message):
  
    print(f'{message.guild}\n#{message.channel}\n@{message.author}\n"{message.content}""\n')
  
    if message.author == client.user:
        return

    if message.content.startswith(f'{prefix}ping'):
        await message.channel.send(
            f'pong dumbass :upside_down: \n**{round(client.latency) * 1000}ms**'
        )

    if message.content.startswith(f'{prefix}insult'):
        await message.channel.send(
            requests.get('https://insult.mattbas.org/api/insult').text)

    if message.content.startswith(f'{prefix}bully'):
        if message.author.guild_permissions.administrator:
            for i in range(10):
                await message.channel.send('@everyone')
        else:
            await message.channel.send(errors.NO_PERMISSION)

    if message.content.startswith(f'{prefix}dead'):
        await message.channel.send(
            random.choice([
                'ur ded lol', 'alive, but not for long\n(look behind u)',
                'ur alive (imagine)', ':skull:'
            ]))

    if message.content.startswith(f'{prefix}cope'):
        await message.channel.send('cope')
    if message.content.startswith(f'{prefix}source'):
        await message.channel.send(f'''
    Caituw is and always will be open source on github:thumbsup:
<https://github.com/muzan-0/caituw>

Hosted on repl.it
<https://replit.com/@MicahEaton/caituw?v=1>
    ''')


client.run(os.getenv('TOKEN'))
