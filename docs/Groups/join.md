# About $join
This command lets the student add their name to the group member list. This is used to ensure that all students can get into a group. making sure no duplicates occur in the process

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/groups.py)

# Code Description
## Functions
join(self, ctx, arg='group', arg2='-1'): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the group argument and the number argument.

# How to run it? (Small Example)
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. All you have to do is 
enter the command 'join group <number>'.
```
$join group <NUMBER>
$join group 0
```
Successful execution of this command will return a message saying you have joined the group.

