# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def __repr__(self):
        return self.name

    def takeItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)
