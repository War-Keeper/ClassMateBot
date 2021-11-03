import discord
from discord.ext import commands
import os
import random
import sys
import db
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------------------------------------------------------------------------------------
# Contains commands for member verification, which is handled with direct DMs to the bot
# ---------------------------------------------------------------------------------------
class NewComer(commands.Cog):
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

    @commands.command(
        name="verify",
        pass_context=True,
        help="User self-verifies by attaching their real name to their discord username in this server: "
             "$verify <FirstName LastName>",
    )
    async def verify(self, ctx, *, name: str = None):
        member = ctx.message.author

        # check if verified and unverified roles exist
        if discord.utils.get(ctx.guild.roles, name="unverified") is None \
                or discord.utils.get(ctx.guild.roles, name="verified") is None:
            await ctx.send("Warning: Please make sure the verified and unverified roles exist in this server!")
            return

        # finds the unverified role in the guild
        unverified = discord.utils.get(ctx.guild.roles, name="unverified")
        verified = discord.utils.get(ctx.guild.roles, name="verified")

        # checks if the user running the command has the unverified role
        if verified not in member.roles:
            if name is None:
                await ctx.send(
                    "To use the verify command, do: $verify <FirstName LastName> \n ( For example: $verify Jane Doe )"
                )
            else:
                # finds the verified role in the guild
                db.query('INSERT INTO name_mapping (guild_id, username, real_name) VALUES (%s, %s, %s)', (ctx.guild.id, member.name, name))

                await member.add_roles(verified)  # adding verified role
                await member.remove_roles(unverified)  # removed unverified role
                await ctx.send(f"Thank you for verifying! You can start using {ctx.guild.name}!")
                embed = discord.Embed(
                    description="Click [Here](https://github.com/txt/se21) for the home page of the class Github page"
                )
                await member.send(embed=embed)
        else:  # user has verified role
            db.query('SELECT real_name from name_mapping where guild_id = %s and username = %s', (ctx.guild.id, member.name))
            await ctx.send("You are already verified!")
            embed = discord.Embed(
                description="Click [Here](https://github.com/txt/se21) for the home page of the class Github page"
            )
            await member.send(embed=embed)


# --------------------------------------
# add the file to the bot's cog system
# --------------------------------------
def setup(bot):
    n = NewComer(bot)
    bot.add_cog(n)


# Copyright (c) 2021 War-Keeper
