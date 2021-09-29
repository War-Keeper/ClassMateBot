# TODO privately pin a message based on copying a message link from a channel
# This functionality lets the students pin the messages they want to.
# The bot personally pins the messages, i.e. the user can only see his pinned messages and not of others.
# The messages could be arranged on the basis of tags which the user can himself/herself give to the messages.
import discord
from discord.ext import commands
import json
import os


class Pinning(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.pinned_messages = json.load(open("data/PinMessage/PinnedMessages.json"))

    # Test command to check if the bot is working
    @commands.command()
    async def helpful3(self, ctx):
        await ctx.send(f"Pong! My ping currently is {round(self.bot.latency * 1000)}ms")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: addMessage(self, ctx, tagname: str, link: str, *, description: str)
    #    Description: Used to pin a message by the user. The message gets stored in a JSON file in the required format.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - tagname: a tag given by the user to their pinned message.
    #    - link: link of the pinned message.
    #    - description: description of the pinned message given by the user.
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="pin",
                      help="Pin a message by adding a tagname (single word), link and a description(can be multi word). EX: $pin Homework Link Resources for HW2")
    async def addMessage(self, ctx, tagname: str, link: str, *, description: str):
        author = ctx.message.author

        self.pinned_messages.append(
            {"ID": author.id, "TAG": tagname, "DESCRIPTION": description, "LINK": link})
        json.dump(self.pinned_messages, open("data/PinMessage/PinnedMessages.json", "w"))
        await ctx.send(
            "A new message has been pinned with tag: {} and link: {} with a description: {} by {}.".format(tagname,
                                                                                                           link,
                                                                                                           description,
                                                                                                           author))

    @addMessage.error
    async def addMessage_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the pin command, do: $pin TAGNAME LINK DESCRIPTION \n ( For example: $pin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 HW8 reminder )')

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteMessage(self, ctx, tagname: str, *, description: str)
    #    Description: This command unpins the pinned messages with the provided tagname and description.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - tagname: the tag used to identify which pinned messages are to be deleted.
    #    - description: description of the pinned message used to uniquely identify a particular message.
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="unpin", help="Unpin a message by passing the tagname and description of the pinned message")
    async def deleteMessage(self, ctx, tagname: str, *, description: str):
        author = ctx.message.author
        to_remove = []
        for pin_mes in self.pinned_messages:
            if ((pin_mes["TAG"] == tagname) and (pin_mes["ID"] == author.id) and (
                    pin_mes["DESCRIPTION"] == description)):
                to_remove.append(pin_mes)

        if (len(to_remove) == 0):
            await ctx.send(
                "No message found with the combination of tagname: {}, description {} and author: {}.".format(tagname,
                                                                                                              description,
                                                                                                              author))

        for pin_mes in to_remove:
            self.pinned_messages.remove(pin_mes)
        if to_remove:
            json.dump(self.pinned_messages, open("data/PinMessage/PinnedMessages.json", "w"))
            await ctx.send(
                "{} pinned message(s) has been deleted with tag: {} and description: {}.".format(len(to_remove),
                                                                                                 str(pin_mes["TAG"]),
                                                                                                 str(pin_mes[
                                                                                                         "DESCRIPTION"])))

    @deleteMessage.error
    async def deleteMessage_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the unpin command, do: $pin TAGNAME DESCRIPTION \n ( For example: $pin HW HW8 reminder )')

    # ----------------------------------------------------------------------------------
    #    Function: retrieveMessages(self, ctx, tagname: str)
    #    Description: This command is used to retrieve all the pinned messages under a
    #                 given tagname by a particular user.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - tagname: the tag used to identify which pinned messages are to be retrieved.
    # ----------------------------------------------------------------------------------
    @commands.command(name="pinnedmessages", help="Retrieve the pinned messages by passing the tagname")
    async def retrieveMessages(self, ctx, tagname: str):
        author = ctx.message.author
        for pin_mes in self.pinned_messages:
            if (pin_mes["ID"] == author.id and pin_mes["TAG"] == tagname):
                await ctx.send("Tag: {}, Message Link: {}, Description: {}".format(tagname, pin_mes["LINK"],
                                                                                   pin_mes["DESCRIPTION"]))
            else:
                await ctx.send("No messages found with the given tagname and author combination")

    @retrieveMessages.error
    async def retrieveMessages_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the pinnedmessages command, do: $pin TAGNAME \n ( For example: $pin HW )')

    # ----------------------------------------------------------------------------------------------------------
    #    Function: updatePinnedMessage(self, ctx, tagname: str, new_link: str, *, description: str)
    #    Description: This is used to update the link of a pinned message with a given tagname and description.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - tagname: a tag given by the user to their pinned message.
    #    - new_link: new link which is to added to the pinned message in place of the old link.
    #    - description: description of the pinned message given by the user.
    # ----------------------------------------------------------------------------------------------------------
    @commands.command(name="updatepin",
                      help="Update a previously pinned message by passing the tagname, new link and old description in the same order")
    async def updatePinnedMessage(self, ctx, tagname: str, new_link: str, *, description: str):
        author = ctx.message.author
        flag = False

        for pin_mes in self.pinned_messages:
            flag = False
            if ((pin_mes["TAG"] == tagname) and (pin_mes["ID"] == author.id) and (
                    pin_mes["DESCRIPTION"] == description)):
                pin_mes["LINK"] = new_link
                flag = True
                if (flag):
                    json.dump(self.pinned_messages, open("data/PinMessage/PinnedMessages.json", "w"))
                    await ctx.send(
                        "A pinned message has been updated with tag: {} and new link: {} by: {}.".format(tagname,
                                                                                                         new_link,
                                                                                                         author))
                else:
                    await ctx.send("No message found with the given tagname, description and author combination")

    @updatePinnedMessage.error
    async def updatePinnedMessage_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the updatepin command, do: $pin TAGNAME NEW_LINK DESCRIPTION \n ( $updatepin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890814489480531969 HW8 reminder )')


# -----------------------------------------
# Used to create a json file if none exist
# -----------------------------------------
def check_folders():
    if not os.path.exists("data/PinMessage"):
        print("Creating data/PinMessage folder...")
        os.makedirs("data/PinMessage")


# -----------------------------------------
# Used to create a json file if none exist
# -----------------------------------------
def check_files():
    f = "data/PinMessage/PinnedMessages.json"
    if not os.path.exists(f):
        print("Creating empty PinnedMessages.json...")
        json.dump([], open(f, "w"))


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    check_folders()
    check_files()
    n = Pinning(bot)
    bot.add_cog(n)
