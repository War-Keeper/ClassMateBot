# This functionality provides mechanism for instructors to post a random review question from the databse
from discord.ext import commands
import random
import db

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
        rand = db.query(
            'SELECT question, answer FROM review_questions WHERE guild_id = %s ORDER BY RANDOM() LIMIT 1',
            (ctx.guild.id, )
        )
        for q, a in rand:
            await ctx.send(f"{q} \n ||{a}||")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: addQuestion(self, ctx, qs, ans)
    #    Description: allow instructors to add review question
    #    Inputs:
    #       - ctx: context of the command
    #       - qs: review question to add
    #       - ans: answer to review question
    #    Outputs:
    #       - success message
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role('Instructor')
    @commands.command(name='addQuestion', help='Add a review question. '
                                               'EX: $addQuestion \"What class is this?\" \"Software Engineering\"')
    async def addQuestion(self, ctx, qs: str, ans: str):
        # add question to database
        db.query(
            'INSERT INTO review_questions (guild_id, question, answer) VALUES (%s, %s, %s)',
            (ctx.guild.id, qs, ans)
        )

        await ctx.send(
            "A new review question has been added! Question: {} and Answer: {}.".format(qs, ans))


def setup(bot):
    n = ReviewQs(bot)
    bot.add_cog(n)
