from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['sword']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['knife']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['bat']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def try_direction(direction, currentRoom):
    attribute = direction + '_to'

    if hasattr(currentRoom, attribute):
        newRoom = getattr(currentRoom, attribute)
        return newRoom
    else:
        print('\nCan not go this way!!!')
        return currentRoom


userName = input('What is your name? ')
player = Player(userName, room['outside'])

print(f'Hello {userName}! Let\'s go on an adventure!')

userInput = ''

while not userInput == 'q':
    # newRoom = ''
    print(player.currentRoom)
    userInput = input('Which way do you want to do or go?\n'
                      'Directions: [n] North [s] South [e] East [w] West\n'
                      'Items: take (item) or drop (item)\n'
                      'or [q] Quit:\n')

    if userInput == 'n'\
            or userInput == 's'\
            or userInput == 'e'\
            or userInput == 'w':

        player.currentRoom = try_direction(userInput, player.currentRoom)

    elif 'take' in userInput or 'drop' in userInput:
        print('yep')

    elif userInput == 'q':
        print('Thanks for playing!!!')

    else:
        print('Incorrect input. Please use n, e, s, or w')


"""
Previous work before lecture.
Now has been refactored above.
"""

# currentRoom = room['outside']


# userName = input('What is your name? ')
# player = Player(userName)

# print(f'Hello {userName}! Let\'s go on an adventure!')

# userInput = ''

# while not userInput == 'q':
#     newRoom = ''
#     print(currentRoom)
#     userInput = input('Which way do you want to do or go?\n'
#                       'Directions: [n] North [s] South [e] East [w] West\n'
#                       'Items: take (item) or drop (item)\n'
#                       'or [q] Quit:\n')

#     if userInput == 'n'\
#             or userInput == 's'\
#             or userInput == 'e'\
#             or userInput == 'w'\
#             or userInput == 'q':

#           # try:
#             if userInput == 'n':
#                newRoom = currentRoom.n_to
#          elif userInput == 'e':
#               newRoom = currentRoom.e_to
#           elif userInput == 's':
#              newRoom = currentRoom.s_to
#          elif userInput == 'w':
#                 newRoom = currentRoom.w_to
#        except AttributeError:
#          print('\nCan not go this way!!! \n')

#       if newRoom:
#            currentRoom = newRoom
