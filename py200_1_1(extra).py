# from py200_1_1 import Glass, GlassDefaultListArg
from Node import Node
from linked_list import LinkedList

def main():
    glass1 = Glass(200, 100)
    glass1.add_water(300)
    print(glass1)
    glass1.remove_water(700)

    print(glass1)

    glass1.add_water(100)
    print(glass1)

    glass1.remove_water(50)
    print(glass1)


if __name__ == '__main__':
    node = Node(1, Node(2), Node(3))
    print(node)

    node3 = Node(5)
    print(node3)
    node.next = node3
    print(node3)
    print(node)
    print(dir(node3))
    print(node3.prev)

    a = LinkedList()

    a.append(25)
    a.append(23)
    a.append(21)
    a.append(2)
    a.append(27)

    for i in a:
        print(i)

    print('=============')
    a.insert(3, 0)

    for i in a:
        print(i)
    print('=============')

    a.insert(6, 5)
    for i in a:
        print(i)
    print('=============')
    print(len(a))
    node3 = Node(123)

    # print(len(a))
    a.insert(4, node3)
    # print(len(a))
    # n = [1, 2, 6, 8]
    print(list(a))

    print('=============')
    print(a.find(node3))

    print(a.remove(node3))

    print(list(a))

    print(a.delete(3))

    print(list(a))
    #
    #
    # print(a.delete(5))
    #
    # print(list(a))
    #
    print(a.delete(0))

    print(list(a))
    print('=============')

    # print(a.clear())
    #
    # print(list(a))
    print('=============')
    b = LinkedList.linked_list([2,4,6,7,8,6,'helo'])
    # print(b.linked_list([2,4,6,7,8,6,'helo']))
