# About $addhw
This command lets the user (either the TAs or professor) to add a homework as a reminder to the discord channel 

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/deadline.py).

# Code Description
## Functions
1. duedate(self, ctx, coursename: str, hwcount: str, *, date: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, name of the course, name of the homework, and the date and time when the homework is due. 

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'addhw' pass in all the parameters as a space seperated inputs in the following order:
coursename, homeworkname, duedate (in MMM DD YYYY optional(HH:MM) format)
```
$addhw CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM)
$addhw CSC510 HW2 SEP 25 2024 17:02
```
Successful execution of this command will add the reminder for the specified coursework and homework on the specified time.

![$addhw CSC510 HW2 SEP 25 2024 17:02](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/addhomework.gif)