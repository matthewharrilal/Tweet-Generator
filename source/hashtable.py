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

       # If we are going to get a value we first have to get bucket at which the key is in
        bucket_index = self._bucket_index(key)

        # We then have to get the actual bucket
        bucket = self.buckets[bucket_index]

        # Now that we have the bucket as well as knowing that in a hash table that we are going to be storing key value pairs we then have
        # to store the values in a tuple therefore what we can do is that we can use a higher order function to get the first value and then from
        # there what we can do is that we can use that to iterate as well as compare the key that the user passes in to the current key we are on
        key_matching = bucket.find(lambda key_value: key_value[0] == key)

        # When the key matching is done sorting through all the values in addition to us having edge cases in the linked list file for the find function
        # we can then use simple error handling to see if the data we get back for the key_matching is none and if it is raise the value error
        if key_matching is None:
            raise KeyError('Key not found: {}'.format(key_matching))
        # Now that we have filtered for if the key matching results are done what we can now do from here is we can now return the value from that tuple
        return key_matching[1]


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        # If we are going to be updating values then we first have to find the bucket that we are trying to set the key at
        bucket_index = self._bucket_index(key)

        #Then we have to get the value at that bucket_index or essentially the bucket
        bucket = self.buckets[bucket_index]

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


# if __name__ == '__main__':
#     test_hash_table()

hash = HashTable()
print(hash.get('matthew'))