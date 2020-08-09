# Dungeons

## Inspiration
A majority of schools around the world use **Windows** as their primary operating system. 

It makes it particularly uncomfortable for students and hackers to shift to a **Linux** based system where they have to interact with terminal regularly.

 To make the transition easier and fun and to get more people to shift to an open source OS,
 we made 
 
**Dungeons: a text based adventure game** 

that'll teach you basic Linux commands such as
 + ls
 + cat
 +  mv
 +  cp
 +  cd
 +  pwd
 +  mkdir
 +  rm
 +  rmdir
 +  touch
 + And many many more 

## What it does
It takes you on an adventure like no other. It'll automatically create files and folders as you move through the game. 

The best part is once you are done playing, it'll automatically cleanup all the files created.
#### You'll have to:
+ Navigate through rooms (Directories)
+ Move the treasure (files) around
+  Fight monsters
+ Answer riddles
+ Practice fighting skills,
+ Find hidden passages 
+ Summon objects

To move around the game and to complete your tasks, you'll have to use one or multiple Linux commands. 


The game's full of beautiful ASCII art, Harry Potter and D&D references. 

Some riddles are hard, some have multiple answers.

My favorite is:  _What is easy to get into, but hard to get out of ?_

You can answer with: trouble or vim.

**P.s. It was just a joke... It's not hard, it's impossible to get out of vim**

## How we built it
The whole game was written in python using the **os** module for all file and directory manipulation. 

For all the banners, we passed figlet commands through os.system function. 

We used an online ASCII art generator to make all the artwork. 
## Challenges we ran into
It was difficult pipelining user inputs to the terminal through the game in such a way that it would still look neat. 

Styling the output to look consistent with old text-based adventure games was surely a challenge.
## Accomplishments that we're proud of
We absolutely love how the file and directory manipulation part turned out to be. We can create any folder structure from the game, keep track of those created by user to check if they got the answers correct and clean all the files and folders afterwards.

## What we learned
We learnt a lot of Linux commands, played a lot of text-based adventure games, learnt file manipulation and a ton of cool Linux terminal tricks.

## What's next for Dungeons
We plan to add a lot more commands in the future.
