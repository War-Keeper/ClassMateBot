import os

import discord.ext.test as dpytest
import pytest
from discord import Intents
from discord.ext.commands import Bot
from setuptools import glob

intents = Intents.all()


# Default parameters for the simulated dpytest bot. Loads the bot with commands from the /cogs directory
# Ran everytime pytest is called
@pytest.fixture
def bot(event_loop):
    bot = Bot(intents=intents, command_prefix="$", loop=event_loop)
    dir = os.path.dirname(os.getcwd())
    os.chdir(dir)
    os.chdir('cogs')
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.py'):
            bot.load_extension(f"cogs.{filename[:-3]}")
    bot.load_extension('jishaku')
    dpytest.configure(bot)
    return bot


# Cleans up leftover files generated through dpytest
def pytest_sessionfinish():
    # Clean up attachment files
    files = glob.glob('./dpytest_*.dat')
    for path in files:
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error while deleting file {path}: {e}")
    print("\nTests closed successfully")
