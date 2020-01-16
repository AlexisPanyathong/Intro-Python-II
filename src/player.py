# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def __str__(self):
        return("Player's Name: {self.name}")
    def __repr__(self):
        return f"Player({repr(self.name, self.room)})"
    def add_items(self, items):
        if items in self.room.items:
            self.room.items.remove(items)
            self.inventory.append(items)
            items.on_take()
        else:
            print("This item isn't in this room.")