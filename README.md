<p align="center"><img width=20.5% src="https://github.com/War-Keeper/ClassMateBot/blob/main/data/neworange.png"></p>
<p align="center"><img width=60% src="https://github.com/War-Keeper/ClassMateBot/blob/main/data/bot.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-yellow.svg)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5539956.svg)](https://doi.org/10.5281/zenodo.5539956)
![Build Status](https://github.com/War-Keeper/ClassMateBot/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/War-Keeper/ClassMateBot/branch/main/graph/badge.svg)](https://codecov.io/gh/War-Keeper/ClassMateBot)

<p align="center">
  <a href="#basic-overview">Basic Overview</a>
  ::
  <a href="#description">Description</a>
  ::
  <a href="#examples"> Examples </a>
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
One of the necessary condition of joining a discord channel should be that the user is a part of the class or group that they are joining. To check this we have added an extra layer of protection by verifying that the new joining user is a student of this class and that they are authorized to join the group. To do this we first assign the non-verified role to the new comer and then ask them to verify them using $verify command. If that goes through the member is assigned a student role and has full access to the server resources. A little example is provided below.
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

## Commands
For the newComer.py file

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
