from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def is_empty(self):
        return self.__head is None

    def insert_at_head(self, new_node: PlayerNode):
        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__head = new_node

    def insert_at_tail(self, new_node: PlayerNode):
        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.previous = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

    def delete_at_head(self):
        if self.is_empty:
            return None

        removed_node = self.__head

        if self.__head is self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__head = removed_node.next
            self.__head.previous = None
            removed_node.next = None

        return removed_node

    def delete_at_tail(self):
        if self.is_empty:
            return None

        removed_node = self.__tail

        if self.__head is self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = removed_node.previous
            self.__tail.next = None
            removed_node.previous = None

        return removed_node

    def delete_by_key(self, key):
        current_node = self.__head

        while current_node is not None:
            if current_node.key == key:
                if current_node is self.__head:
                    return self.delete_at_head()

                if current_node is self.__tail:
                    return self.delete_at_tail()

                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous

                current_node.previous = None
                current_node.next = None

                return current_node

            current_node = current_node.next

        return None

    def display(self, forward= True):
        if forward:
            current_node = self.__head

            while current_node is not None:
                print(current_node)
                current_node = current_node.next

            else:
                current_node = self.__tail

                while current_node is not None:
                    print(current_node)
                    current_node = current_node.previous