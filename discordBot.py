import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default().all()

load_dotenv()
TOKEN = os.getenv('discordToken')
guildCorrect = os.getenv('discordGuild')


class ConnectToDiscord():
    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

ConnectToDiscord().run(TOKEN)