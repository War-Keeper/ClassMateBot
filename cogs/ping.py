import discord
from discord.ext import commands

class Helpful(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! My ping currently is {round(min(999999999 , self.bot.latency * 1000))}ms")

def setup(bot):
    bot.add_cog(Helpful(bot))
