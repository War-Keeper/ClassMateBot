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
        member_name = ctx.message.author.display_name.upper()
        member_group = '-1'

        for key in groups.keys():
            if member_name in groups[key]:
                member_group = key
                print(member_group)

        if member_group == '-1':
            await ctx.send("Could not fine the Group you are in, please contact a TA or join with your group number")
            raise commands.UserInputError

        if project_num in projects:

            if len(projects[project_num]) == 6:
                await ctx.send('A Project cannot have more than 6 Groups working on it!')
                return

            for key in projects.keys():
                if member_group in projects[key]:
                    print(member_group)
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

    @commands.command(name='projects', help='print projects with groups assigned to them', pass_context=True)
    async def projects(self, ctx):
        embed = discord.Embed(title='Project List', color=discord.Color.teal())
        embed.set_thumbnail(url="https://i.pinimg.com/474x/e7/e3/bd/e7e3bd1b5628510a4e9d7a9a098b7be8.jpg")

        embed2 = discord.Embed(title='Project List', color=discord.Color.teal())
        embed2.set_thumbnail(url="https://i.pinimg.com/474x/e7/e3/bd/e7e3bd1b5628510a4e9d7a9a098b7be8.jpg")

        embed3 = discord.Embed(title='Project List', color=discord.Color.teal())
        embed3.set_thumbnail(url="https://i.pinimg.com/474x/e7/e3/bd/e7e3bd1b5628510a4e9d7a9a098b7be8.jpg")

        embed4 = discord.Embed(title='Project List', color=discord.Color.teal())
        embed4.set_thumbnail(url="https://i.pinimg.com/474x/e7/e3/bd/e7e3bd1b5628510a4e9d7a9a098b7be8.jpg")

        projects = load_projects()

        count = 0

        for key in projects.keys():
            if key != 'PROJECT_NUM':
                if count < 10:
                    embed.add_field(name=key, value=str(projects[key]), inline=True)
                elif 10 < count < 20:
                    embed2.add_field(name=key, value=str(projects[key]), inline=True)
                elif 20 < count < 30:
                    embed3.add_field(name=key, value=str(projects[key]), inline=True)
                elif 30 < count < 40:
                    embed4.add_field(name=key, value=str(projects[key]), inline=True)
                count += 1

        embed.set_footer(text="Which groups have voted for which project")
        embed2.set_footer(text="Which groups have voted for which project")
        embed3.set_footer(text="Which groups have voted for which project")
        embed4.set_footer(text="Which groups have voted for which project")

        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)

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
