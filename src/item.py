class Item:
    def __init__(self, i_name, i_description):
        self.i_name = i_name
        self.i_description = i_description
    def __repr__(self):
        return f"{self.i_name}, {self.i_description}"
    
    
# Add an `on_take` method to `Item`.
#   Call this method when the `Item` is picked up by the player.
#   `on_take` should print out "You have picked up [NAME]" when you pick up an item.
#   The `Item` can use this to run additional code when it is picked up.
    def on_take(self):
        print(f'You have picked up a {self.i_name}, {self.i_description}.')

# Add an `on_drop` method to `Item`. Implement it similar to `on_take`.
    def on_drop(self):
        print(f'You have dropped {self.i_name}.')