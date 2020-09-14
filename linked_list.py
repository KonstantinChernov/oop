from Node import Node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __len__(self):
        return self.__len

    def __iter__(self):
        current_node = self.__head
        for _ in range(self.__len):
            yield current_node.value
            current_node = current_node.next

    def __str__(self):
        return f'linked{list(self)}'

    def insert(self, index, insert_node):
        if not isinstance(insert_node, Node):
            insert_node = Node(insert_node)

        if index > self.__len:
            raise IndexError(f'The maximum index you can match is {self.__len}')
        elif index < 0:
            raise IndexError(f'Negative indexation is not required in this list')
        elif index == 0:
            insert_node.next = self.__head
            self.__head = insert_node
        elif index == self.__len:
            insert_node.prev = self.__tail
            self.__tail = insert_node
        else:
            current_node = self.__head
            for _ in range(index):
                current_node = current_node.next
            insert_node.prev = current_node.prev
            insert_node.next = current_node
        self.__len += 1

    def append(self, append_node):
        """
        Append Node to tail of LinkedList
        node - Node
        """
        if not isinstance(append_node, Node):
            append_node = Node(append_node)

        if not self.__len:
            self.__head = append_node
            self.__tail = self.__head
        else:
            append_node.prev = self.__tail
            self.__tail.next = append_node
            self.__tail = append_node

        self.__len += 1

    def clear(self):
        """
        Clear LinkedList
        """
        current_node = self.__head
        for _ in range(self.__len):
            if current_node.next:
                current_node = current_node.next
                current_node.prev = None
        self.__len = 0

    def find(self, node):
        current_node = self.__head
        ind = 0
        for _ in range(self.__len):
            if current_node == node:
                return ind
            current_node = current_node.next
            ind += 1

    def remove(self, node):
        current_node = self.__head
        for _ in range(self.__len):
            if current_node == node:
                if current_node == self.__head:
                    current_node.next = self.__head
                    self.__head.prev = None
                    break
                elif current_node == self.__tail:
                    current_node.prev = self.__tail
                    self.__tail.next = None
                    break
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    break
            current_node = current_node.next
        self.__len -= 1

    def delete(self, index):
        current_node = self.__head
        ind = 0
        if index < 0:
            raise IndexError('Index should be of a positive value')
        if index > self.__len - 1:
            raise IndexError('Index is out of range')
        for _ in range(self.__len):
            if ind == index:
                if current_node == self.__head:
                    self.__head = current_node.next
                    self.__head.prev = None
                    break
                elif current_node == self.__tail:
                    current_node.prev = self.__tail
                    self.__tail.next = None
                    break
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    break
            current_node = current_node.next
            ind += 1
        self.__len -= 1

    @classmethod
    def linked_list(cls, iterable):
        linked_list = cls()
        if isinstance(iterable, (list, tuple, set)):
            for index, value in enumerate(iterable):
                node = Node(value)
                linked_list.append(node)
            return linked_list
        else:
            raise TypeError('Argument should be an iterable object (but not dict)')









if __name__ == '__main__':
    l = LinkedList()
    print(len(l))
