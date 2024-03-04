#!/usr/bin/python3

import discord
from datetime import timedelta

class Lala(discord.Client):
    async def on_ready(self):
        print("Started!!!")
        self.bads = ["spam", "scam", "böse", "pong", "ping", "gewinnspiel", "gratis", "glücksspiel"]
        self.timeouts = {"karl.akemsoft.com": 1, "tyranni": 2, "schädlich": 2, "gezielt zu unterdrücken": 2}
        self.usersend= await client.fetch_user("1060542604573425724")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.author.name != "superai.ai" and message.channel.name != "spam-test":
            for bd in self.bads:
                if bd in message.content.lower():
                    print(message.author.name + " hat eine Böse Nachricht geschrieben: " + message.content)
                    await message.delete()
                    await message.author.send("Ihre Nachricht '" + message.content + "' wurde entfernt! Wenn diese Nachricht nicht böse war, sage dass @superai.ai")

            for bd in self.timeouts.keys():
                if bd in message.content.lower():
                    print(message.author.name + " hat eine Böse Timeout Nachricht geschrieben: " + message.content)
                    await message.delete()
                    timeout = timedelta(hours=self.timeouts[bd])
                    await message.author.timeout(timeout)
                    await message.author.send("Ihre Nachricht '" + message.content + "' wurde entfernt! Wenn diese Nachricht nicht timeoutig war, sage dass @superai.ai")


intents = discord.Intents.default()
intents.message_content = True
client = Lala(intents=intents)
token = open("token.txt", "r").read()
client.run(token)
