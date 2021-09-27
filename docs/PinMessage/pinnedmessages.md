# About $pinnedmessages
This command lets the student to retrieve all the pinned messages from their private pinning board (all messages under one tagname).

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/pinning.py)

# Code Description
## Functions
retrieveMessages(self, ctx, tagname: str):
This function takes as arguments the values provided by the constructor through self, context in which the command was called, tag-name of the pinned message(s).

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'pinnedmessage' pass in all the parameters as a space seperated inputs in the following order:
tagname, link of the message, description.
```
$pin TAGNAME 
$pinnedmessages HW
```
Successful execution of this command will pin the message for the specific user.

![$pinnedmessages HW](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/pinnedmessages.gif)
