# TODO privately pin a message based on copying a message link from a channel

import discord
from discord.ext import commands
import json
import os


class Pinning(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.pinned_messages = json.load(open("data/PinMessage/PinnedMessages.json"))

    @commands.command()
    async def helpful3(self, ctx):
        await ctx.send(f"Pong! My ping currently is {round(self.bot.latency * 1000)}ms")

    @commands.command(name="pin")
    async def addMessage(self, ctx, tagname: str, link: str, *, description: str):
        author = ctx.message.author

        self.pinned_messages.append(
            {"ID": author.id, "TAG": tagname, "DESCRIPTION": description, "LINK": link})
        json.dump(self.pinned_messages, open("data/PinMessage/PinnedMessages.json", "w"))
        await ctx.send("A new message has been pinned with tag: {} and link: {} with a description: {} by {}.".format(tagname, link, description, author))

    @commands.command(name="unpin")
    async def deleteMessage(self, ctx, tagname: str):
        author = ctx.message.author
        to_remove = []
        for pin_mes in self.pinned_messages:
            if ((pin_mes["TAG"] == tagname) and (pin_mes["ID"] == author.id)):
                to_remove.append(pin_mes)

        if(len(to_remove) == 0):
            await ctx.send("No message found with the combination of tagname: {} and author: {}.".format(tagname,
                                                                                                author))

        for pin_mes in to_remove:
            self.pinned_messages.remove(pin_mes)
        if to_remove:
            json.dump(self.pinned_messages, open("data/PinMessage/PinnedMessages.json", "w"))
            await ctx.send("{} pinned message(s) has been deleted with tag: {}".format(len(to_remove), str(pin_mes["TAG"])))

    @commands.command(name="pinnedmessages")
    async def retrieveMessages(self, ctx, tagname: str):
        author = ctx.message.author
        for pin_mes in self.pinned_messages:
            if(pin_mes["ID"] == author.id):
                await ctx.send("Tag: {}, Message Link: {}, Description: {}".format(tagname, pin_mes["LINK"], pin_mes["DESCRIPTION"]))


    @commands.command(name="updatepin", pass_context=True)
    async def updatePinnedMessage(self, ctx, tagname: str, new_link: str, *, description: str):
        author = ctx.message.author
        flag = False

        for pin_mes in self.pinned_messages:
            flag = False
            if ((pin_mes["TAG"] == tagname) and (pin_mes["ID"] == author.id) and (pin_mes["DESCRIPTION"] == description)):
                pin_mes["LINK"] = new_link
                flag = True
                if (flag):
                    json.dump(self.pinned_messages, open("data/PinMessage/PinnedMessages.json", "w"))
                    await ctx.send("A pinned message has been updated with tag: {} and new link: {} by: {}.".format(tagname, new_link, author))


def check_folders():
    if not os.path.exists("data/PinMessage"):
        print("Creating data/PinMessage folder...")
        os.makedirs("data/PinMessage")


def check_files():
    f = "data/PinMessage/PinnedMessages.json"
    # print("Creating file...")
    if not os.path.exists(f):
        print("Creating empty PinnedMessages.json...")
        json.dump([], open(f, "w"))


def setup(bot):
    check_folders()
    check_files()
    n = Pinning(bot)
    bot.add_cog(n)