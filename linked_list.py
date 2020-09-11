from Node import Node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __len__(self):
        return self.__len

    def insert(self, index, value):
        insert_node = Node(value)
        if not self.__len:  # пустой список
            self.__head = insert_node
            self.__tail = self.__head

            self.__len += 1

        elif index >= self.__len:  # вставка вне границ
            insert_node.prev = self.__tail
            self.__tail.next = insert_node
            self.__tail = insert_node

    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def __iter__(self):
        current_node = self.__head
        for _ in range(self.__len):
            yield current_node.value
            current_node = current_node.next


    def find(self, node):
        ...

    def remove(self, node):
        ...

    def delete(self, index):
        ...


if __name__ == '__main__':
    l = LinkedList()
    print(len(l))