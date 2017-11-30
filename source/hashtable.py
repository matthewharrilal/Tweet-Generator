#!python

from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        for bucket in self.buckets:
            if bucket is not None:
                for node in bucket:
                    print(node[1])

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        # So if we arte trying to find the number of how many buckets there are we essentially need all the buckets so we
        # have to iterate through the hash map but the kick is not the number of buckets the sum of all the pairs in all the buckets
        bucket_count = 0
        for bucket in self.buckets:
            # Now that we have each bucket we now have to figure out a way to get each pair in the bucket
            pass
    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        # So to even see if the bucket contains the key the user is looking for we have to get the location of the bucket
        bucket_index = self._bucket_index(key)

        # Now that we have the location of the bucket we now have to see if the bucket even contains any values before we start searching
        if self.buckets[bucket_index] is None:
            print('There were no values in this bucket to begin with')
            return

        for pair in self.buckets[bucket_index]:
            # When iterating through all possible pairs in the desired bucket we check if the key the user passes in matches
            # the key in any of the pairs in the bucket
            if key == pair[0]:
                return True
            # If not return False meaning the user passed in a non existent key
            return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

       # To even get the key that the user passes in we first have to find the bucket it is in
        bucket_index = self._bucket_index(key)

        found_bucket = self.buckets[bucket_index]
        # # Now that we have the location of the bucket we have to first check if there are even any values in the bucket
        # if self.buckets[bucket_index].is_empty:
        #     raise KeyError('Key not found: {}'.format(key))
        # else:
        #     # If we come into this else block we know that the bucket does contain values we do not know how many though therefore
        #     # we have to start iterating through and see when the key in the pair matches the key the user has passed in
        #     for pair in self.buckets[bucket_index].items():
        #         if pair[0] == key:
        #             # Since we know that the pairs are a list constructed of key value pairs we know that the second element is the
        #             # value for the key
        #             return pair[1]


        entry = found_bucket.find(lambda linked_item: linked_item[0] == key)
        if entry:
            # print('this is get entry', entry)
            return entry
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        # Going to insert data at a specific index therefore we first have to get the index of the bucket
        bucket_index = self._bucket_index(key)

        # Since we are solving this with lists we can hold the key value pairs in a list
        key_value = [key, value]

        # We should hold the desired bucket somewhere just so we can call it


        # # Now that we have the index of the bucket we have to see if there are any values if theres none then we can just set the data if there is we are going to have to append a node
        # if self.buckets[bucket_index] is None:
        #     self.buckets[bucket_index] = key_value
        #     return True
        # # Now that we have established that the bucket does actually have values we then face the problem where we actually
        # # do not know how many values are in the bucket therefore we have to iterate
        # else:
        #     for pair in self.buckets[bucket_index]:
        #         # The reason we can do this is due to the reason that we know that the first element at 0 is always going to be the key
        #         if pair[0] == key:
        #             # If the user tries to add to a key that already exists then we simply update the value
        #             # Why do we have to update the value that is just overwriting it does this purposefully avoid collisions?
        #             # Why overwrite it shouldnt we add another pair
        #             pair[1] = value
        #             return True
        #     # However if the user passes in a key that doesnt exist in the bucket we simply make another pair for it
        #     self.buckets[bucket_index].append(key_value)

        # Holding the bucket in the variable
        found_bucket = self.buckets[bucket_index]

        entry = found_bucket.find(lambda linked_item: linked_item[0] == key)
        if entry:
            found_bucket.delete(entry)
        found_bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        # If the user wants to delete a pair in the bucket we first have to get the location of the bucket where the key is
        bucket_index = self._bucket_index(key)

        bucket = self.buckets[bucket_index]

        # Using the find method in the linked list
        found = bucket.find(lambda item: item[0] == key)  # Linear time
        # If found is not empty
        if found is not None:
            # Then delete item from bucket
            bucket.delete(found)
            return
        else:
            raise KeyError("Key not longer exists in this hash table")


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()

