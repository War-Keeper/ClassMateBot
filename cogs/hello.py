from discord.ext import commands


# -----------------------------------------------------------------------
# A basic "Hello World!" command, used to verify basic bot functionality
# -----------------------------------------------------------------------
class Helpful(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # -----------------------------------------------------------------------------------
    #    Function: hello(self, ctx)
    #    Description: prints "Hello World", used as a test function
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: prints "Hello World!"
    # ----------------------------------------------------------------------------------
    @commands.command(name='hello', help='The most basic Hello World! function')
    async def hello(self, ctx):
        await ctx.send("Hello World!")


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    bot.add_cog(Helpful(bot))

# Copyright (c) 2021 War-Keeper
