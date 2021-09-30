<p align="center"><img width=20.5% src="https://github.com/War-Keeper/ClassMateBot/blob/main/data/neworange.png"></p>
<p align="center"><img width=60% src="https://github.com/War-Keeper/ClassMateBot/blob/main/data/bot.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-yellow.svg)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5539956.svg)](https://doi.org/10.5281/zenodo.5539956)
![Build Status](https://github.com/War-Keeper/ClassMateBot/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/War-Keeper/ClassMateBot/branch/main/graph/badge.svg)](https://codecov.io/gh/War-Keeper/ClassMateBot)

<p align="center">
  <a href="#installation">Installation</a>
  ::
  <a href="#basic-overview">Basic Overview</a>
  ::
  <a href="#description">Description</a>
  ::
  <a href="#future-scope">Future Scope</a>
  ::
  <a href="#contributors">Contributors</a>
  
</p>

---

## Basic Overview

This project helps to improve the life of students, TAs and teachers by automating many mundane tasks which are sometimes done manually. ClassMateBot is a discord bot made in Python and could be used for any discord channel.

---

## Description

There are three basic user groups in a ClassMateBot, which are Students, Professor and TAs. Some basic tasks for the bot for the students user group should be automating the task of group making for projects or homewroks, Projection deadline reminders, etc. For TAs it is taking up polls, or answering FAQs asked by the students. 


Our ClassMateBot focuses on the student side of the discord channel, i.e. currently it focuses on the problems faced by the students while using these discord channels.

The user stories covered here would be more concerned about the activities for the channel for Software Engineering class in North Carolina State University for the Fall 2021 semester.

---

### 1 - Student Verification
Once the new member joins the server, before giving them the access to the channels there is a need to get the real full name of the memeber to map it with the discord nick name. This mapping can later be used for group creation, voting and so on. To do this we first assign the unverified role to the new comer and then ask them to verify their identity using $verify command. If that goes through the member is assigned a student role and has full access to the server resources. The bot then welcomes the member and also provides important links related to the course. A little example is provided below.
![$verify Jane Doe](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/verify.gif)

### 2 - Project Voting
The most important task in the upcoming semester that the bot automates is Project Voting which takes place at the end of the month of September and October. Our ClassMateBot allows the student to vote for a particular project which they would like to work on in the coming cycle. This task if done manually could be tedious as the students would have to wait for the TAs or Professor to announce which project they would be getting if voting is done manually. But the bot automates this process and would give out the results as soon as all the students have voted for their choices. A little example is provided below.
![$vote HW](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/vote.gif)

### 3 - Deadline Reminder
Next important thing our project covers is the Deadline reminder feature of our bot. Whenever a homework or project deadline is close the bot itself sends out a reminder to all the students so that they could submit their work on time. This feature also lets the students add other reminders along with the scheduled ones. For example, HW4 is due on 7th october, along with that the student is working on different assignments or homeworks of other subjects then they could add the other reminders too so that they are in touch with all their pending work. A little example is provided below.
![$addhw CSC510 HW2 SEP 25 2024 17:02](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/addhomework.gif)

### 4 - Personally Pinning Messages
Another problem that the students face is that they cannot pin the important messages which they could come back to if they need so. This could be done through the bot as the students could send in the link of the message they would want to pin and the bot would do that. This way all the students could pin the messages personally through the bot. The ppinned messages of other students would not be visible to the current user as we have added the validation of only showing the reminders added by the user not by other students. A little example is provided below.
![$pin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 HW8 reminder](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/pin.gif)

### 5 - Group Creation
Another unique and useful feature of our ClassMateBot is that it helps the students in the process of group making for their projects. Through this feature the bot could help the students to identify other members of the class who have the same requirements and acts as a medium to connect them initially. Afterwards, they can talk to each other in any way possible. This feature is also helpful for times when a person is randomly assigned to a group then the mebers could ask the bot to connect them with the new member and this would not only save time for the students but also, saves effort as many times students do not have their names as their usernames on discord. Through this students can join, leave or connect with others. A little example is provided below. 
![$join HW](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/join.gif)

---


## Installation

1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/War-Keeper/ClassMateBot.git
cd War-Keeper
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip install -r requirements.txt
```
3. Once all the requirements are installed, use the python command to run the ```bot.py``` file.
```
cd src
python3 bot.py 
```

---

## Commands
For the newComer.py file

[$verify command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)

For the voting.py file

[$projects command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Voting/projects.md)

[$vote command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Voting/vote.md)

For the deadline.py file

[$add_homework command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/add_homework.md)

[$change_reminder_due_date command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/change_reminder_due_date.md)

[$clear_all_reminders command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/clear_all_reminders.md)

[$course_due command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/course_due.md)

[$delete_reminder command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/delete_reminder.md)

[$due_this_week command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/due_this_week.md)

[$due_today command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/due_today.md)

[$list_reminders command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/list_reminders.md)

For the pinning.py file

[$pin command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/PinMessage/pin.md)

[$unpin command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/PinMessage/unpin.md)

[$pinnedmessages command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/PinMessage/pinnedmessages.md)

[$updatepin command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/PinMessage/updatepin.md)

For the groups.py file

[$group command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Groups/group.md)

[$join command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Groups/join.md)

[$remove command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Groups/remove.md)


---

## Future Scope

Project 2 and Project 3 user stories and TODO tasks are lockeded in the Projects tab. 

---

## Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/War-Keeper"><img src="https://avatars.githubusercontent.com/u/87688584?v=4" width="75px;" alt=""/><br /><sub><b>Chaitanya Patel</b></sub></a></td>
    <td align="center"><a href="https://github.com/wevanbrown"><img src="https://avatars.githubusercontent.com/u/89553353?v=4" width="75px;" alt=""/><br /><sub><b>Evan Brown</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/kunwarvidhan"><img src="https://avatars.githubusercontent.com/u/51852048?v=4" width="75px;" alt=""/><br /><sub><b>Kunwar Vidhan</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sunil1511"><img src="https://avatars.githubusercontent.com/u/43478410?v=4" width="75px;" alt=""/><br /><sub><b>Sunil Upare</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/salvisumedh2396"><img src="https://avatars.githubusercontent.com/u/72020618?s=96&v=4" width="75px;" alt=""/><br /><sub><b>Sumedh Salvi</b></sub></a><br /></td>
  </tr>
</table>
