# "Treasure chest" game

Simple text game for the pikabu competition.
This is the first public project, 
so the author will be very grateful 
for code-review, comments, remarks etc.

## Dependencies:
 
You might need to install Python 3 (https://www.python.org/) 
before using the game.
 
 ## Running the game:

The first step is to clone the repository locally.

```
$ git clone https://github.com/ProtKsen/pgame.git
``` 
Open a console and "cd" to the game directory and run:

```
$ python main.py
```

## Game process:
This is a text game, the main goal is to collect as 
many game points (coins) as possible. \
\
There are 10 islands with treasures. To get the treasures 
you should hire a pirates team and sail sequentially from 
one island to another, overcoming traps. Each island has 
its own trap, for avoiding which your team should have
certain skill points of logic (L), power (P), and agility (A). 
The island number (N) is equal to the sum of the required 
points: L + P + A = N. For example, the 5th island could have 
such trap requirements:\
L = 5, P = 0, A = 0 \
L = 1, P = 4, A = 0 \
L = 2, P = 1, A = 2 \
and other similar.\
\
On each turn, you can go to the oracle. For a certain 
number of coins, the oracle can predict how many and 
what skill points you need on the next island. After that, 
you should go to the tavern where you can hire some pirates. 
Each pirate has his own number of skill points. You can 
hire as many pirates as you need. After that, go to the 
island and try to get the treasure.\
\
The game ends either when you spend all the money (losing), 
or when you take the treasures from all 10 islands (winning).

