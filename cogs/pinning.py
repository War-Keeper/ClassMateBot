# TODO privately pin a message based on copying a message link from a channel
# Copyright (c) 2021 War-Keeper
# This functionality lets the students pin the messages they want to.
# The bot personally pins the messages, i.e. the user can only see his pinned messages and not of others.
# The messages could be arranged on the basis of tags which the user can himself/herself give to the messages.
import os
import sys

from discord.ext import commands

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db


class Pinning(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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
    @commands.command(name="pin", help="Pin a message by adding a tagname (single word), link and a "
                                       "description(can be multi word). EX: $pin Homework Link Resources for HW2")
    async def addMessage(self, ctx, tagname: str, link: str, *, description: str):
        author = ctx.message.author

        db.query(
            'INSERT INTO pinned_messages (guild_id, author_id, tag, description, link) VALUES (%s, %s, %s, %s, %s)',
            (ctx.guild.id, author.id, tagname, description, link)
        )

        await ctx.send(
            "A new message has been pinned with tag: {} and link: {} with a description: {} by {}.".format(tagname,
                                                                                                           link,
                                                                                                           description,
                                                                                                           author))

    @addMessage.error
    async def addMessage_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the pin command, do: $pin TAGNAME LINK DESCRIPTION \n ( For example: '
                '$pin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 '
                'HW8 reminder )'
            )
        print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteMessage(self, ctx, tagname: str, *, description: str)
    #    Description: This command unpins the pinned messages with the provided tagname and description.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - tagname: the tag used to identify which pinned messages are to be deleted.
    #    - description: description of the pinned message used to uniquely identify a particular message.
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="unpin",
                      help="Unpin a message by passing the tagname and description of the pinned message")
    async def deleteMessage(self, ctx, tagname: str, *, description: str):
        author = ctx.message.author

        rows_deleted = db.query(
            'SELECT * FROM pinned_messages WHERE guild_id = %s AND tag = %s AND author_id = %s AND description = %s',
            (ctx.guild.id, tagname, author.id, description)
        )
        db.query(
            'DELETE FROM pinned_messages WHERE guild_id = %s AND tag = %s AND author_id = %s AND description = %s',
            (ctx.guild.id, tagname, author.id, description)
        )

        if len(rows_deleted) == 0:
            await ctx.send(
                f"No message found with the combination of tagname: {tagname}, "
                f"description {description} and author: {author}.")
        else:
            await ctx.send(
                f"{len(rows_deleted)} pinned message(s) has been deleted with tag: {tagname} "
                f"and description: {description}.")

    @deleteMessage.error
    async def deleteMessage_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the unpin command, do: $unpin TAGNAME DESCRIPTION \n ( For example: $unpin HW HW8 reminder )')
        print(error)

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
        messages = db.query(
            'SELECT tag, link, description FROM pinned_messages WHERE guild_id = %s AND author_id = %s AND tag = %s',
            (ctx.guild.id, author.id, tagname)
        )
        if len(messages) == 0:
            await ctx.send("No messages found with the given tagname and author combination")
        for tag, link, description in messages:
            await ctx.send(f"Tag: {tag}, Message Link: {link}, Description: {description}")


    @retrieveMessages.error
    async def retrieveMessages_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the pinnedmessages command, do: '
                '$pinnedmessages TAGNAME \n ( For example: $pinnedmessages HW )')
        print(error)

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
                      help="Update a previously pinned message by passing the tagname, "
                           "new link and old description in the same order")
    async def updatePinnedMessage(self, ctx, tagname: str, new_link: str, *, description: str):
        author = ctx.message.author
        rows_updated = db.query(
            'SELECT * FROM pinned_messages WHERE guild_id = %s AND tag = %s AND author_id = %s AND description = %s',
            (ctx.guild.id, tagname, author.id, description)
        )
        db.query(
            'UPDATE pinned_messages SET link = %s '
            'WHERE guild_id = %s AND tag = %s AND author_id = %s AND description = %s',
            (new_link, ctx.guild.id, tagname, author.id, description)
        )
        if len(rows_updated) == 0:
            await ctx.send("No message found with the given tagname, description and author combination")
        else:
            await ctx.send(
                f"A pinned message has been updated with tag: {tagname} and new link: {new_link} by: {author}.")

    @updatePinnedMessage.error
    async def updatePinnedMessage_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the updatepin command, do: $pin TAGNAME NEW_LINK DESCRIPTION \n ( $updatepin HW '
                'https://discordapp.com/channels/139565116151562240/139565116151562240/890814489480531969 '
                'HW8 reminder )')
        print(error)


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    n = Pinning(bot)
    bot.add_cog(n)
