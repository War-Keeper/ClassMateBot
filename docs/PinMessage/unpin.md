# About $unpin
This command lets the student to delete a pinned message from their private pinning board.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/pinning.py)

# Code Description
## Functions
1. deleteMessage(self, ctx, tagname: str, *, description: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, tag-name of the pinned message and the description given by the student.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'unpin' pass in all the parameters as a space seperated inputs in the following order:
tagname, link of the message, description
```
$unpin TAGNAME DESCRIPTION
$unpin HW HW8 reminder
```
Successful execution of this command will pin the message for the specific user.

![$unpin HW HW8 reminder](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/unpin.gif)
