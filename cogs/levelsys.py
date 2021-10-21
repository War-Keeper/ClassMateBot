import discord
from discord.ext import commands
from pymongo import MongoClient

bot_channel = 900823126714220604
talk_channels = [900580609540362303, 900840273192558692]

level = ["beginner",
         "student",
         "Helpful",
         "teacher's pet",
         "Github Navigator",
         "Code Hero",
         "TA's Right Hand",
         "Professor's Right Hand",
         "Legend"]

levelnum = [3, 5, 10, 20, 30, 40, 50, 60, 70]

cluster = MongoClient("mongodb+srv://niraj:<lavani12341>@clustern.vxbvi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

levelling = cluster["discord"]["levelling"]

class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    # ----------------------------------
    #    Function: leaderboard(self, ctx)
    #    Description: Checks for messages and adds score to user
    #    Inputs:
    #    - ctx: used to access the values passed through the current context
    #    Outputs:
    # ----------------------------------
    @commands.Cog.listener()
    async def on_message(self, message):
        print("message found")
        if message.channel.id in talk_channels:
            stats = levelling.find_one({"id" : message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id" : message.author.id, "xp" : 100}
                    levelling.insert_one(newuser)
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id": message.author.id}, {"$set": {"xp": xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2)) + (50*(lvl-1))):
                            break
                        lvl += 1
                    xp -= ((50*(lvl-1**2)) + (50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send(f"well done {message.author.mention}! You levelled up to **level: {lvl}**!")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(description=f"{message.author.mention} you have gotten role **{level[i]}**!")
                                embed.set_thumbnail(url=message.author.avatar_url)
                                await message.channel.send(embed=embed)

    # ----------------------------------
    #    Function: rank(self, ctx)
    #    Description: Command for users to check their rank
    #    Inputs:
    #    - ctx: used to access the values passed through the current context
    #    Outputs:
    # ----------------------------------
    @commands.command(name='rank', help='To use the join command, do: $rank \n \
    ( For example: $rank)', pass_context=True)
    async def rank(self, ctx):

        if ctx.channel.id == bot_channel:
            print("rank called in bot channel")
            stats = levelling.find_one({"id" : ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="No messages, no rank!")
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < ((50 * (lvl ** 2)) + (50 * (lvl - 1))):
                        break
                    lvl += 1
                xp -= ((50 * (lvl - 1 ** 2)) + (50 * (lvl - 1)))
                boxes = int((xp / (200 * ((1/2) * lvl))) * 20)
                rankings = levelling.find().sort("xp", -1)
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                embed = discord.Embed(title="{}'s level stats".format(ctx.author.name))
                embed.add_field(name="Name", value=ctx.author.mention, inline=True)
                embed.add_field(name="XP", value=f"{xp}/{int(200 * ((1/2) * lvl))}", inline=True)
                embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                embed.add_field(name="Progress Bar [lvl]", value=boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline=False)
                embed.set_thumbnail(url=ctx.author.avatar_url)

                await ctx.channel.send(embed=embed)

    # ----------------------------------
    #    Function: leaderboard(self, ctx)
    #    Description: Command for users to see highest ranks in server
    #    Inputs:
    #    - ctx: used to access the values passed through the current context
    #    Outputs:
    # ----------------------------------
    @commands.command()
    async def leaderboard(self, ctx):
        if ctx.channel.id == bot_channel:
            rankings = levelling.find().sort("xp", -1)
            i = 1
            embed = discord.Embed(title="Rankings: ")
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            await ctx.channel.send(embed=embed)

# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    bot.add_cog(levelsys(bot))
