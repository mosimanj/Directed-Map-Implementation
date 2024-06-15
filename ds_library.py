# Contains supporting data structures for directed graph project

class Node:
    """Node used in Queue and Stack implementations."""

    def __init__(self, value: object, next = None):
        self.value = value
        self.next = next


class QueueEmptyException(Exception):
    """Exception indicating that the Queue is empty. Raised if dequeue attempt made on empty Queue."""
    pass


class Queue:
    """Queue implemented with SLL."""

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        """
        Returns True if Queue is empty, False otherwise.

        :param:         None.
        :return:        Boolean indicating if list is empty (True) or not (False).
        """
        return self._head is None

    def enqueue(self, value: object) -> None:
        """
        Adds the specified value to the end of the queue.

        :param value:   Value to be added to the end of the queue.

        :return:        None.
        """
        new_node = Node(value)

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

        :param:         None.

        :return:        Value of the first item in the queue before dequeue call.
        """
        # If queue empty, raise exception
        if not self._head:
            raise QueueEmptyException

        front_val = self._head.value

        # Update head to next (or None if queue now empty)
        self._head = self._head.next
        if not self._head:              # If queue now empty, de-references tail
            self._tail = None

        return front_val


class StackEmptyException(Exception):
    """Exception indicating that stack is empty. Raised when an attempt is made to pop from an empty stack."""
    pass


class Stack:
    """Stack implemented with SLL."""

    def __init__(self):
        self._top = None

    def is_empty(self) -> bool:
        """
        Returns True if Stack is empty, False otherwise.

        :param:         None.

        :return:        Boolean indicating if Stack is empty (True) or not (False).
        """
        return self._top is None

    def push(self, value: object) -> None:
        """
        Adds a new element with specified value to the top of the stack.

        :param value:   Value to be added to the top of the stack.

        :return:        None.
        """
        new_node = Node(value)

        # If stack empty, set head to new_node
        if not self._top:
            self._top = new_node
        # If stack not empty, set new_node's next to current top, then set top to new_node
        else:
            new_node.next = self._top
            self._top = new_node

    def pop(self) -> object:
        """
        Removes the element at the top of the stack and returns its value.

        :param:         None.

        :return:        Value at the top of the stack before pop call.
        """
        # If stack empty, raise exception
        if not self._top:
            raise StackEmptyException

        top_value = self._top.value

        # If no node after top, set head to None
        if not self._top.next:
            self._top = None
        # If node after top, set top to that node
        else:
            self._top = self._top.next

        return top_value


class MinHeapEmptyException(Exception):
    """Exception indicating that MinHeap is empty. Raised when an attempt is made to remove from empty heap."""


class MinHeap:
    """MinHeap used for min_path (Dijkstra's Algorithm) method in map class."""
    def __init__(self):
        self._heap = []

    def add(self, node: object) -> None:
        """
        Adds specified object to MinHeap. Operation maintains heap property.

        :param node:    Object to be added to the MinHeap.

        :return:        None
        """
        # Add node to end of storage array
        self._heap.append(node)

        # Initialize variables to calculate and track index of node and parent
        node_ind = len(self._heap) - 1
        parent_ind = (node_ind-1)//2

        # While node not at start of storage array and node's value less than parent, percolate up
        while node_ind > 0 and self._heap[node_ind] < self._heap[parent_ind]:
            self._heap[node_ind] = self._heap[parent_ind]
            self._heap[parent_ind] = node
            node_ind = parent_ind
            parent_ind = (node_ind-1)//2

    def is_empty(self) -> bool:
        """
        Returns True if heap is empty, otherwise returns False (if not empty).

        :param:     None.

        :return:    Boolean. True if empty, False if not empty.
        """
        # Returns True (empty) if underlying storage has a size less than 1
        if len(self._heap) < 1:
            return True

        return False

    def remove_min(self) -> object:
        """
        Removes and returns the heap's top item. Raises exception if heap is empty.

        :param:     None.

        :return:    Object at the top of the heap before method call.
        """
        # If empty --> exception, if one element --> remove and return it
        if self.is_empty():
            raise MinHeapEmptyException
        elif len(self._heap) == 1:
            return self._heap.pop()

        # Store min value before replacing with last element added
        min_val = self._heap[0]
        self._heap[0] = self._heap.pop()

        # If there is more than one element after last element removed, percolate replacement down
        if len(self._heap) > 1:
            self._percolate_down()

        return min_val

    def _percolate_down(self) -> None:
        """
        Compares parent value to the smallest child's value and swaps if parent greater. Stops when parent less or there
        are no children remaining.

        :return:        None.
        """
        parent_value = self._heap[0]
        parent = 0
        left = 1
        right = 2
        end = len(self._heap) - 1

        # Continue while one of the computed child indices are valid
        while left <= end or right <= end:
            # If both indices are valid, set target to smallest (or left if equal). If only one valid, set as target.
            if left <= end and right <= end:
                if self._heap[left] <= self._heap[right]:
                    target = left
                else:
                    target = right
            elif left <= end:
                target = left
            else:
                target = right

            # If parent's value greater than target's, swap & update pointers. Otherwise, return (at final position).
            if self._heap[parent] > self._heap[target]:
                self._heap[parent] = self._heap[target]
                self._heap[target] = parent_value

                parent = target
                left = (2 * parent) + 1
                right = (2 * parent) + 2
            else:
                return
