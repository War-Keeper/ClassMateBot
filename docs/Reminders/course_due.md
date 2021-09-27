# About $coursedue
This command lets the user display all the homeworks that are due for a specific course. 

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/deadline.py).

# Code Description
## Functions
1. def coursedue(self, ctx, courseid: str): <br>
This function takes as arguments the values provided by the constructor through self and the context in which the command was called. It also takes course name as input.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command '$coursedue' with coursename as a parameter:

```
$coursedue CSC505
```
Successful execution of this command will display all the homeworks that are due on that day.

![$coursedue](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/coursedue.gif)