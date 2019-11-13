from List_Node import ListNode


class LinkedList:

    def __init__(self):
        self.root = None

    # O(n) time to loop through list one time
    def in_order(self):
        current = self.root
        print('\nList values:')
        while current is not None:
            print(current.get_data())
            current = current.get_next()

    # O(1) time to insert one item into list
    def insert(self, val):
        temp = self.root
        self.root = ListNode(val)
        self.root.set_next(temp)

    # O(n) time to delete a given node
    def delete_node(self, val):

        current = self.root
        previous = self.root
        found = False

        while current is not None and found is False:
            if current.get_data() == val and current != self.root:
                previous.set_next(current.get_next())
                found = True
            elif current.get_data() == val:
                self.root = self.root.get_next()
                found = True

            previous = current
            current = current.get_next()

        if found is False:
            print(val, 'was not in the list...')
        else:
            print(val, 'was deleted successfully')

    def get_root(self):
        return self.root

    def get_node(self, val):
        current = self.root
        while current is not None:
            if current.get_data() == val:
                return current
            current = current.get_next()
        return str(val) + ' was not found'


