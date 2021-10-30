import json
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
    @commands.has_permissions(administrator=True)
    async def grades(self, ctx, chart: str, aGrade: int, bGrade: int, cGrade: int, dGrade: int, fGrade: int):
        with open('data/charts/chartstorage.json', 'r') as f:
            storage = json.load(f)
        global adminId
        adminId = ctx.author.id
        qc = QuickChart()
        qc.width = 500
        qc.height = 300
        qc.device_pixel_ratio = 2.0
        qc.config = {
            "type": "{}".format(chart),
            "data": {
                "labels": ["A", "B", "C", "D", "F"],
                "datasets": [{
                    "backgroundColor": ['rgb(128, 177, 229)',
                                        'rgb(116, 232, 219)',
                                        'rgb(246, 220, 154)',
                                        'rgb(250, 195, 149)',
                                        'rgb(245, 165, 145)'],
                    "label": "grades",
                    "data": [aGrade, bGrade, cGrade, dGrade, fGrade]
                }]
            }
        }
        link = qc.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)
        await self.update_chart(storage, ctx.author, shortened_link)
        with open('data/charts/chartstorage.json', 'w') as f:
            json.dump(storage, f, indent=4)
        await ctx.send(f"{shortened_link}")

    async def update_chart(self, storage, admin, link):
        if not str(admin.id) in storage:
            storage[str(admin.id)] = {}
        storage[str(admin.id)]['URL'] = link

    @grades.error
    async def grades_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: $grades chart_type (pie, bar, line), title (1 word), "
                "number of As, number of Bs, number of Cs, number of Ds, number of Fs \n"
                "\n EXAMPLE: $grades bar 5 4 3 2 1")

    @commands.command()
    async def checkgrade(self, ctx):
        with open('data/charts/chartstorage.json', 'r') as f:
            storage = json.load(f)
            if not storage:
                await ctx.send(f"No grades posted!")
            else:
                await ctx.send(f" View grade distribution: {storage[str(adminId)]['URL']}")

    @commands.command(name="customchart",
                      help="View grade distribution; FORMAT (many): chart_type (pie, bar, line), title (1 word),"
                           "list data as coordinates: (a,1), (b,2), (c,3)")
    @commands.has_permissions(administrator=True)
    async def customchart(self, ctx, chart: str, title: str, datacount: int, *args):

        if len(args) / 2 != datacount:
            raise IllegalArgumentsError

        labelslist = []
        datasetlist = []

        for x in range(datacount):
            labelslist.append(args[x])
            print(args[x])

        for x in range(datacount, len(args)):
            datasetlist.append(args[x])
            print(args[x])

        qc = QuickChart()
        qc.width = 500
        qc.height = 300
        qc.device_pixel_ratio = 2.0
        qc.config = {
            "type": "{}".format(chart),
            "data": {
                "labels": labelslist,
                "datasets": [{
                    "label": "{}".format(title),
                    "data": datasetlist
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

class IllegalArgumentsError(Exception):
    print("customchart arguments invalid")
    pass