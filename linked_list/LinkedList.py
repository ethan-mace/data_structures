from node.node import Node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
        self.list_size = 0

        if value is not None:
            self.list_size = 1

    def get_head_node(self):
        return self.head_node

    def size(self):
        return self.list_size

    def insert_beginning(self, new_value):
        new_node = Node(new_value)

        if self.head_node.get_value() is not None:
            new_node.set_next_node(self.head_node)

        self.head_node = new_node
        self.list_size += 1

    def stringify_list(self):
        string_list = []
        current_node = self.get_head_node()
        while current_node:
            string_list.append(str(current_node.get_value()))
            current_node = current_node.get_next_node()
        return str(string_list)

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            self.list_size -= 1
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                    self.list_size -= 1
                else:
                    current_node = next_node
                    self.list_size -= 1




def find_max(linked_list):
    """Finds the maximum value within a LinkedList

    :param: linked_list: LinkedList
    :return: maximum value within LinkedList
    """

    # Gets head node of linked list
    current = linked_list.get_head_node()

    # Get value of head node
    maximum = current.get_value()

    # Loop until next node is None
    while current:

        # Get value of current node
        val = current.get_value()

        # Check if current node's value is greater than previous node's value
        if val > maximum:
            # Maximum value is value of current node
            maximum = val

        # Set current node to next node
        current = current.get_next_node()

    return maximum


def sort_linked_list(linked_list):
    """Creates a new LinkedList of values sorted from least to greatest

    :param linked_list: LinkedList
    :return: LinkedList of values sorted from least to greatest
    """

    # Instantiate new LinkedList
    new_linked_list = LinkedList()

    # Loop until original LinkedList is empty
    while linked_list.get_head_node():

        # Get max value of original LinkedList
        value = find_max(linked_list)

        # New LinkedList head is node of current value with next node being node of previous value
        new_linked_list.insert_beginning(value)

        # Remove node of current value from original LinkedList
        linked_list.remove_node(value)

    return new_linked_list
