import array as arr

class Stack:
    def __init__(self, capacity):
        self.data = arr.array('i', [0] * capacity)
        self.top = -1

    def push(self, value):
        if self.top < len(self.data) - 1:
            self.top += 1
            self.data[self.top] = value
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top >= 0:
            popped = self.data[self.top]
            self.data[self.top] = 0
            self.top -= 1
            return popped
        else:
            print("Stack Underflow")
            return None

class Queue:
    def __init__(self, capacity):
        self.data = arr.array('i', [0] * capacity)
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = capacity

    def enqueue(self, value):
        if self.size < self.capacity:
            self.data[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1
        else:
            print("Queue Overflow")

    def dequeue(self):
        if self.size > 0:
            dequeued = self.data[self.front]
            self.data[self.front] = 0
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return dequeued
        else:
            print("Queue Underflow")
            return None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, capacity):
        self.nodes = [Node(0) for _ in range(capacity)]
        self.head = -1
        self.next_available = 0

    def insert_node(self, value):
        if self.next_available < len(self.nodes):
            self.nodes[self.next_available].data = value
            if self.head == -1:
                self.head = self.next_available
            else:
                current = self.head
                while self.nodes[current].next is not None:
                    current = self.nodes[current].next
                self.nodes[current].next = self.next_available
            self.next_available += 1
        else:
            print("Singly Linked List is full.")

    def display_linked_list(self):
        if self.head == -1:
            print("Linked list is empty")
            return

        current = self.head
        while current is not None:
            print(self.nodes[current].ssdata, end=" -> ")
            current = self.nodes[current].next

        print("NULL")

capacity = 100

stack = Stack(capacity)
queue = Queue(capacity)
linked_list = SinglyLinkedList(capacity)

stack.push(10)
stack.push(20)
print(stack.pop())
print(stack.pop())

queue.enqueue(30)
queue.enqueue(40)
print(queue.dequeue())
print(queue.dequeue())

linked_list.insert_node(50)
linked_list.insert_node(60)
linked_list.display_linked_list()
