#





#

 
import Point


class Node:
    def __init__(self):
        
        self.p = None
        self.next = None

class Tour:
    #
    # Initialize an empty linked list. 
    # 
    def __init__(self):
        self.start = None
        
    def show(self):
        print(self.start.p.toString())
        node = self.start.next
        while node != self.start:
            print(node.p.toString())
            node = node.next
        
    def draw(self):
        node = self.start.next
        self.start.p.draw()
        self.start.p.drawTo(node.p)
        while node != self.start:
            node.p.draw()
            node.p.drawTo(node.next.p)
            node = node.next
            
    def size(self):
        count = 0
        node = self.start
        working = True
        while working:
            count += 1
            node = node.next()
            if node == self.start:
                working = False
        return count
            
    def distance(self):
        distance = self.start.p.distanceTo(self.start.next.p)
        node = self.start.next
        while node != self.start:
            distance += node.p.distanceTo(node.next.p)
            node = node.next
        return distance
        
    def insertInOrder(self, p):
        newNode = Node()
        newNode.p = p
        if self.start == None:
            self.start = newNode
        else:
            lastNode = self.start
            while lastNode.next != self.start:
                lastNode = lastNode.next
            lastNode.next = newNode
        newNode.next = self.start
        
    


        
            
    
    