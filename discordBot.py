import os
import random

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
    
    members = '\n -'.join(member.name for member in guild.members)
    print(f"The members of the guild are \n -{members}\n")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hello {member.name}. Welcome to Bot Development."
    )
    print(f"-{member.name} has been welcomed to the Guild.")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(client.user.id) in message.content:
        randomResponses = [
            "He lost his ticket for the movie.",
            "I can hardly wait till I see you.",
            "My father loves pizza.",
            "I don't know what Mary is looking for.",
            "He's in bed with the flu.",
            "I'll pay the bill.",
            "You can say whatever you want to.",
            "OK. Now what?",
            "What time did you wake up this morning?",
            "The bottle smashed to pieces.",
            "Well, you could go down to 22nd street. There are lot of stores down there that are open 24 hours a day.",
            "He was dropped from the team for using drugs."
        ]
        response = random.choice(randomResponses)
        await message.channel.send(response)
        print(f"Responded to {message.author}")
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(error, *args, **kwargs):
    with open('err.log', 'a') as f:
        if error == 'on_message':
            f.write(f"Unhandled Message: {args[0]}\n")
            print('Logged Error... \n')

client.run(TOKEN)