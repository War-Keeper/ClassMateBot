# Copyright (c) 2021 War-Keeper

import csv
import discord
from discord.ext import commands
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db


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
        # get the arguments for the project to vote on
        project_num = int(arg2)

        # get the name of the caller
        member_name = ctx.message.author.display_name.upper()

        groups = db.query(
            'SELECT group_num FROM group_members WHERE guild_id = %s AND member_name = %s LIMIT 1',
            (ctx.guild.id, member_name)
        )

        # error handle if member is not in a group
        if len(groups) == 0:
            await ctx.send("Could not find the Group you are in, please contact a TA or join with your group number")
            raise commands.UserInputError

        num_groups = db.query(
            'SELECT COUNT(*) FROM project_groups WHERE guild_id = %s AND project_num = %s',
            (ctx.guild.id, project_num)
        )[0]

        # check if project has more than 6 groups voting on it
        if num_groups == 6:
            await ctx.send('A Project cannot have more than 6 Groups working on it!')
            return

        member_group = groups[0]
        voted_for = db.query(
            'SELECT project_num FROM project_groups WHERE guild_id = %s AND group_num = %s',
            (ctx.guild.id, member_group)
        )
        if voted_for:
            project_voted_for, *_ = voted_for[0]
            await ctx.send(f'You already voted for Project {project_voted_for}')
            return

        # add the group to the project list
        db.query(
            'INSERT INTO project_groups (guild_id, project_num, group_num) VALUES (%s, %s, %s)',
            (ctx.guild.id, project_num, member_group)
        )
        await ctx.send(f'{member_group} has voted for Project {project_num}!')

    # this handles errors related to the vote command
    @vote.error
    async def vote_error(self, ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send('To join a group, use the join command, do: $vote \'Project\' <Num> \n \
            ( For example: $vote Project 0 )')
        print(error)

    # ----------------------------------------------------------------------------------
    #    Function: projects(self, ctx)
    #    Description: prints the list of current projects
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: prints the list of current projects
    # ----------------------------------------------------------------------------------
    @commands.command(name='projects', help='print projects with groups assigned to them', pass_context=True)
    # @commands.dm_only()
    async def projects(self, ctx):
        projects = db.query(
            "SELECT project_num, string_agg(group_num::text, ', ') AS group_members FROM project_groups WHERE guild_id = %s GROUP BY project_num",
            (ctx.guild.id,)
        )
        
        await ctx.send('\n'.join(f'Project {project_num}: Group(s) {group_members}' for project_num, group_members in projects))


# -----------------------------------------------------------
# add the file to the bot's cog system
# -----------------------------------------------------------
def setup(bot):
    bot.add_cog(Voting(bot))


