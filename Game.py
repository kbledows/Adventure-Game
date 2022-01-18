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

ZONENAME = 'zonename'
DESCRIPTION = 'description'
ITEMS = 'items'
EXAMINE = 'examine', 'look'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
NPC = 'npc'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
                 }

zone_map = {
    'a1': {
        ZONENAME: 'The Nexus',
        DESCRIPTION: 'Hub area in the Realm of the Mad God and a safe zone from enemies.',
        ITEMS: ['sword', 'shield'],
        SOLVED: False,
        UP: 'a2',
        DOWN: 'a3',
        LEFT: 'a4',
        RIGHT: 'a5',
        NPC: ''
    },
    'a2': {
        ZONENAME: 'Portal Room',
        DESCRIPTION: 'A glowing portal sits in the center of the room...',
        ITEMS: [],
        SOLVED: False,
        UP: 'b1',
        DOWN: 'a1',
        LEFT: '',
        RIGHT: '',
        NPC: ''
    },
    'a3': {
        ZONENAME: 'The Vault',
        DESCRIPTION: 'A steel enclosed private area, with room to store items, gear, and access the pet yard. There is a soft glow eminating from a nearby fireplace.',
        ITEMS: [],
        SOLVED: False,
        UP: 'a1',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
        NPC: ''
    },
    'a4': {
        ZONENAME: 'The Grand Bazaar',
        DESCRIPTION: 'A beautifully ornate room, large with many shopkeepers stocking various items. A scruffy looking man with a great beard sits behind the counter',
        ITEMS: [],
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: 'a1',
        NPC: ''
    },
    'a5': {
        ZONENAME: 'Quest Room',
        DESCRIPTION: 'A shoddy home, built of mud and brick.',
        ITEMS: [],
        SOLVED: False,
        UP: '',
        DOWN: 'a3',
        LEFT: '',
        RIGHT: '',
        NPC: 'Tinkerer'
    },
    'b1': {
        ZONENAME: 'Beach',
        DESCRIPTION: 'The shoreline, or shore, is the narrow area that makes up the outer edge of a realm. The shore area generally features sand with no vegetation and shallow water that eventually reaches the uncrossable deep waters of the ocean. Enemies found here are generally considered the least threatening.',
        ITEMS: [],
        SOLVED: False,
        UP: '',
        DOWN: 'a2',
        LEFT: '',
        RIGHT: '',
        NPC: ''
    },

}


def print_map():
    pass


##### GAME INTERACTIVITY #####


def print_location():
    print('\n' + ('#' * (4 + len(zone_map[player.location][ZONENAME]))))
    print('# ' + zone_map[player.location][ZONENAME] + ' #')
    print(('#' * (4 + len(zone_map[player.location][ZONENAME])) + '\n'))
    print('# ' + zone_map[player.location][DESCRIPTION] + ' #')
    print("===================================================")
    if zone_map[player.location][NPC] != '':
        type_out("There is an NPC here! type 'talk' to speak with them.")
    if zone_map[player.location][ITEMS] != []:
        type_out("There appear to be some items scattered about here.")


def prompt():
    print("===================================================")
    question1 = 'What would you like to do?'
    type_out(question1)
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit',
                          'examine', 'inspect', 'interact', 'look', 'inventory', 'commands', 'help', 'take', 'grab', 'pickup', 'pick up', 'move down', 'down', 'south', 'move up', 'north', 'up', 'move left', 'left', 'west', 'east', 'move right', 'right', 'talk']
    while action.lower() not in acceptable_actions:
        print("Invalid Option! Try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        if player.state != 'normal':
            print("You can't do that right now!")
        else:
            move()
    elif action.lower() in ['examine', 'interact', 'inspect', 'look']:
        examine()
    elif action.lower() in ['take', 'grab', 'pickup', 'pick up']:
        take()
    elif action.lower() in ['commands', 'help']:
        commands()
    elif action.lower() in ['move up', 'up', 'north']:
        moveUp()
    elif action.lower() in ['move down', 'down', 'south']:
        moveDown()
    elif action.lower() in ['move right', 'right', 'east']:
        moveRight()
    elif action.lower() in ['move left', 'west', 'left']:
        moveLeft()


def move():
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    while dest not in ['up', 'north', 'down', 'south', 'right', 'east', 'left', 'west']:
        print("Invalid Direction!\n")
        dest = input(ask)
    if dest in ['up', 'north']:
        moveUp()
    elif dest in ['down', 'south']:
        moveDown()
    elif dest in ['left', 'west']:
        moveLeft()
    elif dest in ['right', 'east']:
        moveRight()


def moveUp():
    if zone_map[player.location][UP] == '':
        print("Cannot move there.")
    else:
        player.set_location(zone_map[player.location][UP])
        print("You have moved to the " + zone_map[player.location][ZONENAME])
        print_location()


def moveDown():
    if zone_map[player.location][DOWN] == '':
        print("Cannot move there.")
    else:
        player.set_location(zone_map[player.location][DOWN])
        print("You have moved to the " + zone_map[player.location][ZONENAME])
        print_location()


def moveLeft():
    if zone_map[player.location][LEFT] == '':
        print("Cannot move there.")
    else:
        player.set_location(zone_map[player.location][LEFT])
        print("You have moved to the " + zone_map[player.location][ZONENAME])
        print_location()


def moveRight():
    if zone_map[player.location][RIGHT] == '':
        print("Cannot move there.")
    else:
        player.set_location(zone_map[player.location][RIGHT])
        print("You have moved to the " + zone_map[player.location][ZONENAME])
        print_location()


def examine():
    if zone_map[player.location][SOLVED]:
        print("There's nothing else here...")
    else:
        print("You can trigger a puzzle here")


def take():
    if zone_map[player.location][ITEMS] == []:
        print("There's nothing here for you to take!\n")
    else:
        print("What would you like to take?")
        take = input("> ")
        while take not in zone_map[player.location][ITEMS]:
            print("That item is not here...")
            take = input("> ")
        player.inventory.append(take)
        zone_map[player.location][ITEMS].remove(take)
        print("Picked up, a " + take)
        print(player.inventory)
        print(zone_map[player.location][ITEMS])


def talk():
    if zone_map[player.location][NPC] == []:
        print("There's no one here for you to talk with!\n")
    else:
        if zone_map[player.location][NPC] == 'kreg':
            shop()


def commands():
    print()
    travel_commands = ['move', 'go', 'travel',
                       'walk', 'up', 'left', 'right', 'down']
    examine_commands = ['examine', 'inspect', 'interact', 'look']
    other_commands = ['talk', 'inventory']
    q1 = "Here is a list of viable commands in the game world."
    type_out(q1)
    print("====================================")
    print("Travel commands: " + str(travel_commands))
    print("Examine commands: " + str(examine_commands))
    print("Other commands: " + str(other_commands))
    print("====================================")
    q2 = "And finally, remember you may always exit the program by typing 'quit'"
    type_out(q2)


def talk():
    pass


def drop():
    if player.inventory == []:
        print("You have no items in your inventory!")
    pass


def shop():
    print("Welcome to Kreg's store!")

#### MAIN GAMEPLAY LOOP ####


def type_out(phrase):
    for character in phrase:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def start_game():
    os.system('clear')
    question1 = "What is your name?\n"
    type_out(question1)

    name = input("> ")
    print()
    question2 = "Please choose a player class!"
    type_out(question2)
    question3 = "You can play as a Knight, Wizard, or Archer."
    type_out(question3)
    char_class = input("> ")
    while char_class.lower() not in classes:
        print("Invalid Option")
        char_class = input("> ")

    player.set_name(name)
    player.set_class(char_class)
    player.set_location('a1')
    if player.char_class == 'knight':
        player.set_hp(500)
        player.set_max_hp(800)
    elif player.char_class == 'wizard':
        player.set_hp(400)
        player.set_max_hp(700)
    elif player.char_class == 'archer':
        player.set_hp(450)
        player.set_max_hp(750)
    print_location()
    core_loop()


def core_loop():
    playing = True
    while playing:
        print_map()
        prompt()
    game_over()


def game_over():
    print("Congratulations! You beaten the game!")
    print("Total Score: n/a")
    print("Mobs killed: n/a")
    time.sleep(2)
    title_screen()


def main():
    title_screen()


if __name__ == "__main__":
    main()
