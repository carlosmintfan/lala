#!/usr/bin/python3

import discord
from datetime import timedelta

class Lala(discord.Client):
    async def on_ready(self):
        print("Started!!!")
        self.bads = ["spam", "scam", "böse", "pong", "ping", "gewinnspiel", "gratis", "glücksspiel", "sapm", "masp"]
        self.timeouts = {"karl.akemsoft.com": 1, "tyranni": 2, "schädlich": 2, "gezielt zu unterdrücken": 2}
        self.usersend= await client.fetch_user("1060542604573425724")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
            
        if isinstance(message.channel, discord.channel.DMChannel):
            # Dm message
            await message.author.send("Hallo " + message.author.name + "! Leider hab ich noch keine Funktionen in Direktnachrichten!")
        else:
            self.log("Neue Nachricht von " + message.author.name + ": " + message.content)
            if message.author.name != "superai.ai" and message.channel.name != "spam-test":
                for bd in self.bads:
                    if bd in message.content.lower():
                        self.log(message.author.name + " hat eine Böse Nachricht geschrieben: " + message.content)
                        await message.delete()
                        await message.author.send("Ihre Nachricht '" + message.content + "' wurde entfernt! Wenn diese Nachricht nicht böse war, sage dass @superai.ai")

                for bd in self.timeouts.keys():
                    if bd in message.content.lower():
                        self.log(message.author.name + " hat eine Böse Timeout Nachricht geschrieben: " + message.content)
                        await message.delete()
                        timeout = timedelta(hours=self.timeouts[bd])
                        await message.author.timeout(timeout)
                        await message.author.send("Ihre Nachricht '" + message.content + "' wurde entfernt! Wenn diese Nachricht nicht timeoutig war, sage dass @superai.ai")
                    
    def log(self, msg, pri=True):
        f = open("log.txt", "a")
        f.write(msg+"/n")
        f.close()
        if pri:
            print(msg)


intents = discord.Intents.default()
intents.message_content = True
client = Lala(intents=intents)
token = open("token.txt", "r").read()
client.run(token)
