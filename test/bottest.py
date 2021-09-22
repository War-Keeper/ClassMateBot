# Main file for bot pytest actions. Uses dpytest to test bot activity on a simulated server with simulated members

import discord.ext.test as dpytest
import pytest


# Tests cogs/hello.py
@pytest.mark.asyncio
async def test_hello(bot):
    await dpytest.message("$hello")
    assert dpytest.verify().message().content("Hello World!")

# Tests cogs/ping.py
@pytest.mark.asyncio
async def test_ping(bot):
    await dpytest.message("$ping")
    assert dpytest.verify().message().contains().content("Pong!")

