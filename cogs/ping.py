import discord
from discord.ext import commands


# ----------------------------------------------------------------------------------------------
# Returns the ping of the bot, useful for testing bot lag and as a simple functionality command
# ----------------------------------------------------------------------------------------------
class Helpful(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # -------------------------------------------------
    # Ping command, prints the current ping of the bot
    # -------------------------------------------------
    @commands.command()
    async def ping(self, ctx):
        # We set an upper bound on the ping of the bot to prevent float_infinity situations which crash testing
        await ctx.send(f"Pong! My ping currently is {round(min(999999999, self.bot.latency * 1000))}ms")


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    bot.add_cog(Helpful(bot))
