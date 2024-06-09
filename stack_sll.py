# Name: Jacob Mosiman
# OSU Email: mosimaja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 (Linked List and ADT Implementation)
# Due Date: 5/6/24
# Description: Implementation of a Stack ADT utilizing a chain of SLNodes (Singly Linked Nodes) as underlying storage.


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Adds a new element with specified value to the top of the stack.

        :param value:   Value to be added to the top of the stack.

        :return:        None.
        """
        new_node = SLNode(value)

        # If stack empty, set head to new_node
        if not self._head:
            self._head = new_node
        # If stack not empty, set new_node's next to current head, then set head to new_node
        else:
            new_node.next = self._head
            self._head = new_node

    def pop(self) -> object:
        """
        Removes the element at the top of the stack and returns its value.

        :param:     None.

        :return:    Value at the top of the stack before pop call.
        """
        # If stack empty, raise exception
        if not self._head:
            raise StackException

        top_value = self._head.value

        # If no node after head, set head to None
        if not self._head.next:
            self._head = None
        # If node after head, set head to that node
        else:
            self._head = self._head.next

        return top_value

    def top(self) -> object:
        """
        Returns the value of the element at the top of the stack without removing it.

        :param:     None.

        :return:    Value of element at the top of the stack.
        """
        # If stack empty, raise exception
        if not self._head:
            raise StackException

        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
