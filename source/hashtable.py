#!python
import pdb

from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

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
        all_values = []
        #
        # for bucket in self.buckets:
        #    values_in_bucket = bucket.find(lambda value: value[1])
        #    print('These are the values in the bucket %s' %(values_in_bucket))
        #    all_values.append(values_in_bucket)
        # return all_values

        for bucket in self.buckets:
            for key,value in bucket.items():
                print('These are the values %s' %(value))
                all_values.append(value)
        return all_values


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

        # All we need to do is return the length of self.items due to us already traversing the buckets in the items function
        # return len(self.items())
        return self.size


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        # So to even see if the bucket contains the key the user is looking for we have to get the location of the bucket
        index = self._bucket_index(key)

        # Getting that bucket at that index
        bucket = self.buckets[index]

        # Using lambda to find and iterate through the keys to see if any match the key that the user provided
        key_match = bucket.find(lambda key_value: key_value[0] == key)

        # Return the boolean value depending on the value from the key match
        return key_match is not None


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
        # key_matching = bucket.find(lambda key_value: key_value[0] == key)
        #
        # # When the key matching is done sorting through all the values in addition to us having edge cases in the linked list file for the find function
        # # we can then use simple error handling to see if the data we get back for the key_matching is none and if it is raise the value error
        # if key_matching is not None:
        #     return key_matching[1]
        # # Now that we have filtered for if the key matching results are done what we can now do from here is we can now return the value from that tuple
        # raise KeyError('Key not found: {}'.format(key))

        # Iterate through the key value pairs in the specific bucket that we have found
        for iter_key, iter_value in bucket.items():
            # If the keys we are iterating through over matches the key that the user passes in then return that value back to me
            if iter_key == key:
                return iter_value
        # If not raise the key error
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        # Finding the index of the bucket at the given key
        bucket_index = self._bucket_index(key)

        # Find the bucket at the index
        bucket = self.buckets[bucket_index]

        # Check if the key is contained in the bucket we have found using the key
        if self.contains(key):

            # If so we find the old value using the get function which returns us a value at the given key
            old_value = self.get(key)

            # Then we delete the key and old value pair in that bucket
            bucket.delete((key,old_value))

            bucket.append((key, value))
        else:
            bucket.append((key,value))
            self.size += 1


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key)

        bucket = self.buckets[bucket_index]

        if bucket.is_empty():
            # Checking if the bucket is empty and if so raising the key value error
            raise KeyError('Key not found: {}'.format(key))
        else:
            # Since the get function gets the value at a given key we get the corresponding value to the given key by the user
            value = self.get(key)
            # Then delete that key value pair
            bucket.delete((key,value))
            self.size -= 1





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
