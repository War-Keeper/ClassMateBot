# TODO Group Creation and Inter-group Communication

import discord
from discord.ext import commands

import csv

class Helper(commands.Cog):
    student_pool = {}
    groups = {}

    def __init__(self, bot):
        self.bot = bot

    # TODO work on getting a member to join a group
    @commands.command(name='join', help='join a group number', pass_context=True)
    async def join(self, ctx, arg):

        student_pool = load_pool()

        student_pool[ctx.message.author.display_name] = arg

        print_pool(student_pool)

    @join.error
    async def join_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('To use the join command, do: $join <Group Num> \n ( For example: $join Group 0 )')

    # TODO work on displaying the group sizes
    @commands.command(name='group', help='print amount of groups that are full', pass_context=True)
    async def group(self, ctx):
        groups = load_groups()
        print_groups(groups)

def load_groups() -> dict:
    with open('data/server_data/groups.csv', mode='r') as infile:
        reader = csv.reader(infile)
        group = {rows[0].upper(): [rows[1].upper(), rows[2].upper(), rows[3].upper(), rows[4].upper(), rows[5].upper(), rows[6].upper()] for rows in reader}

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

def load_pool() -> dict:
    with open('data/server_data/name_mapping.csv', mode='r') as infile:
        reader = csv.reader(infile)
        student_pools = {rows[0].upper(): rows[1].upper() for rows in reader}
    return student_pools

def print_pool(pools):
    with open('data/server_data/name_mapping.csv', mode='w', newline="") as outfile:
        writer = csv.writer(outfile)
        for key, value in pools.items():
            writer.writerow([key, value])

def setup(bot):
    bot.add_cog(Helper(bot))

