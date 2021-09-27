# About $pin
This command lets the student to pin a message from the discord channel to their private pinning board.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/pinning.py)

# Code Description
## Functions
addMessage(self, ctx, tagname: str, link: str, *, description: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, tag-name of the pinned message, link of the message to be pinned, and the description given by the student.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'pin' pass in all the parameters as a space seperated inputs in the following order:
tagname, link of the message, description
```
$pin TAGNAME LINK DESCRIPTION
$pin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 HW8 reminder
```
Successful execution of this command will pin the message for the specific user.

![$pin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 HW8 reminder](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/pin.gif)
