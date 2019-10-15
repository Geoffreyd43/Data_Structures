class ListNode:

    def __init__(self, val):
        self.data = val
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node
