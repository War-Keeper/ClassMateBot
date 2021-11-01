# Copyright (c) 2021 War-Keeper
from discord.ext import commands


# ----------------------------------------------------------------------------------------------
# Returns the ping of the bot, useful for testing bot lag and as a simple functionality command
# ----------------------------------------------------------------------------------------------
class Helpful(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # -------------------------------------------------------------------------------------------------------
    #    Function: ping(self, ctx)
    #    Description: prints the current ping of the bot, used as a test function
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: prints the current ping of the bot, with an upper bound of 999999999 to avoid float errors
    # -------------------------------------------------------------------------------------------------------
    @commands.command()
    async def ping(self, ctx):
        # We set an upper bound on the ping of the bot to prevent float_infinity situations which crash testing
        await ctx.send(f"Pong! My ping currently is {round(min(999999999, self.bot.latency * 1000))}ms")


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    bot.add_cog(Helpful(bot))
