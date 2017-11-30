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
        key_index = self.get_index(key)

        # Since we are using lists we are constructing a list that is a key value pair
        key_value = [key, value]

        # First we have to see if what the user is trying to add even exists and if it doesnt then at that index
        # that we have gotten from the key index variable that we update the value at that index with that list comprised
        # of the key value pair
        if self.map[key_index] is None:
            # This is checking if there any values even in that bucket and the way that it is doing that is oddly enough
            # even though the user is trying to find the specific key when we get and come across that index we are
            # presented with all the values instead so this is checking if there are even any values in that index and if
            # there is not you wouldn't be appending to anything you just construct a new list
            self.map[key_index] = list([key_value])
            return 'The index at the key was non existent therefore a new list was added comprised of the key value pair'

        # Now we are checking if the value does exist at that index we are going to want to update the value at that key
        else:
            # We are accessing the list at that index the key value pair in that list
            for pair in self.map[key_index]:
                # Now that we are checking if the key does actually match what we are looking for but you are probably
                # wondering dont we know that already but in the case that there was a collision we can have mulitple
                # lists in once bucket therefore this confirms if we are in the right list in the bucket
                if pair[0] == key:

                    # Then update the value
                    pair[1] = value
                    return True
            # And if the key that the user is trying to append is a key that we can not find in the list we then append the key value pair
            # but keep in mind we are actually at a state where we can confirm that the reason we append and not not just contstruct a new
            # list like in the if block is due to the reason that we there are actual value present at that index therefore to avoid
            # collisions we simply append another list to that bucket
            self.map[key_index].append(key_value)

    def get(self, key):
        # When the user passes in a key we want to be able to find the value associated with that key
        key_value = self.get_index(key)

        # If there are actually values at this index of the key that the user is passing in
        if self.map[key_value] is not None:

            # Since we know there are values however we dont know how many iterate through the bukets at that given index
            for pair in self.map[key_value]:
                # If that key which is that first element in the list is equal to the key that the user passes in
                if pair[0] == key:
                    # Return the value for the key that we confirmed is the key that the user passed in
                    return pair[1]
        return None