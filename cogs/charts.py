import discord
from discord.ext import commands
from quickchart import QuickChart
import pyshorteners


class Charts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="grades",
                      help="View grade distribution; FORMAT (7 inputs): chart_type (pie, bar, line), title (1 word),"
                           "number of As, number of Bs, number of Cs, number of Ds, number of Fs")
    async def grades(self, ctx, chart: str):
        qc = QuickChart()
        qc.width = 500
        qc.height = 300
        qc.device_pixel_ratio = 2.0
        qc.config = {
            "type": "{}".format(chart),
            "data": {
                "labels": ["A", "B", "C", "D", "F"],
                "datasets": [{
                    "label": "grades",
                    "data": [1, 2, 3, 4, 5]
                }]
            }
        }

        link = qc.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)
        await ctx.send(f"{shortened_link}")

# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    bot.add_cog(Charts(bot))
