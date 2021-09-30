# Contributing to ClassMateBot

Thank you so much for taking an interest in contributing!

Follow the set of guidelines below to contribute to ClassMateBot!

## Code of Conduct

By participating, you are expected to uphold this code. Please report unacceptable behavior to cpatel3@ncsu.edu, webrown2@ncsu.edu.

Prerequisites required before starting this project during the Fall of 2021.

1. Must be a graduate student at NC State University
2. Must be a student in Software Engineering Course in Fall 2021
3. Have proficiency in Python

Starting 2022, anyone will be allowed to contribute, provided you have experience with python, discord.py and experience with GitHub

## How can I Contribute -

### Pull Requests

The process described here has several goals:

- Maintain the projects quality

- Fix problems that are important to users

- Enable a sustainable system for the projects maintainers to review contributions

Please follow these steps to have your contribution reviewed by the maintainers:

1. Include a clear and descriptive title.
2. Include a description of the change.

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

### Adding Commands
 Commands can be added in the form of Cogs. View hello.py as a simple example of how a Cog can be added.

The basic structure is as follows:

```
class <NAME>(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    <COMMANDS RELATED TO THIS FILE>
    
def setup(bot):
    bot.add_cog(<NAME>(bot))
```
For more information on how to use cogs, refer to the [Cogs Page](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)

For more information on the API of discord.py you can use the [API Reference Page](https://discordpy.readthedocs.io/en/stable/api.html)

For general Knowledge of discord.py use the [Documentation Page](https://discordpy.readthedocs.io/en/latest/index.html)
## Reporting Bugs

This section guides you through submitting a bug report for ClassMateBot. 
Following these guidelines helps maintainers and the community understand your report, reproduce the behavior and find related reports.

### How Do I Submit A (Good) Bug Report?

- Use a clear and descriptive title for the issue to identify the problem.

- Describe the exact steps which reproduce the problem in as many details as possible.

- Provide specific examples to demonstrate the steps. 

- Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.

- Explain which behavior you expected to see instead and why.

- Include screenshots and animated GIFs which show you following the described steps and clearly demonstrate the problem. 

- If the problem is related to performance or memory, include a CPU profile capture with your report.

## Styleguides

### Git Commit Messages

- Describe why a change is being made.

- Describe any limitations of the current code.

- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")

- Limit the first line to 72 characters or less

