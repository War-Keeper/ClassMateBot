# Copyright (c) 2021 War-Keeper

import csv
import discord
from discord.ext import commands
import os
import flair
from threading import Event
# -----------------------------------------------------------
# This File contains commands for sentiment analysis,
# displays the sentiment of the message sent.
# -----------------------------------------------------------
class Sentiment(commands.Cog):

# -----------
# initialize
# -----------
    def __init__(self, bot):
        self.bot = bot
        self.mess = ""



    @commands.Cog.listener()
    async def on_message(self, message):
        self.mess = message.content

# -------------------------------------------------------------------------------------------------------------
    #    Function: sentiment(self, ctx)
    #    Description: Analyses the sentiment of the message when the command $sentiment is given.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: The bot replies with the sentiment of the given message.
    #             If the message is empty, it replies with a "Please enter your message".
    # --------------------------------------------------------------------------------------------------------------

    @commands.command(name='sentiment',
                      help='Used for sentiment analysis, \
    To use the sentiment command, do: $sentiment \n \
    (For example: sentiment)', pass_context=True)
    async def sentiment(self, ctx):
        try:
            flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
            message = self.mess

            if message == "" or message == null:
                await ctx.send("Please enter your message")
            else:
                print(message)
                s = flair.data.Sentence(message)
                flair_sentiment.predict(s)
                sentiment = s.labels
                print(sentiment)
                await ctx.send(sentiment)

        except:
            print("an exception has occurred")





    # -----------------------------------------------------------
    # add the file to the bot's cog system
    # -----------------------------------------------------------
def setup(bot):
    bot.add_cog(Sentiment(bot))






