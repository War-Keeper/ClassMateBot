# About $updatepin
This command lets the student to update a pinned message with a new link from the discord channel to their private pinning board.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/pinning.py)

# Code Description
## Functions
updatePinnedMessage(self, ctx, tagname: str, new_link: str, *, description: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, tag-name of the old pinned message, new link of the message to be pinned, and the old description given by the student.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'updatepin' pass in all the parameters as a space seperated inputs in the following order:
tagname, link of the message, description.
```
$pin TAGNAME NEWLINK DESCRIPTION
$updatepin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890814489480531969 HW8 reminder
```
Successful execution of this command will pin the message for the specific user.

![$updatepin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890814489480531969 HW8 reminder](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/updatepin.gif)
