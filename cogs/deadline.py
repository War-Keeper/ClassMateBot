# TODO deadline reminder for all students

import discord
from discord.ext import commands
import time
import os
import json

class Helper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reminders = json.load(open("data/remindme/reminders.json"))
        self.units = {"second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800, "month": 2592000}

    @commands.command()
    async def helpful1(self, ctx):
        await ctx.send(f"Pong! My ping currently is {round(self.bot.latency * 1000)}ms")

    @commands.command(name="remindme", pass_context=True, help="Request the bot to set a reminder for a due date")
    async def remindme(self, ctx, quantity: int, time_unit : str,*, text :str):

        time_unit = time_unit.lower()
        author = ctx.message.author
        s = ""
        if time_unit.endswith("s"):
            time_unit = time_unit[:-1]
            s = "s"
        if not time_unit in self.units:
            await ctx.send("Invalid unit of time. Select from seconds/minutes/hours/days/weeks/months")
            return
        if quantity < 1:
            await ctx.send("Quantity must not be 0 or negative")
            return
        if len(text) > 1960:
            await ctx.send("Text is too long.")
            return

        seconds = self.units[time_unit] * quantity
        future = int(time.time()+seconds)

        self.reminders.append({"ID": author.id, "FUTURE": future, "TEXT": text})
        await ctx.send("I will remind you that in {} {}.".format(str(quantity), time_unit + s))
        json.dump(self.reminders, open("data/remindme/reminders.json", "w"))


def check_folders():
    if not os.path.exists("data/remindme"):
        print("Creating data/remindme folder...")
        os.makedirs("data/remindme")

def check_files():
    f = "data/remindme/reminders.json"
    print("Creating file...")
    if not os.path.exists(f):
        print("Creating empty reminders.json...")
        json.dump([], open(f, "w"))

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Helper(bot))

