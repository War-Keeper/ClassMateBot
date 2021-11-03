# Copyright (c) 2021 War-Keeper
"""This file contains serval methods to greet Hello"""

from discord.ext import commands


class Helpful(commands.Cog):
    """A basic "Hello World!" command, used to verify basic bot functionality"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='hello', help='The most basic Hello World! function')
    async def hello(self, ctx):
        """Function: hello(self, ctx)
        Description: prints "Hello World", used as a test function
        Inputs:
        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        -  Outputs: prints "Hello World!\""""
        await ctx.send("Hello World!")



def setup(bot):
    """add the file to the bot's cog system"""
    bot.add_cog(Helpful(bot))
