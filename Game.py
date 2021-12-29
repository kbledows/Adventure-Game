#Python Text RPG
#Konrad Bledowski 12-29-2021
from Player import Character
from Item import Item

import time
import cmd
import textwrap
import sys
import os
import random

screen_width = 100
classes = ["wizard","archer","knight"]
options = ['play','help','quit']

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #placeholder
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in options:
        print("Invalid Option!")
        print("Choose from " + str(options))
        title_screen_selections()

def title_screen():
    os.system('clear')
    print("###################################")
    print("# Welcome to Realm of the Mad God #")
    print("###################################")
    print("             -- Play --            ")
    print("             -- Help --            ")
    print("             -- Quit --            ")
    print("")
    title_screen_selections()


def help_menu():
    pass

def start_game():
    print("Please enter a name")
    name = input("> ")
    while True:
        print("Please choose a player class!")
        print("Class options: " + str(classes))
        player_class = input("> ").lower()
        if player_class not in classes:
            print("Invalid Option")
        else:
            break

    p = Character(name,player_class)


def main():
    title_screen()

if __name__ == "__main__":
	main()
