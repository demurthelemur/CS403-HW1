import random
import conset
import threading

n = 3
nodes = []

class Node(threading.Thread):
    def __init__(self, id, n):
      threading.Thread.__init__(self)
      self.mailbox = conset.ConSet()
      self.id = id
      self.n = n
      self.leader = None
      self.round = 1
      
    def mailBoxNotEmpty(self, messages):

      if len(messages) < self.n:
            return True
        
      msg = self.mailbox._head
      if msg is None:
          return False

      while msg is not None:
          if msg.data[2] == self.round:
            return True
          msg = msg.next
    
    def findLeader(self, messages):
      currentMax = (0, 0, 0)
      for message in messages:
        if message[1] == currentMax[1]:
          currentMax = (-1, 0, 0)
          return currentMax
        elif message[1] > currentMax[1]:
          currentMax = message
      return currentMax

    def nodeWork(self, n):
      while self.leader == None:
        randomInt = random.randint(0, self.n * self.n)
        message = (self.id, randomInt, self.round)
        for node in nodes:
          node.mailbox.add(message)
        messages = []
        while self.mailBoxNotEmpty(messages):
          messages.append(self.mailbox.remove()) 
        leaderID, leaderN, roundNo = self.findLeader(messages)
        if leaderID == -1:
          print(f'Node {self.id} could not decide on the leader and moves to the round {self.round + 1}.')
          self.round += 1
        else:
          self.leader = leaderID
          print(f'Node {self.id} decided {leaderID} as the leader (with n={leaderN})')
    def run(self):
      self.nodeWork(self.n)

for i in range (n):
  nodes.append(Node(i,n))

if __name__ == '__main__':
    
    for node in nodes:
        node.start()

    
          
      
