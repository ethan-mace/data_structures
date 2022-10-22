import random
from linked_list import LinkedList


class Tests:

    def linked_list(self):
        new_list = LinkedList.LinkedList()

        i1, i2, i3, i4 = 10, 1000, -1000, 1000

        rand_num = random.randint(i1, i2)

        print(f'\n*** Test: Instantiate LinkedList with Randomly Generated Size of {rand_num} ***\n')

        while rand_num > 0:
            value = random.randint(i3, i4)
            new_list.insert_beginning(value)
            rand_num -= 1

        print(f'LinkedList Size: {new_list.size()}\n')
        print(f'Unsorted values of LinkedList: \n\t{new_list.stringify_list()}\n')
        print(f'*** Test: Get max value of LinkedList: {LinkedList.find_max(new_list)} ***\n')
        print(f'*** Test: Sort Values from Least to Greatest ***\n')

        sorted_list = LinkedList.sort_linked_list(new_list)

        print(f'Sorted values of Linked List:\n\t {sorted_list.stringify_list()}')

