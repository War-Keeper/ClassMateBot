# This functionality provides mechanism for students to ask and answer questions
# Students and instructors can choose ask and answer questions anonymously or have their names displayed

from discord.ext import commands

class QuestionsAnswers:
    ''' Class containing needed question/answer information and identification '''
    def __init__(self, qs, number, author, message, ans):
        self.question = qs
        self.number = number
        self.author = author
        self.msg = message
        self.answer = ans

class Qanda(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.question_number = 1
        self.qna_dict = {}

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: askQuestion(self, ctx, qs: str, anonymous)
    #    Description: takes question from user and reposts anonymously and numbered
    #    Inputs:
    #       - ctx: context of the command
    #       - qs: question text
    #       - anonymous: option if user wants their question to be shown anonymously
    #    Outputs:
    #       - User question in new post
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name='ask', help='Ask question. Please put question text in quotes. Add *anonymous* if desired.'
                                       'EX: $ask /"When is the exam?/" anonymous')
    async def askQuestion(self, ctx, qs: str, anonymous=''):

        # get author
        if anonymous == '':
            author = ctx.message.author.name
        elif anonymous == 'anonymous':
            author = anonymous
        else:
            await ctx.send('Unknown input for *anonymous* option. Please type **anonymous** or leave blank.')

        # format question
        q_str = 'Q' + str(self.question_number) + ': ' + qs + ' by ' + author + '\n'

        message = await ctx.send(q_str)

        # create QNA object
        new_question = QuestionsAnswers(qs, self.question_number, author, message.id, '')
        # add question to list
        self.qna_dict[self.question_number] = new_question

        # increment question number for next question
        self.question_number += 1

        # delete original question
        await ctx.message.delete()

def setup(bot):
    n = Qanda(bot)
    bot.add_cog(n)
