import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Helper(bot))

class Helper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f"Pong! My ping currently is {round(self.bot.latency * 1000)}ms")


