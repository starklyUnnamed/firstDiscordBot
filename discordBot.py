import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default().all()

load_dotenv()
TOKEN = os.getenv('discordToken')
guildCorrect = os.getenv('discordGuild')


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=guildCorrect)
    print(
        f"{client.user} has connected to the following Guild: \n"
        f"{guild.name}(id: {guild.id})"
    )
    
    members = '\n +'.join(member.name for member in guild.members)
    print(f"The members of the guild are \n +{members}")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hello {member.name}. Welcome to Bot Development."
    )

client.run(TOKEN)