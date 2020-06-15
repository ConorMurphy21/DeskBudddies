# Desk Buddies
A simple TCP server-client application for scheduling 
employees in a way that maintains social distancing.

# Overview
As we move back towards working in person, some things can't go back to the way they were. One of those things 
is sitting right next to your coworkers. This has never been a problem before so figuring out how to schedule
who can go in without putting people at risk can be hard. This program aims to solve this.  
To achieve this we keep track of 2 things.
1. Who sits next to each other (or too close for company)
2. who wants to work when

To keep track of who sits next to each other we request that you (the administrator) upload an adjacency file 
(more on this below). To keep track of who's working we listen for requests from employees and schedule them
on a first come first serve basis. If a request to work fails due to one of your desk buddies wishing to work
that same day, we provide you with their name. This way if you believe your attendance is required you can
have a discussion with your coworker to figure it out.

# Security
I want to be very clear, that this program is **not secure**. This shouldn't be a problem because we don't store
any personal data (besides userId's and when they work), but if you are worried about this information being in
someone else's hands then this is not the app for you. There is also no authentication so if a coworker wanted they
could mess with the schedule however they please. I would hope that your employees can be trusted not to this but who
knows.

# Installation

Install python 3.5+ if you do not have it already.  
`pip install Desk-Buddies`  
If you have both python 2 and 3 installed:  
`pip3 install Desk-Buddies`  

# Setup

For your group of desk buddies you will need to have 1 person running the server, and the remaining 
using the client interface. If you're workplace is not using a vpn to connect to a lan, you will have 
to configure your server using port forwarding. This process is well documented by gamers creating
Minecraft servers and shouldn't be too hard.

## Server setup

Setting up the server is very easy. The only thing necessary to start the server is an adjacency file.
The adjacency file must follow the format below, and to import the file into the server use the import flag.
The file will be copied into deskBuddies, so if any changes are made to the file you will need to re-import the file.

#### Adjacency File

Currently the only adjacency file is an adjacency matrix in the form of a csv. Support for adjacency lists,
and other file types is possibly in the works. Here is an example of an adjacency matrix:

|        | Jen | Conor | Dakota |
|--------|-----|-------|--------|
| Jen    | 0   | 1     | yes    |
| Conor  |     | 0     |        |
| Dakota | x   |       |  0     |

Important things to note:
* The row headers and column headers are the same
* The userId's (headers) are unique
* empty, '0', 'false', or 'no' means the column header and row header are not sitting together
* anything else means the column header and row header
* If there is a true value in either (a,b) or (b,a) it will be treated as true. (eg Conor & Jen)

The recommended way to create this document, is by making a shared google sheet, or excel sheet, and request
that your employees fill in who their neighbours are.

## Client setup
The client only needs to know 2 things.
1. The IP address or hostname of the server
2. Their own userId

### User Id's
UserId's can be whatever is easiest. If your floor is small it could be your first names. You could use
first and last names, nicknames, employeeId's or emails. Just keep in mind a few things. the userId
that the employee uses needs to match the userId that is listed in the adjacency file. It is also what is returned
from queries, so try to keep something that can identify the employee (ie avoid numbers).


# Config Items
#### Client Config Items

| Name  | Type | Default | Description |
|--------|-----|-------|--------|
| uid    | str   | ''  | userId of user |
| host   | str   | ''  | IP address or hostname of server|
| port   | int   | 6719| port the server listens on      |

#### Server Config Items

| Name  | Type | Default | Description |
|--------|-----|-------|--------|
| port   | int   | 6719| port the server listens on      |
|enableForce | bool | False | enable users to use the force flag |

# Command Line Interface
```
usage: commandLineEntryPoint.py [-h] [--serve] [--request] [-f] [-r] [-g] [-w]
                                [--config] [--servcfg] [-i ADJACENCY]
                                [--date DATE] [--day DAY]

Communicate who can come into the office while maintaining social distancing

optional arguments:
  -h, --help            show this help message and exit
  --serve               Run a DeskBuddies server [action]
  --request             Request to work (Requires date or day) [default
                        action]
  -f, --force           Force request to go through without safety checks
  -r, --remove          Remove request to work (Requires date or day) [action]
  -g, --get             Request schedule (Requires date or day) [action]
  -w, --week            Request a week of schedule (get modifier)
  --config              Update client configuration properties [action]
  --servcfg             Update server configuration properties [action]
  -i ADJACENCY, --import ADJACENCY
                        Import given adjacency file
  --date DATE           Calendar date in the form dd/mm, (format is
                        configurable)
  --day DAY             Weekday (full or abbreviated)

Process finished with exit code 0

```

### Examples
Start server: `DeskBuddies --serve`  
Request to work: `DeskBuddies --day Monday` or equivalently `DeskBuddies -q --day Mon`  
Remove request to work: `DeskBuddies -r --day Tues`  
Find out who's working: `DeskBuddies -g --day Thurs`    
Find out who's working this week: `DeskBuddies -g --day Monday -w`

