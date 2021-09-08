# TODO privately pin a message based on copying a message link from a channel

import discord
from discord.ext import commands

class Helper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def helpful3(self, ctx):
        await ctx.send(f"Pong! My ping currently is {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Helper(bot))

