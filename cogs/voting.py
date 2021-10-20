# Copyright (c) 2021 War-Keeper

import csv
import discord
from discord.ext import commands
import os


# -----------------------------------------------------------
# This File contains commands for voting on projects,
# displaying which groups have signed up for which project
# -----------------------------------------------------------
class Voting(commands.Cog):

    # -----------
    # initialize
    # -----------
    def __init__(self, bot):
        self.bot = bot

    # ----------------------------------------------------------------------------------------------------------
    #    Function: vote(self, ctx, arg='Project', arg2='-1')
    #    Description: "votes" for the given project by adding the user to it
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - arg: the name of the project
    #    - arg2: the number of the project
    #    Outputs: adds the user to the given project or returns an error if the project is invalid or the user
    #             is not in a valid group
    # ----------------------------------------------------------------------------------------------------------
    @commands.command(name='vote', help='Used for voting for Project 2 and 3, \
    To use the vote command, do: $vote \'Project\' <Num> \n \
    (For example: $vote project 0)', pass_context=True)
    async def vote(self, ctx, arg='Project', arg2='-1'):
        # load the groups from the csv
        groups = load_groups(ctx.guild.id)
        # load the projects from the csv
        projects = load_projects(ctx.guild.id)

        # get the arguments for the project to vote on
        project_num = arg.upper() + ' ' + arg2

        # get the name of the caller
        member_name = ctx.message.author.display_name.upper()

        # initialize which group the member in in
        member_group = '-1'

        # check which group the member is in
        for key in groups.keys():
            if member_name in groups[key]:
                member_group = key
                print(member_group)

        # error handle if member is not in a group
        if member_group == '-1':
            await ctx.send("Could not fine the Group you are in, please contact a TA or join with your group number")
            raise commands.UserInputError

        # if the project is a valid option
        if project_num in projects:

            # check if project has more than 6 groups voting on it
            if len(projects[project_num]) == 6:
                await ctx.send('A Project cannot have more than 6 Groups working on it!')
                return

            # check if you have already voted for another group
            for key in projects.keys():
                if member_group in projects[key]:
                    print(member_group)
                    await ctx.send('You already voted for ' + key.title())
                    return

            # add the group to the project list
            db.query(
                'INSERT INTO projects (guild_id, project_num, group_num) VALUES (%s, %s, %s)',
                (ctx.guild.id, project_num, member_group)
            )
            await ctx.send(member_group + ' has voted for ' + project_num.title() + '!')

        # error handling
        else:
            await ctx.send('Not a valid Project')
            await ctx.send('Used for voting for Project 2 and 3, To use the vote command, do: $vote \'Project\' <Num> \n \
            (For example: $vote project 0)')

    # this handles errors related to the vote command
    @vote.error
    async def vote_error(self, ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send('To join a group, use the join command, do: $vote \'Project\' <Num> \n \
            ( For example: $vote Project 0 )')

    # ----------------------------------------------------------------------------------
    #    Function: projects(self, ctx)
    #    Description: prints the list of current projects
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: prints the list of current projects
    # ----------------------------------------------------------------------------------
    @commands.command(name='projects', help='print projects with groups assigned to them', pass_context=True)
    @commands.dm_only()
    async def projects(self, ctx):

        projects = load_projects()
        overall = ''
        for key in projects.keys():
            if key != 'PROJECT_NUM':
                s = ''
                temp = projects[key]
                for num in temp:
                    s += num + ', '
                if s != '':
                    overall += key + ': ' + s[:-2] + '\n'
                else:
                    overall += key + ': \n'
        await ctx.send(overall)


# -----------------------------------------------------------
# Used to load the Project from the csv file into a dictionary
# -----------------------------------------------------------
def load_projects(guild_id) -> dict:
    projects = db.query('SELECT array_agg(group_num) FROM projects WHERE guild_id = %s GROUP BY project_num', (guild_id,))
    # dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # os.chdir(dir)
    # os.chdir('data')
    # os.chdir('server_data')
    # with open('Project_mapping.csv', mode='r') as infile:
    #     reader = csv.reader(infile)
    #     student_pools = {rows[0].upper(): [rows[1].upper(), rows[2].upper(), rows[3].upper(), rows[4].upper(),
    #                                        rows[5].upper(), rows[6].upper()] for rows in reader}
    # for key in student_pools.keys():
    #     student_pools[key] = list(filter(None, student_pools[key]))

    return projects


# -----------------------------------------------------------
# Used to load the groups from the csv file into a dictionary
# -----------------------------------------------------------
def load_groups(guild_id) -> dict:
    groups = db.query('SELECT array_agg(member_name) FROM groups WHERE guild_id = %s GROUP BY group_num', (guild_id,))
    # dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # os.chdir(dir)
    # os.chdir('data')
    # os.chdir('server_data')
    # with open('groups.csv', mode='r') as infile:
    #     reader = csv.reader(infile)
    #     group = {rows[0].upper(): [rows[1].upper(), rows[2].upper(), rows[3].upper(), rows[4].upper(),
    #                                rows[5].upper(), rows[6].upper()] for rows in reader}

    # for key in group.keys():
    #     group[key] = list(filter(None, group[key])
    # )

    # TODO CHECK

    return groups


# -----------------------------------------------------------
# add the file to the bot's cog system
# -----------------------------------------------------------
def setup(bot):
    bot.add_cog(Voting(bot))


