# Contains supporting data structures for directed graph project

class Node:
    """Node used in Queue and Stack implementations."""

    def __init__(self, value: object, next=None):
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
    """MinHeap used for min_path (Dijkstra's Algorithm) method in directed map class."""
    def __init__(self):
        self._heap = []

    def add(self, priority: int, value: object) -> None:
        """
        Adds specified object to MinHeap with the given priority. Operation maintains heap property.

        :param priority:    Integer representing the priority of the value being added to the MinHeap. Smaller priority
                            values are at the top of the MinHeap.
        :param value:       Object representing the value being added to the MinHeap.

        :return:        None
        """
        # Add the priority and value ('node') to end of storage array as tuple
        node = (priority, value)
        self._heap.append(node)

        # Initialize variables to calculate and track index of node and parent
        node_ind = len(self._heap) - 1
        parent_ind = (node_ind-1)//2

        # While node not at start of storage array and node's priority value less than parent's, percolate up
        while node_ind > 0 and self._heap[node_ind][0] < self._heap[parent_ind][0]:
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

    def remove_min(self) -> tuple:
        """
        Removes and returns the heap's top item. Raises exception if heap is empty.

        :param:     None.

        :return:    Tuple containing the priority and value of the top item of the heap before method call.
        """
        # If empty --> exception, if one element --> remove and return it
        if self.is_empty():
            raise MinHeapEmptyException
        elif len(self._heap) == 1:
            return self._heap.pop()

        # Store min value before replacing with last element added
        min_val = self._heap[0][1]
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
        parent = self._heap[0]
        parent_ind = 0
        left_ind = 1
        right_ind = 2
        end_ind = len(self._heap) - 1

        # Continue while one of the computed child indices are valid
        while left_ind <= end_ind or right_ind <= end_ind:
            # If both indices are valid, set target to smallest (or left if equal). If only one valid, set as target.
            if left_ind <= end_ind and right_ind <= end_ind:
                if self._heap[left_ind][0] <= self._heap[right_ind][0]:
                    target = left_ind
                else:
                    target = right_ind
            elif left_ind <= end_ind:
                target = left_ind
            else:
                target = right_ind

            # If parent's value greater than target's, swap & update pointers. Otherwise, return (at final position).
            if self._heap[parent_ind][0] > self._heap[target][0]:
                self._heap[parent_ind] = self._heap[target]
                self._heap[target] = parent

                parent_ind = target
                left_ind = (2 * parent_ind) + 1
                right_ind = (2 * parent_ind) + 2
            else:
                return

    def print_heap(self) -> None:
        """
        Prints the MinHeap's underlying storage array. Used for testing.

        :param:         None.

        :return:        None.
        """
        print([val for val in self._heap])


class PriorityQueue:
    """Priority Queue ADT used for directed graph's min_path. Utilizes MinHeap as underlying data structure."""

    def __init__(self):
        self._data = MinHeap()

    def enqueue(self, priority: int, value: object) -> None:
        """
        Adds the specified value to the PriorityQueue. Its position in the queue is determined based on the given
        priority. The smallest priority value is placed in the front of the queue.

        :param priority:    Integer representing the priority of the added item. Smaller value = higher priority.
        :param value:       The value being stored in the PriorityQueue.

        :return:            None.
        """
        self._data.add(priority, value)

    def dequeue(self) -> tuple:
        """
        Removes the first item in the PriorityQueue and returns its value and priority as a tuple.

        :param:             None.

        :return:            Tuple containing the priority and value of the first item in the PriorityQueue.
        """
        return self._data.remove_min()

    def is_empty(self) -> bool:
        """
        Returns True if PriorityQueue is empty, otherwise returns False (if not empty).

        :param:     None.

        :return:    Boolean. True if empty, False if not empty.
        """
        return self._data.is_empty()
