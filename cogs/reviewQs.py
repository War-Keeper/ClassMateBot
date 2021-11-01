# This functionality provides mechanism for instructors to post a random review question from the databse
from discord.ext import commands
import db

class ReviewQs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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
        # get random question from db
        rand = db.query(
            'SELECT question, answer FROM review_questions WHERE guild_id = %s ORDER BY RANDOM() LIMIT 1',
            (ctx.guild.id, )
        )

        # send question to guild
        for q, a in rand:
            await ctx.send(f"{q} \n ||{a}||")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: get_question_error(self, ctx, error)
    #    Description: prints error message for getQuestion command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @getQuestion.error
    async def get_question_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the getQuestion command, do: $getQuestion \n')
        else:
            await ctx.author.send(error)
        print(error)
        await ctx.message.delete()

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

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: add_question_error(self, ctx, error)
    #    Description: prints error message for addQuestion command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @addQuestion.error
    async def add_question_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the addQuestion command, do: $addQuestion \"Question\" \"Answer\" \n'
                '(For example: $addQuestion \"What class is this?\" "CSC510")')
        else:
            await ctx.author.send(error)
        print(error)
        await ctx.message.delete()

def setup(bot):
    n = ReviewQs(bot)
    bot.add_cog(n)
