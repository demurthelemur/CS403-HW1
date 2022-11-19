import random
import threading
import time

class setItem:
  def __init__(self, x):
        self.data = x
        self.next = None

class ConSet:
  def __init__(self) -> None:
    self._set = []
    self._lock = threading.Lock()
    self._head = None

  def add(self, item):
    newItem = setItem(item)
    if self._head == None:
      self._lock.acquire()
      self._head = newItem
      self._lock.release()
      return
    
    self._lock.acquire()
    temp = self._head
    while temp.next != None:
      temp = temp.next
    temp.next = newItem
    newItem.prev = temp
    self._lock.release()

  def remove(self):
    while True:
      self._lock.acquire()
      if self._head == None:
        self._lock.release()
        time.sleep(0.001)
      elif self._head.next == None:
        temp = self._head.data
        self._head = None
        self._lock.release()
        return temp
      else:
        temp = self._head.data
        self._head = self._head.next
        self._lock.release()
        return temp
  
  def print(self):
    temp = self._head
    while temp != None:
      print(temp.data)
      temp = temp.next

