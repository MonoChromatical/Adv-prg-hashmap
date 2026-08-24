from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        # Start with an empty list.
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        # Return the first node.
        return self.__head

    @property
    def tail(self):
        # Return the last node.
        return self.__tail

    @property
    def is_empty(self):
        # The list is empty when it has no head node.
        return self.__head is None

    def insert_at_head(self, new_node: PlayerNode):
        # Check whether the list is empty.
        if self.is_empty:
            # Make the new node both the head and tail.
            self.__head = new_node
            self.__tail = new_node
        else:
            # Connect the new node before the current head.
            new_node.next = self.__head
            self.__head.previous = new_node

            # Make the new node the head.
            self.__head = new_node

    def insert_at_tail(self, new_node: PlayerNode):
        # Check whether the list is empty.
        if self.is_empty:
            # Make the new node both the head and tail.
            self.__head = new_node
            self.__tail = new_node
        else:
            # Connect the new node after the current tail.
            new_node.previous = self.__tail
            self.__tail.next = new_node

            # Make the new node the tail.
            self.__tail = new_node

    def delete_at_head(self):
        # Return None when there is nothing to delete.
        if self.is_empty:
            return None

        # Save the node that will be removed.
        removed_node = self.__head

        # Check whether the list contains only one node.
        if self.__head is self.__tail:
            # Empty the list.
            self.__head = None
            self.__tail = None
        else:
            # Move the head to the next node.
            self.__head = removed_node.next
            self.__head.previous = None

            # Disconnect the removed node.
            removed_node.next = None

        # Return the node that was removed.
        return removed_node

    def delete_at_tail(self):
        # Return None when there is nothing to delete.
        if self.is_empty:
            return None

        # Save the node that will be removed.
        removed_node = self.__tail

        # Check whether the list contains only one node.
        if self.__head is self.__tail:
            # Empty the list.
            self.__head = None
            self.__tail = None
        else:
            # Move the tail to the previous node.
            self.__tail = removed_node.previous
            self.__tail.next = None

            # Disconnect the removed node.
            removed_node.previous = None

        # Return the node that was removed.
        return removed_node

    def find_by_key(self, key):
        # Start searching from the head.
        current_node = self.__head

        # Continue until the end of the list.
        while current_node is not None:
            # Return the node when its key matches.
            if current_node.key == key:
                return current_node

            # Move to the next node.
            current_node = current_node.next

        # Return None when the key is not found.
        return None

    def delete_by_key(self, key):
        # Start searching from the head.
        current_node = self.__head

        # Continue until the end of the list.
        while current_node is not None:
            # Check whether this is the node to delete.
            if current_node.key == key:
                # Use the head deletion method when needed.
                if current_node is self.__head:
                    return self.delete_at_head()

                # Use the tail deletion method when needed.
                if current_node is self.__tail:
                    return self.delete_at_tail()

                # Connect the surrounding nodes to each other.
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous

                # Disconnect the removed node.
                current_node.previous = None
                current_node.next = None

                # Return the node that was removed.
                return current_node

            # Move to the next node.
            current_node = current_node.next

        # Return None when the key is not found.
        return None

    def display(self, forward=True):
        # Check which direction should be displayed.
        if forward:
            # Begin at the head for forward traversal.
            current_node = self.__head

            # Print each node from head to tail.
            while current_node is not None:
                print(current_node)
                current_node = current_node.next
        else:
            # Begin at the tail for backward traversal.
            current_node = self.__tail

            # Print each node from tail to head.
            while current_node is not None:
                print(current_node)
                current_node = current_node.previous