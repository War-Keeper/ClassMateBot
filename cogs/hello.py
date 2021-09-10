from discord.ext import commands


class Helpful(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', help='The most basic Hello World! function')
    async def hello(self, ctx):
        await ctx.send("Hello World!")


def setup(bot):
    bot.add_cog(Helpful(bot))
