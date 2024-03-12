from collections import deque

class Queue:
  def __init__(self):
    self.data = deque()

  def enqueue(self, node):
    self.data.append(node)
  
  def dequeue(self):
    self.data.popleft()

# fifo = Queue()
# fifo.enqueue(1)
# fifo.enqueue(2)
# fifo.enqueue(3)
# fifo.enqueue(4)
# fifo.enqueue(5)

# fifo.dequeue()
# print(fifo.data)
# fifo.dequeue()
# print(fifo.data)

class Queue_Arr:
  def __init__(self, arr_size) -> None:
    self.data = [None for _ in range(arr_size)]
    self.read = 0
    self.write = 0
    self.capacity = arr_size

  def enqueue(self, value):
    if self.write + 1 == self.read:
      print('There is not space for more queues')
      return
    if self.write == len(self.data) - 1 and self.data[0] is None:
      self.data[self.write] = value
      self.write = 0
      return
    elif self.write == len(self.data) - 1 and self.data[0] is not None:
      print('There is not space')
      return
    self.data[self.write] = value
    self.write += 1

  def dequeue(self):
    if self.read == self.write:
      print('There are no items in the queue')
      return
    if self.read == len(self.data) - 1:
      self.data[self.read] = None
      self.read = 0
      return
    self.data[self.read] = None
    self.read += 1
  
  def empty(self):
    if self.write == self.read:
      return True
    else:
      return False
  
  def full(self):
    if self.write + 1 == self.read:
      return True
    elif self.write == len(self.data) - 1 and self.read == 0:
      return True
    else:
      return False


# queue_with_arr = Queue_Arr(10)
# queue_with_arr.enqueue(50)
# queue_with_arr.enqueue(3)
# queue_with_arr.enqueue(80)
# queue_with_arr.enqueue(15)
# queue_with_arr.enqueue(53)
# queue_with_arr.enqueue(33)
# queue_with_arr.enqueue(36)
# queue_with_arr.enqueue(223)
# queue_with_arr.enqueue(999)
# print(queue_with_arr.data)
# print(queue_with_arr.empty())
# print(queue_with_arr.full())

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue_Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def enqueue(self, value):
    if self.head is None:
      self.head = Node(value)
      self.tail = self.head
    else:
      new_node = Node(value)
      self.tail.next = new_node
      self.tail = new_node

  def dequeue(self):
    if self.head == self.tail:
      self.head, self.tail = None, None
    current_node = self.head
    self.head = current_node.next

  def empty(self):
    if self.tail is None:
      return True
    else:
      return False
  
  def printll(self):
    current_node = self.head
    print_arr = []
    while(current_node):
      print_arr.append(current_node.data)
      current_node = current_node.next
    print(print_arr)

queue_with_linked_list = Queue_Linked_List()
queue_with_linked_list.enqueue(5)
queue_with_linked_list.enqueue(3)
queue_with_linked_list.enqueue(2)
queue_with_linked_list.enqueue(7)
queue_with_linked_list.enqueue(9)
queue_with_linked_list.enqueue(2)
queue_with_linked_list.printll()
queue_with_linked_list.dequeue()
queue_with_linked_list.printll()
queue_with_linked_list.dequeue()
queue_with_linked_list.printll()
queue_with_linked_list.dequeue()
queue_with_linked_list.printll()
queue_with_linked_list.enqueue(7)
queue_with_linked_list.enqueue(2)
queue_with_linked_list.printll()
