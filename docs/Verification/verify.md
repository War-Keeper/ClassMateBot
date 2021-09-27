# About $verify
This command verifies the user by getting his/her full name and then giving access to the channels

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/War-Keeper/ClassMateBot/blob/main/bot.py) and [here](https://github.com/War-Keeper/ClassMateBot/blob/main/cogs/newComer.py).

# Code Description
## Functions
1. def on_member_join(member): <br>
This function gets called when a new member joins the server. It takes as arguments the object of the member who has joined the server.

2. def verify(self, ctx, *, name: str = None): <br>
This function is used to get the full name of the user and give access to the channels. It takes as arguments the values provided by the constructor through self, context in which the command was called and full name of the user. 

# How to run it? (Small Example)
Let's say that you join the server that has the Classmate Bot active and online, you won't have the access to the channels as you will be assigned a some unverified role. You will receive a DM from the Classmate Bot to verify yourself to get access to the channels with appropriate instructions. All you have to do is 
enter the command '$verify' pass in your full name as a parameters as a space seperated inputs.
```
$verify your_full_name
$addhw Jane Doe
```
Successful execution of this command will assign you some verified role and give you the access to the chanels. You will also receive a welcome message from Classmate Bot with important links related to the course.
