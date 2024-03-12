#Singly-list without tail pointer

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def size(self):
    sizeCounter = 0
    if(self.head):
      current_node = self.head
      while(current_node):
        size = size+1
        current_node = current_node.next
      return sizeCounter
    else:
      return 0
    
  def empty(self):
    if(self.head is None):
      return True
    else:
      return False
    
  def value_at(self, index):
    position = 0
    current_node = self.head
    if(position == index):
      return current_node.data
    else:
      while(current_node):
        current_node = current_node.next
        position += 1
        if(position == index):
          return current_node.data
      return print('Index not found')

  def push_front(self, data):
    if(self.head is None):
      self.head = Node(data)
    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node
  
  def pop_front(self):
    if(self.head is None):
      print("Not items in the linked list")
    else:
      current_node = self.head
      self.head = current_node.next

  def push_back(self, data):
    if(self.head is None):
      self.head = Node(data)
    else:
      current_node = self.head
      while(current_node.next):
        current_node = current_node.next
      new_node = Node(data)
      current_node.next = new_node
    
  def pop_back(self):
    if(self.head is None):
      print('Not items in the linked list')
    else:
      current_node = self.head
      while(current_node.next.next):
        current_node = current_node.next
      current_node.next = None
  
  def front(self):
    if(self.head is None):
      print('Not items in the linked list')
    else:
      return self.head.data
  
  def back(self):
    if(self.head is None):
      print('Not items in the linked list')
    else:
      current_node = self.head
      while(current_node.next):
        current_node = current_node.next
      return current_node.data
    
  def insert(self, index, value):
    position = 0
    current_node = self.head
    if(position == index):
      new_node = Node(value)
      new_node.next = current_node
      self.head = new_node
    else:
      while(current_node.next):
        if (position == index-1):
          new_node = Node(value)
          new_node.next = current_node.next
          current_node.next = new_node
          return
        position += 1
        current_node = current_node.next
      print('index not found')

  def erase(self, index):
    position = 0
    current_node = self.head
    if(position == index):
      self.head = current_node.next
    else:
      while(current_node.next):
        if (position == index-1):
          current_node.next = current_node.next.next
          return
        position += 1
        current_node = current_node.next
      print('index not found')


  # returns the value of the node at the nth position from the end of the list
  def value_n_from_end(self, n):
    pass

  # reverse the list
  def reverse():
    pass

  # removes the first item in the list with this value
  def remove_value(self, value):
    current_node = self.head
    while(current_node):
      if(current_node.next.data == value):
        current_node.next = current_node.next.next
        return
      current_node = current_node.next
    print('Value not found in the linked list')

  def printLL(self):
    current_node = self.head
    while(current_node):
      print(current_node.data)
      current_node = current_node.next

llist = LinkedList()
print(llist.empty())

llist.push_back(1)
llist.push_back(2)
llist.push_back(3)
llist.push_back(5)
llist.push_back(6)
llist.push_back(10)
llist.push_back(15)
llist.insert(0, 9)

llist.printLL()