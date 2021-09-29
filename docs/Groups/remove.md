# About $remove
This command lets the student remove their name to the group member list. This is used to ensure that if a member switches groups or drops the class, then they can be removed from a group.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/groups.py)

# Code Description
## Functions
remove(self, ctx, arg='group', arg2='-1'): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the group argument and the number argument.

# How to run it? (Small Example)
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. All you have to do is 
enter the command 'remove group <number>' or just 'remove'.
```
$remove group <NUMBER>
$remove group 0
$remove
```
Successful execution of this command will return a message saying you have been removed from the group.

![$remove HW](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/remove.gif)