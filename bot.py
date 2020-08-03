import os

import discord
from dotenv import load_dotenv
from emojize import Emojize
import random

print()

e = Emojize()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


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
