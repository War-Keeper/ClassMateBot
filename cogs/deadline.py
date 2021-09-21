# TODO deadline reminder for all students

import discord
from discord.ext import commands
import json
import os
import asyncio
import time
from datetime import datetime

class Deadline(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reminders = json.load(open("data/remindme/reminders.json"))
        self.units = {"second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800, "month": 2592000}

    @commands.command()
    async def helpful1(self, ctx):
        await ctx.send(f"Pong! My ping currently is {round(self.bot.latency * 1000)}ms")

    @commands.command(name="addhw")
    async def duedate(self, ctx, coursename: str, hwcount: str, *, date: str):
        author = ctx.message.author
        # print('Author: '+str(author)+' coursename: '+coursename+' homework count: '+hwcount+' date: '+str(date))
        try:
            duedate = datetime.strptime(date, '%b %d %Y %H:%M')
            # print(seconds)
        except ValueError:
            try:
                duedate = datetime.strptime(date, '%b %d %Y')
            except:
                await ctx.send("Due date could not be parsed")
                return
        a_timedelta = duedate - datetime.today()
        seconds = (time.time() + a_timedelta.total_seconds())
        self.reminders.append(
            {"ID": author.id, "COURSE": coursename, "HOMEWORK": hwcount, "DUEDATE": str(duedate), "FUTURE": seconds})
        json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
        await ctx.send("A date has been added for: {} homework named: {} which is due on: {} by {}.".format(coursename, hwcount,str(duedate), author))

    @commands.command(pass_context=True)
    async def deleteReminder(self, ctx, courseName: str, hwName: str):
        author = ctx.message.author
        to_remove = []
        for reminder in self.reminders:
            # print('in json '+str(reminder["HOMEWORK"])+' hwName '+hwName)
            if ((reminder["HOMEWORK"] == hwName) and (reminder["COURSE"] == courseName)):
                # print('true '+hwName)
                to_remove.append(reminder)
                # print('to_remove '+ str(to_remove))
        for reminder in to_remove:
            self.reminders.remove(reminder)
        if to_remove:
            json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
            await ctx.send("Following reminder has been deleted: Course: {}, Homework Name: {}, Due Date: {}".format(str(reminder["COURSE"]), str(reminder["HOMEWORK"]), str(reminder["DUEDATE"])))

    @commands.command(name="changeduedate", pass_context=True)
    async def change_due_date(self, ctx, classid: str, hwid: str, *, date: str):
        author = ctx.message.author
        flag = False
        try:
            duedate = datetime.strptime(date, '%b %d %Y %H:%M')
        except ValueError:
            try:
                duedate = datetime.strptime(date, '%b %d %Y')
            except:
                await ctx.send("Due date could not be parsed")
                return
        for reminder in self.reminders:
            flag = False
            if ((reminder["HOMEWORK"] == hwid) and (reminder["COURSE"] == classid)):
                reminder["DUEDATE"] = str(duedate)
                a_timedelta = duedate - datetime.today()
                seconds = (time.time() + a_timedelta.total_seconds())
                reminder["FUTURE"] = seconds
                reminder["ID"] = author.id
                flag = True
                if (flag):
                    json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
                    await ctx.send("{} {} has been updated with following date: {} by {}".format(classid, hwid,reminder["DUEDATE"],self.bot.user(reminder["ID"])))

    @commands.command(name="duethisweek", pass_context=True)
    async def duethisweek(self, ctx):
        time = ctx.message.created_at
        for reminder in self.reminders:
            timeleft = datetime.strptime(reminder["DUEDATE"], '%Y-%m-%d %H:%M:%S') - time
            print("timeleft: " + str(timeleft) + " days left: " + str(timeleft.days))
            if timeleft.days <= 7:
                await ctx.send("{} {} is due this week at {}".format(reminder["COURSE"], reminder["HOMEWORK"], reminder["DUEDATE"]))

    @commands.command(name="duetoday", pass_context=True)
    async def duetoday(self, ctx):
        for reminder in self.reminders:
            timedate = datetime.strptime(reminder["DUEDATE"], '%Y-%m-%d %H:%M:%S')
            if timedate.date() == ctx.message.created_at.date():
                await ctx.send("{} {} is due today at {}".format(reminder["COURSE"], reminder["HOMEWORK"], timedate.time()))

    @commands.command(name="coursedue", pass_context=True)
    async def coursedue(self, ctx, courseid: str):
        course_due = []
        for reminder in self.reminders:
            if reminder["COURSE"] == courseid:
                course_due.append(reminder)
                await  ctx.send("{} is due at {}".format(reminder["HOMEWORK"], reminder["DUEDATE"]))
        if not course_due:
            await ctx.send("Rejoice..!! You have no pending homeworks for {}..!!".format(courseid))

    @commands.command(name="listreminders", pass_context=True, help="lists all reminders")
    async def listreminders(self, ctx):
        to_remove = []
        for reminder in self.reminders:
            # if reminder["FUTURE"] <= int(time.time()):
            try:
                # await ctx.send("{} homework named: {} which is due on: {} by {}".format(self.bot.get_user(reminder["ID"]), reminder["TEXT"]))
                await ctx.send("{} homework named: {} which is due on: {} by {}".format(reminder["COURSE"], reminder["HOMEWORK"],reminder["DUEDATE"],self.bot.get_user(reminder["ID"])))
            except (discord.errors.Forbidden, discord.errors.NotFound):
                to_remove.append(reminder)
            except discord.errors.HTTPException:
                pass
            else:
                to_remove.append(reminder)

    @commands.command(name="clearreminders", pass_context=True, help="deletes all reminders")
    async def clearallreminders(self, ctx):
        to_remove = []
        for reminder in self.reminders:
            to_remove.append(reminder)
        for reminder in to_remove:
            self.reminders.remove(reminder)
        if to_remove:
            json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
            await ctx.send("All reminders have been cleared..!!")

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

    async def delete_old_reminders(self):
        print("inside delete old reminders")
        #print(self.bot.get_cog("Deadline"))
        while self is self.bot.get_cog("Deadline"):
            to_remove = []
            for reminder in self.reminders:
                if reminder["FUTURE"] <= int(time.time()):
                    try:
                        print("Deleting an old reminder..!!")
                    except (discord.errors.Forbidden, discord.errors.NotFound):
                        to_remove.append(reminder)
                    except discord.errors.HTTPException:
                        pass
                    else:
                        to_remove.append(reminder)
            for reminder in to_remove:
                self.reminders.remove(reminder)
            if to_remove:
                json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
            await asyncio.sleep(5)


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
    n = Deadline(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(n.delete_old_reminders())
    bot.add_cog(n)

