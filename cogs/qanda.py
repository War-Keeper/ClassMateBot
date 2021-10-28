# This functionality provides mechanism for students to ask and answer questions
# Students and instructors can choose ask and answer questions anonymously or have their names displayed
from discord import NotFound
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

    # -----------------------------------------------------------------------------------------------------------------
    # Function: answer
    # Description: adds user answer to specific question and post anonymously
    # Inputs:
    #      - ctx: context of the command
    #      - num: question number being answered
    #      - ans: answer text to question specified in num
    #      - anonymous: option if user wants their question to be shown anonymously
    # Outputs:
    #      - User answer added to question post
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name='answer',
                      help='Answer question. Please put answer text in quotes. Add *anonymous* if desired.'
                           'EX: $answer 1 /"Oct 12/" anonymous')
    async def answer(self, ctx, num, ans, anonymous=''):
        ''' answer the specific question '''

        # get author
        if anonymous == '':
            author = ctx.message.author.name
        elif anonymous == 'anonymous':
            author = anonymous
        else:
            await ctx.send('Unknown input for *anonymous* option. Please type **anonymous** or leave blank.')

        # check if question number exists
        if int(num) not in self.qna_dict.keys():
            await ctx.author.send('Invalid question number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        # get question
        q_answered = self.qna_dict[int(num)]
        # check if message exists
        try:
            message = await ctx.fetch_message(q_answered.msg)
        except NotFound:
            await ctx.author.send('Invalid question number: ' + str(num))
            # delete user msg
            await ctx.message.delete()
            return

        # generate and edit msg with answer
        if "instructor" in [y.name.lower() for y in ctx.author.roles]:
            role = 'Instructor'
        else:
            role = 'Student'
        new_answer = author + ' (' + role + ') Ans: ' + ans

        # store new answer
        if not q_answered.answer == '':
            q_answered.answer += '\n'
        q_answered.answer += new_answer

        # check if message exists and edit
        q_str = 'Q' + str(q_answered.number) + ': ' + q_answered.question
        content = q_str + '\n' + q_answered.answer
        try:
            await message.edit(content=content)
            # message.content = content
        except NotFound:
            await ctx.author.send('Invalid question number: ' + str(num))

        # delete user msg
        await ctx.message.delete()

def setup(bot):
    n = Qanda(bot)
    bot.add_cog(n)
