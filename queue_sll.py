# Name: Jacob Mosiman
# OSU Email: mosimaja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 (Linked List and ADT Implementation)
# Due Date: 5/6/24
# Description: Implementation of a Queue ADT utilizing a chain of SLNodes (Singly Linked Nodes) as underlying storage.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
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
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds the specified value to the end of the queue.

        :param value:   Value to be added to the end of the queue.

        :return:        None.
        """
        new_node = SLNode(value)

        # If empty queue, set head and tail to new_node
        if not self._head:
            self._head = new_node
            self._tail = new_node
        # If queue not empty, set old tail.next to new_node then tail to new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> object:
        """
        Removes the first item in the queue and returns its value.

        :param:     None.

        :return:    Value of the first item in the queue before dequeue call.
        """
        # If queue empty, raise exception
        if not self._head:
            raise QueueException

        front_val = self._head.value

        # Update head to next (or None if queue now empty)
        self._head = self._head.next
        if not self._head:              # If queue now empty, de-references tail
            self._tail = None

        return front_val

    def front(self) -> object:
        """
        Returns the value of the first item in the queue without removing it.

        :param:     None.

        :return:    Value of the first item in the queue.
        """
        # If queue empty, raise exception
        if not self._head:
            raise QueueException

        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
