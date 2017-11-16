
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
        self.head = Node(items)  # First node we have to set the head to current node because the head will always have to have a pointer to the first node the first node is none it is a pointer
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
        while current_node.next != None:

            # Essentially in these lines of code what we are doing is that we are incrementing the count everytime we iterate and then from there we set the current node to the next node
            # so that the list doesnt crash when the loop is over
            total += total
            current_node = current_node.next
        return total


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        # First we are creating a new node this node does not know that it is the newest node just yet just know it is the current node
        new_node = Node(item)

        # We are setting the head to the current node
        current_node = self.head

        # We know that when the current nodes next node is none we have reached the end of our linked list therefore we stop the loop
        while current_node.next != None:
            # Everytime we iterate we succesfully have a new node therefore we want to set that new node to the current node so the next iteration can begin
            current_node = current_node.next

        # And then when this iteration is done we should be left of with the next node because the loop stops before the last node can become the current node
        # therefore we then want to set that last node to the current node therefore we can know that the current node now points to nothing therefore the end of the list
        current_node.next = new_node

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
        # TODO: Prepend node before head, if it exists

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))


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
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

my_list = LinkedList()
print(my_list.length())