# TODO deadline reminder for all students
# Copyright (c) 2021 War-Keeper
# This functionality provides various methods to manage reminders (in the form of creation, retrieval, updation and deletion)
# A user can set up a reminder, check what is due this week or what is due today. He/She can also check all the due homeworks based on hte coursename.
# A user can also update or delete a reminder if needed.
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
        self.units = {"second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800, "month": 2592000}

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: duedate(self, ctx, coursename: str, hwcount: str, *, date: str)
    #    Description: Adds the homework to json in the specified format
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - coursename: name of the course for which homework is to be added
    #    - hwcount: name of the homework
    #    - date: due date of the assignment
    #    Outputs: returns either an error stating a reason for failure or returns a success message
    #          indicating that the reminder has been added
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="addhw",
                      help="add homework and due-date $addhw CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) ex. $addhw CSC510 HW2 SEP 25 2024 17:02")
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
        existing = db.query(
            'SELECT author_id FROM reminders WHERE guild_id = %s AND course = %s AND homework = %s',
            (ctx.guild.id, coursename, hwcount)
        )
        if not existing:
            db.query(
                'INSERT INTO reminders (guild_id, author_id, course, homework, due_date, future) VALUES (%s, %s, %s, %s, %s)',
                (ctx.guild.id, author.id, coursename, hwcount, duedate, seconds)
            )
            await ctx.send(
                f"A date has been added for: {coursename} homework named: {hwcount} which is due on: {duedate} by {author}.")
        else:
            await ctx.send("This homework has already been added..!!")

    @duedate.error
    async def duedate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the addhw command, do: $addhw CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) \n ( For example: $addhw CSC510 HW2 SEP 25 2024 17:02 )')

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteReminder(self, ctx, courseName: str, hwName: str)
    #    Description: Delete a reminder using Classname and Homework name
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - coursename: name of the course for which homework is to be added
    #    - hwName: name of the homework
    #    Outputs: returns either an error stating a reason for failure or
    #          returns a success message indicating that the reminder has been deleted
    # -----------------------------------------------------------------------------------------------------------------

    @commands.command(name="deletereminder", pass_context=True,
                      help="delete a specific reminder using course name and homework name using $deletereminder CLASSNAME HW_NAME ex. $deletereminder CSC510 HW2 ")
    async def deleteReminder(self, ctx, courseName: str, hwName: str):
        author = ctx.message.author
        reminders_deleted = db.query(
            'DELETE FROM reminders WHERE guild_id = %s AND homework = %s AND course = %s',
            (ctx.guild.id, hwName, courseName)
        )

        for reminder in reminders_deleted:
            _, course, homework, due_date = reminder
            await ctx.send(f"Following reminder has been deleted: Course: {course}, Homework Name: {homework}, Due Date: {due_date}")

    @deleteReminder.error
    async def deleteReminder_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the deletereminder command, do: $deletereminder CLASSNAME HW_NAME \n ( For example: $deletereminder CSC510 HW2 )')

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: changeduedate(self, ctx, classid: str, hwid: str, *, date: str)
    #    Description: Update the 'Due date' for a homework by providing the classname and homewwork name
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - classid: name of the course for which homework is to be added
    #    - hwid: name of the homework
    #    - date: due date of the assignment
    #    Outputs: returns either an error stating a reason for failure or
    #          returns a success message indicating that the reminder has been updated
    # -----------------------------------------------------------------------------------------------------------------

    @commands.command(name="changeduedate", pass_context=True,
                      help="update the assignment date. $changeduedate CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) ex. $changeduedate CSC510 HW2 SEP 25 2024 17:02 ")
    async def changeduedate(self, ctx, classid: str, hwid: str, *, date: str):
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

        future = (time.time() + (duedate - datetime.today()).total_seconds())
        updated_reminders = db.query(
            'UPDATE reminders SET author_id = %s, due_date = %s, future = %s WHERE guild_id = %s AND homework = %s AND course = %s',
            (author.id, duedate, future, ctx.guild.id, hwid, classid)
        )
        for reminder in updated_reminders:
            *_, due_date, _ = reminder
            await ctx.send(
                f"{classid} {hwid} has been updated with following date: {due_date}")

    @changeduedate.error
    async def changeduedate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the changeduedate command, do: $changeduedate CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) \n ( For example: $changeduedate CSC510 HW2 SEP 25 2024 17:02 )')

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: duethisweek(self, ctx)
    #    Description: Displays all the homeworks that are due this week along with the coursename and due date
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: returns either an error stating a reason for failure
    #             or returns a list of all the assignments that are due this week
    # -----------------------------------------------------------------------------------------------------------------

    @commands.command(name="duethisweek", pass_context=True,
                      help="check all the homeworks that are due this week $duethisweek")
    async def duethisweek(self, ctx):
        time = ctx.message.created_at
        # TODO come back to this one





        #






        db.query(
            'SELECT course, homework, due_date FROM reminders WHERE guild_id = %s AND due_date - %s <= 7',
            (ctx.guild.id, time)
        )
        for reminder in self.reminders:
            timeleft = datetime.strptime(reminder["DUEDATE"], '%Y-%m-%d %H:%M:%S') - time
            print("timeleft: " + str(timeleft) + " days left: " + str(timeleft.days))
            if timeleft.days <= 7:
                await ctx.send("{} {} is due this week at {}".format(reminder["COURSE"], reminder["HOMEWORK"],
                                                                     reminder["DUEDATE"]))

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: duetoday(self, ctx)
    #    Description: Displays all the homeworks that are due today
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    # Outputs: returns either an error stating a reason for failure or
    #          returns a list of all the assignments that are due on the day the command is run
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="duetoday", pass_context=True, help="check all the homeworks that are due today $duetoday")
    async def duetoday(self, ctx):
        flag = True
        for reminder in self.reminders:
            timedate = datetime.strptime(reminder["DUEDATE"], '%Y-%m-%d %H:%M:%S')
            if timedate.date() == ctx.message.created_at.date():
                flag = False
                await ctx.send(
                    "{} {} is due today at {}".format(reminder["COURSE"], reminder["HOMEWORK"], timedate.time()))
        if (flag):
            await ctx.send("You have no dues today..!!")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: coursedue(self, ctx, courseid: str)
    #    Description: Displays all the homeworks that are due for a specific course
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - courseid: name of the course for which homework is to be added
    #    Outputs: returns either an error stating a reason for failure or
    #          a list of assignments that are due for the provided courseid
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="coursedue", pass_context=True,
                      help="check all the homeworks that are due for a specific course $coursedue coursename ex. $coursedue CSC505")
    async def coursedue(self, ctx, courseid: str):
        course_due = []
        for reminder in self.reminders:
            if reminder["COURSE"] == courseid:
                course_due.append(reminder)
                await  ctx.send("{} is due at {}".format(reminder["HOMEWORK"], reminder["DUEDATE"]))
        if not course_due:
            await ctx.send("Rejoice..!! You have no pending homeworks for {}..!!".format(courseid))

    @coursedue.error
    async def coursedue_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the coursedue command, do: $coursedue CLASSNAME \n ( For example: $coursedue CSC510 )')

    # ---------------------------------------------------------------------------------
    #    Function: listreminders(self, ctx)
    #    Description: Print out all the reminders
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: returns either an error stating a reason for failure or
    #             returns a list of all the assignments
    # ---------------------------------------------------------------------------------
    @commands.command(name="listreminders", pass_context=True, help="lists all reminders")
    async def listreminders(self, ctx):
        reminders = db.query('SELECT author_id, course, homework, due_date FROM reminders WHERE guild_id = %s', (ctx.guild.id,))
        for author_id, course, homework, due_date in reminders:
            await ctx.send(f"{course} homework named: {homework} which is due on: {due_date} by {author_id}")
        if not reminders:
            await ctx.send("Mission Accomplished..!! You don't have any more dues..!!")

    # ---------------------------------------------------------------------------------
    #    Function: clearallreminders(self, ctx)
    #    Description: Delete all the reminders
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: returns either an error stating a reason for failure or
    #             returns a success message stating that reminders have been deleted
    # ---------------------------------------------------------------------------------

    @commands.command(name="clearreminders", pass_context=True, help="deletes all reminders")
    async def clearallreminders(self, ctx):
        db.query('DELETE FROM reminders WHERE guild_id = %s', (ctx.guild.id,))
        await ctx.send("All reminders have been cleared..!!")

    # ---------------------------------------------------------------------------------
    #    Function: remindme(self, ctx, quantity: int, time_unit : str,*, text :str)
    #    Description: Personal remind me functionality
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - quantity - time after which the data will be erased
    #    Outputs: returns either an error stating a reason for failure or
    #             returns a success message stating that reminders have been deleted
    # ---------------------------------------------------------------------------------

    @commands.command(name="remindme", pass_context=True, help="Request the bot to set a reminder for a due date")
    async def remindme(self, ctx, quantity: int, time_unit: str, *, text: str):

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
        future = int(time.time() + seconds)
        # TODO set timestamp compatible with db

        db.query(
            'INSERT INTO reminders (guild_id, author_id, future, text) VALUES (%s, %s, %s)',
            (ctx.guild.id, author.id, future, text)
        )

        await ctx.send("I will remind you that in {} {}.".format(str(quantity), time_unit + s))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send('Unidentified command..please use $help to get the list of available comamnds')

    # -----------------------------------------------------------------------------------------------------
    #    Function: delete_old_reminders(self)
    #    Description: asynchronously keeps on tracking the json file for expired reminders and cleans them.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    # -----------------------------------------------------------------------------------------------------
    async def delete_old_reminders(self):
        print("inside delete old reminders")
        while self is self.bot.get_cog("Deadline"):
            db.query('DELETE FROM reminders WHERE now() >= future')
            await asyncio.sleep(5)


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    n = Deadline(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(n.delete_old_reminders())
    bot.add_cog(n)
