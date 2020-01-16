from room import Room
from player import Player
from item import Item

# Items
items = {
    'sword':    Item("sword",
                     "Dull sword."),
    'potion':   Item("potion",
                     "Health potion."),
    'book':     Item("book",
                     "Old weathered book."),
    'backpack': Item("backpack",
                     "Small backpack with rope."),
    'bag':      Item("bag",
                     "Small bag filled with 10 gold coins."),
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["bag"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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
player_name = input("Enter a Player's Name: ")
player = Player(player_name, room["outside"])
print(f"Awesome! Hello: {player_name}")
# Write a loop that:
while True:
# * Prints the current room name
    print(f"{player.room}, {player.room.description}")
# * Prints the current description (the textwrap module might be useful here).
    print(f"\n{player.room}, {player.room.description}")
    for item in player.room.items:
        print(f"\nItems in current room: {item.i_name}")
        print("\n")
# * Waits for user input and decides what to do.
    move = input("Enter a direction(n, s, e, w)>> ")
# If the user enters a cardinal direction, attempt to move to the room there.
    if len(move) == 1:
        try:
            if move == 'get {item.i_name}':
                player.inventory = player.add_items
            if move == 'n':
                player.room = player.room.n_to
            elif move == 's':
                player.room = player.room.s_to
            elif move == 'e':
                player.room.e_to
            elif move == 'w':
                player.room.w_to
                
            
# Print an error message if the movement isn't allowed.
        except:
            print("Error, this movement isn't allowed. Please try again.")
            
    
# If the user enters "q", quit the game.
    elif move == 'q':
        print("Thank you for playing, see you later!")
        break
    
    if len(move) >= 2:
        print("get {item.i_name}")
        try:
            if move == f'get {item.i_name}': 
                player.add_items(items)
            if move == f'drop {item.i_name}':
                player.drop_items(item)
        except:
            print("Please enter '\get <item name>\' to add an item to your inventory OR drop \<item name>\ to remove an item.")