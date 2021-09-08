# TODO Group Creation and Inter-group Communication

import discord
from discord.ext import commands

import csv

class Helper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', help='join a group number')
    async def join(self, ctx):
        student_pool = load_pool()

        print(student_pool)
        student_pool['working'] = 'on it'
        print(student_pool)

        print_pool(student_pool)

    @commands.command(name='group', help='print amount of groups that are full')
    async def group(self, ctx):
        print('testing')

# TODO work on loading in groups, adding and subtracting from groups
def load_groups() -> dict:
    groups = {}
    return groups

def load_pool() -> dict:
    with open('data/server_data/name_mapping.csv', mode='r') as infile:
        reader = csv.reader(infile)
        student_pool = {rows[0]: rows[1] for rows in reader}
    return student_pool

def print_pool(pool):
    with open('data/server_data/name_mapping.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        for key, value in pool.items():
            writer.writerow([key, value])

def setup(bot):
    bot.add_cog(Helper(bot))

