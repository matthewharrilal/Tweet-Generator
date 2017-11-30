#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        # The reason why the next node is set to none is because there are no other nodes currently the pointer is pointing to null

        # User never actually interacts with the node class

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node we have to set the head to current node because the head will always have to have a pointer to the first node the first node is none it is a pointer
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each

        # First thing we essentially need is the first node
        current_node = self.head

        # Then we need a counter to see how many times thee while loop iterates over the list
        total = 0

        # This is similar to essentially stopping a list index out of range since the current node is always looking to the next node if the loop is done iterating
        # it will stop at the last node and make that the current node, but that node doesn't exist therefore it will crash however if you set the last node to the next node
        # we can stop the loop and outside of the loop to simpley make that the current node however we only care about making that the current node if we have to use the current node
        # here we only care about the count and even thought the iteration stops on the next node we still iterate over it fully before crash
        while current_node is not None:

            # Essentially in these lines of code what we are doing is that we are incrementing the count everytime we iterate and then from there we set the current node to the next node
            # so that the list doesnt crash when the loop is over
            total += 1
            current_node = current_node.next
        return total

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists


        # Instantiate a node to represent what the user wants to append to the end of the list
        new_node = Node(item)

        # In the case where the list is not empty we taking in account the first possible node
        current_node = self.head

        # Take in account of the linked list in its current state
        count = self.length()

        if count == 0:
            # The reason that we assign the head and the tail to the new node in this fashion is due to to the fact that the node has to be instantiated
            # Therfore we assign the head and the tail to it where as when we set current_node.next to the head and the tail is because it already exists
            self.head = new_node
            self.tail = new_node
            return
        else:
            # Instead of having to iterate through the whole list we can just locate the end of the list and append there
            self.tail.next = new_node
            self.tail = new_node
            return


    def display_all_nodes(self):
        # Essentially in this function we want to display all the nodes in our linked list therefore we are going to need a list
        list_of_nodes = []

        # Sets the pointer of where the head points to the fist current node therefore when we loop we get other  nodes
        current_node = self.head

        # As we discussed before this is to keep the error being thrown at us that the list is going out of range
        while current_node.next != None:

            # Set the next node to the new current node every succeful iteration this contributes how we populate each element in the list
            current_node = current_node.next

            # We dont care about how many nodes they are we care about the data within the nodes which is the property that we have initalized
            list_of_nodes.append(current_node.data)
        return list_of_nodes

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # # TODO: Prepend node before head, if it exists



        # We have to instantiate a new node and that represents what the user wants to prepend
        new_node = Node(item)

        # accounting for the case where the length of the linked list is 0 then when we prepend we want the head as well as the tail to be pointing to the node we had instantiated
        if self.length() == 0:
            self.tail = new_node

        else:
            # What this is essentially saying that we have to set the new nodes next values pointer equal to the old head this essentially gives us a previous value
            new_node.next = self.head
        # Then we establish that the pointer of the head is pointing to the new node that we had instantiated
        self.head = new_node



    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        current_node = self.head



        while current_node.data != quality:
            current_node = current_node.next
            if current_node is None:
                # raise ValueError('Item not found: {}'.format(quality))
                return None
        return current_node.data



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        # The reason that we use the is empty function opposed to the length function then we rather go to the direct to checking if the head is there
        # as oppose to iterating through the values and seeing nothing is in there
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        # Setting the pointer of the head to point to the first node
        current_node = self.head



        if self.length() == 1:
            #
            #     # We have to tell the head and the tail not to point anything because what they are pointing to is about to be deleted
            self.head = None
            self.tail = None
            return

        # Until the data of the node matches the name of the item we do not stop iterating
        while current_node.data != item:

            # This gives us three positions the previous node the current node and the next node
            previous_node = current_node
            current_node = current_node.next

            # The reason that we have to put this statement inside the loop is becuase if the user is trying to delete an item that is
            # not in the linked list we will be caught in an infinite loop therefore we have to return after its done iterating thorugh all
            # the values and we know we are done because we have the current node
            if current_node is None:
                raise ValueError('Item not found: {}'.format(item))


        # Since we have the node the user is trying to delete we then have to verify if the node that is trying to be deleted is the head
        if current_node == self.head:
            # Update the head to the next node therefore bumping out the current node or deleting it
            self.head = current_node.next
            return

        # If the node that the user is trying to delete is the tail
        if current_node == self.tail:
            # We update the tail to be pointing to previous node
            self.tail = previous_node

            # We then set the previous nodes pointer equal to None
            previous_node.next = None
            return

        previous_node.next = current_node.next






        #
        #     # We start iterating through by setting the previous node to the current node everytime we iterate through the loop
        #     previous_node = current_node
        #
        #     # We start iterating through and we set that current node to the next node and then we have now a current node next node as well as previous node
        #     current_node = current_node.next
        #
        #     # When the name of the item the user passes in matches the data of the node we are looking for
        #     if current_node.data == item:
        #
        #         # We then set the pointer of the previous node to the node after the current node
        #         previous_node.next = current_node.next
        #
        #         # If the length of the list is only one we have to go about deleting the node in a different way
        #         #
        #
        #         if item == self.tail.data:
        #
        #             # If the user is trying to delete the last node of the list essentially where the tail is pointing we
        #             # set the previous node next node to none so it knows we are pointing to None
        #
        #             previous_node.next = None
        #             self.tail = previous_node
        #
        #
        #             return
        #             # We then set the tail to the previous node
        #
        #         if item == self.head.data:
        #
        #             # If the user trys to delete the first node we set the pointer of the head to that nodes next node
        #             current_node.next = self.head
        #
        #             # We then set the current node to None to basically say it doesnt exist
        #             current_node = None
        #         return
        #
        #
        # raise ValueError('Item not found: {}'.format(item))
        #


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


linked = LinkedList()

linked.append("Matthew")
linked.append("Steven")
print(linked.length())