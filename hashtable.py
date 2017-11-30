class HashTable:
    def __init__(self):
        # We are setitng the default size of the map to a numerical value
        self.size = 6

        # The hash map or the hash table is the an array with null values which is
        # the same as the size we pass in
        self.map = [None] * self.size

    def get_index(self, key):
        # We are setting the counter for the hash
        hash = 0

        # For each character in the key increment the hash by its ascii value
        # representation and then return the remainder of that value when divided
        # by the size of the array
        for char in key:
            hash += ord(char)
        index = hash % self.size
        return index

    def add(self, key, value):
        # Gets the index of the key that the user passes in
        key_hash = self.get_index(key)
