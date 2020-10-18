# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:07:40 2020

@author: Legedith
"""
import os
import sys
from platform import system

from time import sleep

import ascii_images

path = os.getcwd()

def banner(string):
    operating_system = system().lower()
    if operating_system == "linux" or operating_system == "linux2":
        os.system("figlet -c string")
    else:
        print("\t\t" + string)


def game():

    ascii_images.ascii_castle()

    banner("DUNGEONS")
    print("\t\tI welcome thee to an adventure like none other.")
    sleep(1)
    name = input("\t\tWhat shall I call you great Hero: ")
    sleep(1)
    print("\t\tWelcome "+name+".  You have been chosen as the defender of all magical creatures.")
    sleep(1)
    print("\t\tYour journey will take you through mysterious places, ")
    print("\t\tThis is one dark journey and you may need to take help from somebody")
    print("\t\tYou will get one chance to ask for help from the greedy wizard. Remember, he is not your friend and you will have to pay him")
    sleep(1)
    opt = ''
    while opt not in ['y', 'yes']:
        opt = input("\t\tAre you ready to begin your adventure? (y/n): ").lower()
        if opt == 'n' or opt == 'no':
            print("\n\n\t\tSo long and thanks for all the fish!")
            exit(0)

    print("\n\n\n\t\tWe shall begin Mighty warrior!")
    dungeons()

def dungeons():
    place = 'dungeons'
    sleep(1)
    print('\n\n\n')
    print("\t\t\tDUNGEONS")
    print("\t\t---------------------------")
    print("\t\tSelect a training class:")
    print("\t\t1. I wanna learn everything from basics")
    print("\t\t2. I wanna learn the good stuff")
    print("\t\t3. Teach me the Dark Arts!")
    print()
    sleep(1)
    num = input("\t\tEnter a number:")
    print('\n\n\n\n\n')
    if num == '1':
        banner("SPELL CLASS")
        print("\n\n\t\tYou are in a dark room.")
        print()
        print("\t\tYou can use the 'ls' command in the game as well")
        print("\t\tas on a linux system to look around the directory/location.")

        print()
        print("\t\tYou can use the 'cat <scroll/filename>' command in the game as well")
        print("\t\tas on a linux system to read the contents of a scroll(file).")
        os.system("touch metal_bars.dragon scroll_of_knowledge.dragon broken_bones.dragon dead_rats.dragon a_locked_door.dragon")
        os.system('printf "\t\tDoor is locked! Try reading the scroll_of_knowledge" > a_locked_door.dragon')
        os.system('printf "\t\tWhat can you catch but never throw?" > scroll_of_knowledge.dragon')
        while True:
            opt = input("\t\tInput:").lower()
            if opt == 'cold':
                print("\t\tCold it is! Just like your movement inside this cell. ")
                print("\t\tRead the Scrool of Cold Movement! (Did you not see the scroll before?)")
                os.system('touch scroll_of_cold_movement.dragon')
                os.system('printf "             You can use the cd <roomname/directory_name> command to move through rooms\n \
             in the game and directories in the terminal.\n \
             Enter the new room the has appeared!\n             (Only files have the extension .dragon)" > scroll_of_cold_movement.dragon')
                os.system('mkdir alley')
                os.system('touch alley/empty_alley.dragon')
            elif opt == 'cd alley':
                os.chdir('alley')
                print('\n\n\n')
                banner("ALLEY")
                sleep(1)
                print("\t\tYou entered an abandoned Alley.")
                sleep(1)
                place = 'alley'
                break
            else:
                os.system(opt)
            print()

        if place == 'alley':
            alley()

    elif num == '2':
        banner("ARCHERY")
        os.system('mkdir archery')
        os.chdir('archery')
        print("\n\n\t\tSometimes you need a little more precission.")
        print()
        print("\t\tYou can use the cat command to view multiple files at once.")
        print("\t\tYou can write 'cat <file1> <file2> <file2>")
        print("\t\tAnd the contents of three files will be concatinated.")
        sleep(2)
        print("\t\tYou can see that the current folder contains a number of files.")
        print("\t\tWith names riddleA, riddleB, riddleC and so on....")
        print("\t\tEach file contains just a single letter of the riddle.")
        sleep(1)
        print("\t\tTo view all the files, you can use */? operator.")
        for i,j in enumerate("What is at the end of rainbow?"):
            os.system('echo '+j+' > riddle'+chr(i+65)+'.dragon')
        opt = ''
        cpMoney = "cp money.dragon"
        mvMoney = "mv money.dragon"
        while True:
            opt = input("\t\tInput:").lower()

            if opt == 'w':
                os.system('rm *.dragon')
                print("\t\tYou hit that target spot on!")
                print("\t\tAll the following commands would have worked:")
                print("\t\tcat *")
                print("\t\tcat riddle?.dragon")
                print("\t\tcat riddle*")
                print('\n\n\n')
                print("\t\tOh no, a vicious dragon just appeared to end your journey")
                print("\t\tThis is your chance to take help from the wizard")
                print("\t\tBut he demands double the money you have right now\n")
                print("\t\tTo copy a file with the \"cp\" command, pass the name of the file to be copied and then the destination")
                print("\t\tYou have money in the file money.dragon,read the file contents and copy it using cp command to double your money")
                print("\t\tYou can write `cp fileToBeCopied duplicateFileName`")
                os.system('echo 100 Gold Coins'+' > money.dragon')
            if opt != cpMoney and cpMoney in opt:
                os.system("ls")
                print("\t\tYou have successfully doubled your money, the wizard teleported you to another world (directory)")
                os.system("mkdir safeChamber")
                os.system("cp money.dragon safeChamber")
                os.chdir("safeChamber")
                print("\t\tWith a new skill (command) called `mv`, you can move your files to another world (directory)")
                print("\t\tSo next time you want to teleport to a new world you can take your files with you")
                print("\t\tTo move a file into a directory using the `mv` command, pass the name of the file and then the directory")
                print("\t\tYou can write `mv fileToBeMoved newDirectory`")
            if mvMoney in opt and opt!=mvMoney:
                print('\n\n\n')
                print("\t\tYou have successfully moved the file money.dragon to a new world (directory)")
                print("\t\tinput `dungeons` at any time to return to dungeons")
                king()
            if opt == "dungeons":
                print('\n\n\n')
                print('See you at your next Training!')
                dungeons()
            else:
                os.system(opt)
            print()
    elif num == '3':
        print("This tale is to be continued!")


def alley():
    place = 'alley'
    ascii_images.ascii_dragon()
    print("\t\tYou have answer a riddle to go to the next room.")
    sleep(1)
    print("\t\tAnswer wrong and the dragon would eat you!!! JK, or am I?")
    sleep(1)
    print("\t\tWhat disappears as soon as  you say its name    ")
    ans = ''
    while True:
        ans =  input("\t\tInput:").lower()
        if ans == 'silence':
            print('\t\tA new path appeared. Go to THE GREAT HALL!')
            sleep(1)
            print("\t\tUse cd command to go to the The Great Hall!")
            os.system('mkdir the_great_hall')
            sleep(1)

        elif ans == 'cd the_great_hall':
            os.chdir('the_great_hall')
            print('\n\n\n')
            banner("THE GREAT HALL")
            sleep(1)
            place = 'hall'
            break

        else:
            os.system(ans)
        print()

    if place == 'hall':
        hall()

def hall():
    sleep(2)
    ascii_images.ascii_hall()
    print('             Try to read scroll in The Great Hall to unlock the path!')
    os.system('touch the_great_hall.dragon')
    os.system('printf "             What goes up, but never comes down? " > the_great_hall.dragon')
    ans1 = ''
    while True:
        ans1 = input("\t\tInput:").lower()
        if ans1 == 'age':
            print('\t\tA new path appeared.')
            sleep(1)
            print("\t\tUse cd command to go to the kitchen! ")
            os.system('mkdir the_royal_kitchen')

        elif ans1 == 'cd the_royal_kitchen':
            os.chdir('the_royal_kitchen')
            print('\n\n\n')
            banner("THE ROYAL KICHEN")
            sleep(1)
            place = 'kitchen'
            break

        else:
            os.system(ans1)
        print()

    if place == 'kitchen':
        kitchen()

def kitchen():
    sleep(2)
    ascii_iamges.ascii_couldron()
    print("\t\tTry to read kitchen.dragon")
    os.system('touch kitchen.dragon')
    os.system('printf "             What is easy to get into, but hard to get out of ? " > kitchen.dragon')
    ans2 = ''
    while True:
        ans2 = input("\t\tInput:").lower()
        if ans2 == 'trouble' or ans2 == 'vim' or ans2 == 'realtionship':
            print("\t\tA new path appeared.")
            sleep(1)
            print("\t\tUse cd command to go to the library!")
            os.system('mkdir infinite_library')

        elif ans2 == 'cd infinite_library':
            os.chdir('infinite_library')
            print('\n\n\n')
            banner("INFINITE LIBRARY")
            sleep(1)
            place = 'library'
            break

        else:
            os.system(ans2)
        print()

    if place == 'library':
        library()

def library():
    ascii_images.ascii_scrolls()
    place = 'library'
    print("\t\tYou have reached the Infinite Library!")
    sleep(1)
    print("\t\tI wonder if you remember the path you followed to come here...")
    sleep(1)
    print("\t\tYou can use the \'pwd\' command to know your location in dungeon\n \
             as well as in the linux system.")
    sleep(1)
    print("\t\tpwd stands for present workng directory")
    sleep(1)
    print("\t\tand shows you the name as well as the location of your current directory.")
    print("\t\t---------------------------------------------")
    opt = ''
    while True:
        sleep(1)
        opt = input("\t\tTry it: ")
        if opt == 'pwd':
            os.system('pwd')
            print()
            print("\t\tTo go back to a previous room (directory),")
            sleep(1)
            print("\t\tyou can use the 'cd ..' command")
            sleep(1)
            print("\t\tTo go back to multiple directories,")
            sleep(1)
            print("\t\tyou can use the 'cd ../../..' command")
            sleep(1)
            print("\t\tfor example 'cd ../../../..' would take you back to Dungeons")

        elif opt == 'cd ../../../..':
            place = 'dungeons'
            print("Taking you back to Dungeons\n\n\n\n\n")
            break
        else:
            print("\t\tWrong spell\n")

    if place == 'dungeons':
        dungeons()

def king():
    banner("POISON")
    print("\t\tYou were just poisoned. You no longer remember who you are.")
    sleep(0.5)
    print("\t\tTry reading the scroll in the room. ")
    os.system('touch king_riddle.dragon')
    os.system('printf " Two bodies have I, though both joined in one. The more still I stand, the quicker I run." > king_riddle.dragon ')
    res_1 = ''
    while 1:
        res_1 = input("             Input:").lower()
        if res_1 == 'hourglass':
            print("Use 'whoami' command in game as well as in linux system to know your identity.")
        elif res_1 == 'whoami':
            os.system(res_1)
            print()
            print("\t\tTime to move on to next task!\n\n\n")
            touch()
        else:
            os.system(res_1)
        print()

def touch():
    banner("SUMMONING")
    #os.system('mkdir door')
    os.system(' touch riddle.dragon')
    os.system('printf " First think of the person who lives in disguise,\n \
                        Who deals in secrets and tells naught but lies.\n \
                        Next, tell me what’s always the last thing to mend,\n \
                        The middle of middle and end of the end?\n \
    		    And finally give me the sound often heard\n \
    		    During the search for a hard-to-find word.\n \
     		    Now string them together, and answer me this,\n \
    		    Which creature would you be unwilling to kiss??" > riddle.dragon')

    print("\t\tYour next task is to master the summoning spell.")
    print("\t\tYou can create forge new items (files) using the 'touch' command")
    print("\t\tFor example you can write 'touch sword.dragon' to create a sword file with extension dragon.")
    sleep(1)
    print("\t\tSolve the riddle in the scroll and create a dragon file using the answer.")
    opt = ''
    while True:
        opt = input("\t\tInput:").lower()
        os.system(opt)
        if 'escape' in os.listdir():
            print("\t\tYou found a way out, It teleported you back to the dungeons\n\n\n")
            dungeons()

        elif 'spider.dragon' in os.listdir():
            print("\t\tYou created a spider!!!")
            print("\t\tNow you have to eescape from the spider....")
            print("\t\tUse 'mkdir <directory_name>' command to create a new directory named escape")



# def previous_moves():
#     print('Do you want to know what were your previous moves?')
#     print('try to open moves_riddle ')
#     os.system('touch moves_riddle.dragon')
#     os.system('printf " I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?  " > moves_riddle.dragon')
#     res_2 = ''
#     while 1:
#         res_2 = input("             Input:").lower()
#         if res_2 == 'echo':
#             print("Use 'history' command  in game as well as in the linux system to see your previous commands")

#         elif res_2 == 'history':
#             os.system(res_2)
#             print()
#             print("             Time to go back to Dungeons!\n\n\n")
#             dungeons()

#         else:
#             os.system(res_2)
#         print()


try:
    game()

except KeyboardInterrupt:
    os.chdir(path)
    os.system('rm *.dragon')
    os.system('rm -rd alley')
    os.system('rm -rd archery')
    banner("FAREWELL")
    exit()


# change cd command frfom chdir to system
