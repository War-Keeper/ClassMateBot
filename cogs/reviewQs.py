# This functionality provides mechanism for instructors to post a random review question from the databse
from discord.ext import commands
import random

class Questions:
    ''' Class containing needed question/answer information and identification '''
    def __init__(self, num, qs, ans):
        self.number = num
        self.question = qs
        self.answer = ans

class ReviewQs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.q_dict = {}
        self.recent_q = []
        # add questions manually for initial implementation
        # TODO store questions in database
        self.q_dict[1] = Questions(1, "What are similarities between on-prem and cloud?",
                  "Most of the characteristics of software engineering stay the same, "
                  "development is “Mostly” location agnostic.")
        self.q_dict[2] = Questions(2, "What are reasons to pick on-prem over cloud?",
                                   "Security Reasons, Low Availability Needs, Local Network services")
        self.q_dict[3] = Questions(3, "What are reasons to pick cloud over on-prem?",
                                   "Global availability needs, Growth of user base prediction")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: getQuestion(self, ctx)
    #    Description: prints a random question from the database
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       - a random question from the database (in user guild) is sent by the bot
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name='getQuestion', help='Get a review question. EX: $getQuestion')
    async def getQuestion(self, ctx):

        # check if all quesitons have been asked and reset recents
        if len(self.recent_q) == len(self.q_dict):
            self.recent_q.clear()
        # get a random question number from available numbers
        rand = random.choice(list(self.q_dict.keys()))
        # check if the question has been asked
        while rand in self.recent_q:
            rand = random.choice(list(self.q_dict.keys()))
        self.recent_q.append(rand)
        question = self.q_dict[rand].question + '\n' + '||' + self.q_dict[rand].answer + '||'

        await ctx.send(question)


def setup(bot):
    n = ReviewQs(bot)
    bot.add_cog(n)
