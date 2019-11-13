from Linked_List import LinkedList


def iterate_count(input_list):
    count = 0
    node = input_list.get_root()
    while node is not None:
        count += 1
        node = node.get_next()
    return count


def recursive_count(input_list):
    node = input_list.get_root()
    return _recursive_count(node, 0)


def _recursive_count(node, count):
    if node is not None:
        return _recursive_count(node.get_next(), count + 1)
    return count


cool_list = LinkedList()
cool_list.insert(1)
cool_list.insert(1)
cool_list.insert(2)
cool_list.insert(1)
cool_list.insert(1)

cool_list.in_order()

print ()
print (iterate_count(cool_list))
print (recursive_count(cool_list))