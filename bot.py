# bot.py
import os

import discord
from discord import Intents
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.ext.commands import Bot, has_permissions, CheckFailure

# ----------------------------------------------------------------------------------------------
# Initializes the discord bot with a unique TOKEN and joins the bot to a server provided by the
# GUILD token. Handles bot shutdown and error events
# ----------------------------------------------------------------------------------------------

# Load the environment
load_dotenv()
# Get the token for our bot
TOKEN = os.getenv("TOKEN")
# Get the token for our discord server
GUILD = os.getenv("GUILD")
UNVERIFIED_ROLE_NAME = os.getenv("UNVERIFIED_ROLE_NAME")
# Set the bots intents to all
intents = Intents.all()
# Set all bot commands to begin with $
bot = Bot(intents=intents, command_prefix="$")


# ------------------------------------------------------------------------------------------------------------------
# Activates when the bot starts, prints the name of the server it joins and the names of all members of that server
# ------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f"{bot.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )

    members = "\n -".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    bot.load_extension("jishaku")

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="Over This Server"
        )
    )
    print("READY!")


# ------------------------------------------------------------------------------------------
# Handles on_member_join events, DMs the user and asks for verification through newComer.py
# ------------------------------------------------------------------------------------------
@bot.event
async def on_member_join(member):
    unverified = discord.utils.get(
        member.guild.roles, name=UNVERIFIED_ROLE_NAME
    )  # finds the unverified role in the guild
    await member.add_roles(unverified)
    await member.send("Hello " + member.name + "!")
    await member.send(
        "Verify yourself before getting started! \n To use the verify command, do: $verify <your_full_name> \n ( For example: $verify Jane Doe )")


# ------------------------------------------------
# Handles bot errors, prints errors to a log file
# ------------------------------------------------
@bot.event
async def on_error(event, *args, **kwargs):
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise


# ----------------------------------
# Command for shutting down the bot
# ----------------------------------
@bot.command(name="shutdown", help="Shuts down the bot, only usable by the owner")
@has_permissions(administrator=True)
async def shutdown(ctx):
    await ctx.send('Shutting Down bot')
    print("Bot closed successfully")
    ctx.bot.logout()
    exit()


# Starts the bot with the current token
bot.run(TOKEN)

# Copyright (c) 2021 War-Keeper
