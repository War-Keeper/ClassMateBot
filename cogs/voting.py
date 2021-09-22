# TODO work on voting for projects
import csv
import discord
from discord.ext import commands

class Helper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vote', help='Used for voting for Project 2 and 3, \
    To use the vote command, do: $vote <Project Num> \n \
    (For example: $vote project 0)', pass_context=True)
    async def vote(self, ctx,arg='Project', arg2='-1'):
        groups = load_groups()
        projects = load_projects()

        project_num = arg.upper() + ' ' + arg2
        member_name = ctx.message.author.display_name
        member_group = None

        for key in groups.keys():
            if member_name in groups[key]:
                member_group = key

        if member_group is None:
            await ctx.send("Could not fine the Group you are in, please contact a TA or join with your group number")
            raise commands.UserInputError

        if project_num in projects:

            if len(projects[project_num]) == 6:
                await ctx.send('A Project cannot have more than 6 Groups working on it!')
                return

            for key in projects.keys():
                if member_group in projects[key]:
                    await ctx.send('You already voted for ' + key)
                    return

            projects[project_num].append(member_group)
            await ctx.send(member_group + ' has voted for ' + project_num + '!')
            print_projects(projects)

        else:
            await ctx.send('Not a valid Project')
            await ctx.send('Used for voting for Project 2 and 3, To use the vote command, do: $vote <Project Num> \n \
            (For example: $vote project 0)')

    @vote.error
    async def vote_error(self, ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send('To join a group, use the join command, do: $join <Group Num> \n \
            ( For example: $join Group 0 )')

def load_projects() -> dict:
    with open('data/server_data/Project_mapping.csv', mode='r') as infile:
        reader = csv.reader(infile)
        student_pools = {rows[0].upper(): [rows[1].upper(), rows[2].upper(), rows[3].upper(), rows[4].upper(),
                                           rows[5].upper(), rows[6].upper()] for rows in reader}
    for key in student_pools.keys():
        student_pools[key] = list(filter(None, student_pools[key]))

    return student_pools

def print_projects(projects):
    with open('data/server_data/Project_mapping.csv', mode='w', newline="") as outfile:
        writer = csv.writer(outfile)
        for key in projects.keys():
            while len(projects[key]) < 6:
                projects[key].append(None)
            writer.writerow([key] + projects[key])

def load_groups() -> dict:
    with open('data/server_data/groups.csv', mode='r') as infile:
        reader = csv.reader(infile)
        group = {rows[0].upper(): [rows[1].upper(), rows[2].upper(), rows[3].upper(), rows[4].upper(),
                                   rows[5].upper(), rows[6].upper()] for rows in reader}

    for key in group.keys():
        group[key] = list(filter(None, group[key]))

    return group

def print_groups(group):
    with open('data/server_data/groups.csv', mode='w', newline="") as outfile:
        writer = csv.writer(outfile)
        for key in group.keys():
            while len(group[key]) < 6:
                group[key].append(None)
            writer.writerow([key] + group[key])

def setup(bot):
    bot.add_cog(Helper(bot))
