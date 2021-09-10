# Main file for bot pytest actions. Uses dpytest to test bot activity on a simulated server with simulated members

import discord.ext.test as dpytest
import pytest


# Tests cogs/hello.py
@pytest.mark.asyncio
async def test_hello(bot):
    await dpytest.message("$hello")
    assert dpytest.verify().message().content("Hello World!")
