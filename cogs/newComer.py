import discord
from discord.ext import commands
import os
import csv
import random
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db


# ---------------------------------------------------------------------------------------
# Contains commands for member verification, which is handled with direct DMs to the bot
# ---------------------------------------------------------------------------------------
class Helper(commands.Cog):
    path = os.path.join("data", "welcome")

    def __init__(self, bot):
        self.bot = bot

    # -------------------------------------------------------------------------------------------------------------
    #    Function: verify(self, ctx, *, name: str = None)
    #    Description: Ask the bot to give the user the verified role in the server
    #    Constraint: only other verified members can use this command
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - *:
    #    - name: name of the user to verify
    #    Outputs: returns a success message if the user is successfully verified or error in case of syntax problems
    # --------------------------------------------------------------------------------------------------------------
    @commands.has_role("verified")
    @commands.command(
        name="verify",
        pass_context=True,
        help="Request the bot to verify the user to get access to channels",
    )
    async def verify(self, ctx, *, name: str = None):
        member = ctx.message.author

        #check if verified and unverified roles exist
        if discord.utils.get(ctx.guild.roles, name="unverified") == None:
            await ctx.send("Warning: there is no unverified role in this server!")
            pass
        if discord.utils.get(ctx.guild.roles, name="verified") == None:
            await ctx.send("Warning: there is no verified role in this server!")
            pass

        # finds the unverified role in the guild
        unverified = discord.utils.get(ctx.guild.roles, name="unverified")

        # checks if the user running the command has the unverified role
        if unverified in member.roles:
            if name == None:
                await ctx.send(
                    "To use the verify command, do: $verify <your_full_name> \n ( For example: $verify Jane Doe )"
                )
            else:
                # finds the verified role in the guild
                verified = discord.utils.get(ctx.guild.roles, name="verified")
                db.query('INSERT INTO name_mappings (guild_id, username, real_name) VALUES (%s, %s, %s)', (ctx.guild.id, member.name, name))

                await member.add_roles(verified)  # adding verfied role
                await member.remove_roles(unverified)  # removed verfied role
                await ctx.send(f"Thank you for verifying! You can start using {ctx.guild.name}!")
                embed = discord.Embed(
                    description="Click [Here](https://github.com/txt/se21) for the home page of the class Github page"
                )
                welcome_images = os.listdir(self.path)
                selected_image = random.choice(welcome_images)
                file = discord.File(os.path.join(self.path, selected_image))
                embed.set_image(
                    url="attachment://" + selected_image
                )  # Embedding the image
                await member.send(file=file, embed=embed)
        else:  # user has verified role
            await ctx.send("You are already verified!")
            embed = discord.Embed(
                description="Click [Here](https://github.com/txt/se21) for the home page of the class Github page"
            )
            await member.send(embed=embed)


# --------------------------------------
# add the file to the bot's cog system
# --------------------------------------
def setup(bot):
    bot.add_cog(Helper(bot))


# Copyright (c) 2021 War-Keeper
