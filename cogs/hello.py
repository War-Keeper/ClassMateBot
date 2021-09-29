from discord.ext import commands

# -----------------------------------------------------------------------
# A basic "Hello World!" command, used to verify basic bot functionality
# -----------------------------------------------------------------------
class Helpful(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # ------------------------------------------------
    # Greetings command, responds with "Hello World!"
    # ------------------------------------------------
    @commands.command(name='hello', help='The most basic Hello World! function')
    async def hello(self, ctx):
        await ctx.send("Hello World!")

# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    bot.add_cog(Helpful(bot))
