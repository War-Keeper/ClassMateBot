# Copyright (c) 2021 War-Keeper

import csv
import discord
from discord.ext import commands
import os
import re


# -----------------------------------------------------------
# This File contains commands for Saving the links in a file,
# Display all the messages which contains links.
# -----------------------------------------------------------
class links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        url=[]
        message_links = []
        temp=[]
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, message.content)
        test= re.findall(regex, message.content) is not None
        for x in url:
            temp.append(x[0])
        if temp:
            message_links.append(message.content)
            with open('.\data\links\links.txt', "a") as f:
                f.write("Message containing Link :-  " + message.content + "\n")
                f.close()
        else:
            pass


    @commands.command()
    async def send_links(self, ctx):
        await ctx.send(file=discord.File('.\data\links\links.txt'))

# -----------------------------------------------------------
# add the file to the bot's cog system
# -----------------------------------------------------------
def setup(bot):
    bot.add_cog(links(bot))


