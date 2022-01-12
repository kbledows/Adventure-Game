# Python Text RPG
# Konrad Bledowski 12-29-2021
from Player import Character
from Item import Item

import time
import cmd
import textwrap
import sys
import os
import random

screen_width = 100
classes = ["wizard", "archer", "knight"]
options = ['play', 'help', 'quit']

player = Character()

#### GAME INSTRUCTIONS + TITLE SCREEN ###


def title_screen_selections():
    option = input("> ")
    if option.lower() in ['play', "p"]:
        start_game()
    elif option.lower() in ["help", "h"]:
        help_menu()
    elif option.lower() in ["quit", "q"]:
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
    print("###################################")
    print("# Welcome to Realm of the Mad God #")
    print("###################################")
    print("Use up, down, left, right to move. ")
    print("Type your commands to use them.  ")
    print("Once in game, 'commands' will bring up your list of commands.")
    print('\n')
    title_screen_selections()
    pass


##### MAP #####
"""
   1   2  3  4  5     #PLAYER STARTS AT [ ]
  ----------------
a |  |  |  |  |  |
  ----------------
b |  |  |  |  |  |
  ----------------
c |  |  |  |  |  |
  ----------------
d |  |  |  |  |  |
  ----------------
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINE = 'examine', 'look'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
                 }

zone_map = {
    'a1': {
        ZONENAME: 'The Nexus',
        DESCRIPTION: 'Hub area in the Realm of the Mad God and a safe zone from enemies.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'a3',
        LEFT: 'a4',
        RIGHT: 'a5'
    },
    'a2': {
        ZONENAME: 'Portal Room',
        DESCRIPTION: 'A glowing portal sits in the center of the room...',
        SOLVED: False,
        UP: '',
        DOWN: 'a1',
        LEFT: '',
        RIGHT: ''
    },
    'a3': {
        ZONENAME: 'The Vault',
        DESCRIPTION: 'A steel enclosed private area, with room to store items, gear, and access the pet yard. There is a soft glow eminating from a nearby fireplace.',
        SOLVED: False,
        UP: 'a1',
        DOWN: '',
        LEFT: '',
        RIGHT: ''
    },
    'a4': {
        ZONENAME: 'The Grand Bazaar',
        DESCRIPTION: 'A beautifully ornate room, large with many shopkeepers stocking various items. A scruffy looking man with a great beard sits behind the counter',
        SOLVED: False,
        UP: '',
        DOWN: 'a3',
        LEFT: '',
        RIGHT: ''
    },
    'a5': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: '',
        DOWN: 'a3',
        LEFT: '',
        RIGHT: ''
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        SOLVED: False,
        UP: '',
        DOWN: 'a3',
        LEFT: '',
        RIGHT: ''
    },

}


def print_map():
    pass


def start_game():
    print("Please enter a name")
    name = input("> ")
    print()
    while True:
        print("Please choose a player class!")
        print("Class options: " + str(classes))
        char_class = input("> ")
        if char_class.lower() not in classes:
            print("Invalid Option")
        else:
            break

    player.set_name(name)
    player.set_class(char_class)
    player.set_location('a1')
    while True:
        prompt()

##### GAME INTERACTIVITY #####


def print_location():
    print('\n' + ('#' * (4 + len(zone_map[player.location][ZONENAME]))))
    print('# ' + zone_map[player.location][ZONENAME] + ' #')
    print(('#' * (4 + len(zone_map[player.location][ZONENAME])) + '\n'))
    print('# ' + zone_map[player.location][DESCRIPTION] + ' #')


def prompt():
    print('\n' + "==========================")
    print('What would you like to do?')
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit',
                          'examine', 'inspect', 'interact', 'look', 'inventory']
    while action.lower() not in acceptable_actions:
        print("Invalid Option! Try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        move()
    elif action.lower() in ['examine', 'interact', 'inspect', 'look']:
        player.examine()


def move():
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        player.set_location(zone_map[player.location][UP])
        print("You have moved to the " + zone_map[player.location][UP])
    elif dest in ['down', 'south']:
        player.set_location(zone_map[player.location][DOWN])
        print("You have moved to the " + zone_map[player.location][DOWN])
    elif dest in ['left', 'west']:
        player.set_location(zone_map[player.location][LEFT])
        print("You have moved to the " + zone_map[player.location][LEFT])
    elif dest in ['right', 'east']:
        player.set_location(zone_map[player.location][RIGHT])
        print("You have moved to the " +
              zone_map[player.location][RIGHT] + '\n')
    print_location()


def examine():
    pass


def main():
    title_screen()


if __name__ == "__main__":
    main()
