import os

import discord
from dotenv import load_dotenv
from emojize import Emojize
import random

e = Emojize()
load_dotenv()
TOKEN = 'NDQxMzgwNTY5NjcxMjcwNDEw.WupJsA.UpdXgwaxCGgF7vSTPX64reZ7OXw'

client = discord.Client()


@client.event
async def on_message(message):
    #print(message.author, client.user, type(client.user))
    #print(randomn)
    randomn = random.randint(0,20)
    
    if message.author == client.user:
        return

    if randomn <= 10:
        emoji = e.predict(message.content)
        if emoji != '':
            await message.add_reaction(emoji)

print(TOKEN)
client.run(TOKEN)
