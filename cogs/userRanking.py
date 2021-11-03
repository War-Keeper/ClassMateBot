from math import floor

import discord
from discord.ext import commands
import json
import sys
import os
from datetime import datetime


class userRanking(commands.Cog):

    def __init__(self, client):
        cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(cur_dir)
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('data/participation/users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

        with open('data/participation/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            os.chdir(cur_dir)
            with open('data/participation/users.json', 'r') as f:
                users = json.load(f)
            await self.update_data(users, message.author)
            await self.add_experience(users, message.author)
            await self.level_up(users, message.author)

            with open('data/participation/users.json', 'w') as f:
                json.dump(users, f, indent=4)

    async def update_data(self, users, user):
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 1

    async def add_experience(self, users, user):
        users[str(user.id)]['experience'] += 15

    async def level_up(self, users, user):
        experience = users[str(user.id)]['experience']
        lvl = users[str(user.id)]['level']
        lvl_end = 5 * (lvl ** 2) + (50 * lvl) + 100
        print(user)
        print(f"Level:{lvl}")
        print(f"experience:{experience}")
        print(f"lvl_end: {lvl_end} ")

        if lvl_end <= experience:
            channel = self.client.get_channel(900580609540362303)
            await channel.send('{} has levelled up to level {} ! 🙌'.format(user.mention, lvl + 1))
            users[str(user.id)]['level'] = lvl + 1
            users[str(user.id)]['experience'] -= lvl_end

    async def to_integer(self, dt_time):
        answer = 100000000 * dt_time.year + 1000000 * \
                 dt_time.month + 10000 * dt_time.day + 100 * dt_time.hour + dt_time.minute
        return int(answer)

    @commands.command()
    async def level(self, ctx, user: discord.Member = None):
        with open('data/participation/users.json', 'r') as f:
            users = json.load(f)

        if user is None:
            if not str(ctx.author.id) in users:
                users[str(ctx.author.id)] = {}
                users[str(ctx.author.id)]['experience'] = 0
                users[str(ctx.author.id)]['level'] = 0

            user = ctx.author
            lvl = int(users[str(ctx.author.id)]['level'])
            exp = int(5 * (lvl ** 2) + (50 * lvl) + 100)  # XP cap
            experience = int(users[str(user.id)]['experience'])
            boxes = floor((experience * 20) / exp)

            embed = discord.Embed(Title=f"**{user}'s Rank**",
                                  Description=f"Experience: {lvl}/{5 * (lvl ** 2) + (50 * lvl) + 100}", color=0x0091ff)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name=f"**{user}'s Rank**", value="🙌  ", inline=False)
            embed.add_field(name="Level", value=f"**{users[str(user.id)]['level']}**", inline=True)
            embed.add_field(name="Experience", value=f"**{str(int(users[str(user.id)]['experience']))} / {exp}**",
                            inline=True)
            embed.add_field(name="Progress Bar",
                            value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:", inline=False)
            embed.set_footer(text="Contribute more to level up!")
            await ctx.send(embed=embed)

        else:
            if not str(user.id) in users:
                users[str(user.id)] = {}
                users[str(user.id)]['experience'] = 0
                users[str(user.id)]['level'] = 0
                users[str(user.id)]['LastMessage'] = await self.to_integer(datetime.now())
            lvl = int(users[str(user.id)]['level'])
            exp = int(5 * (lvl ** 2) + (50 * lvl) + 100)
            experience = int(users[str(user.id)]['experience'])
            boxes = floor((experience * 20) / exp)

            embed = discord.Embed(Title=f"**{user}'s Rang**",
                                  Description=f"Experience: {lvl}/{5 * (lvl ** 2) + (50 * lvl) + 100}", color=0x0091ff)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name=f"**{user}'s Rang**", value="🙌  ", inline=False)
            embed.add_field(name="Level", value=f"**{users[str(user.id)]['level']}**", inline=True)
            embed.add_field(name="Experience", value=f"**{str(int(users[str(user.id)]['experience']))} / {exp}**",
                            inline=True)
            embed.add_field(name="Progress Bar",
                            value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:", inline=False)
            embed.set_footer(text="Contribute more to level up!")
            await ctx.send(embed=embed)

        with open('data/participation/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    @commands.command()
    async def add_database(self, ctx, user: discord.Member):
        with open('data/participation/users.json', 'r') as f:
            users = json.load(f)
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 0
            users[str(user.id)]['LastMessage'] = await self.to_integer(datetime.now())
            await ctx.send("added to database!")
        else:
            await ctx.send("already in database!")

        with open('data/participation/users.json', 'w') as f:
            json.dump(users, f, indent=4)


def setup(bot):
    bot.add_cog(userRanking(bot))
