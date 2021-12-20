import sys

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def add(self, node):
        self.size += 1
        self.heap += [node]
        index = self.size - 1
        if index != 0:
            while self.heap[(index-1)//2].val > node.val:
                temp = self.heap[(index-1)//2]
                self.heap[(index-1)//2] = node
                self.heap[index] = temp
                index = (index-1)//2
                if index == 0:
                    break

    def remove(self):
        if self.size > 0:
            self.size -= 1
            node = self.heap[0]
            bottom = self.heap.pop()
            if self.size > 0:
                self.heap[0] = bottom
                index = 0
                while index < self.size:
                    i_temp = 0

                    left_node = None
                    right_node = None

                    if (index*2)+1 < self.size:
                        left_node = self.heap[(index*2)+1]
                    if (index*2)+2 < self.size:
                        right_node = self.heap[(index*2)+2]

                    if left_node == None and right_node == None:
                        break
                    elif right_node == None:
                        i_temp = (index*2)+1 
                    else:
                        if left_node.val < right_node.val:
                            i_temp = (index*2)+1
                        else:
                            i_temp = (index*2)+2
                    if self.heap[index].val > self.heap[i_temp].val:
                        temp = self.heap[index]
                        self.heap[index] = self.heap[i_temp]
                        self.heap[i_temp] = temp
                        index = i_temp
                    else:
                        break        
            return node

    def __str__(self):
        return self.heap.__str__()


class Position:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    
    def __str__(self):
        return f'({self.y}, {self.x})'

class Node:
    def __init__(self, value, y, x):
        self.val = value
        self.pos = Position(y, x)
        self.dist = sys.maxsize
        self.path = None
        self.adj = []
        self.visited = False

    def __lt__(self, other):
        return self.dist < other.dist
    
    def __str__(self):
        return f'[{self.val}]{self.pos}'


class Graph:
    def __init__(self, fname):
        self.graph = []
        with open(fname) as f:
            for line in f:
                self.graph += [[int(val) for val in line.strip()]]
        self.size_y = len(self.graph)
        self.size_x = len(self.graph[0])
        for j in range(self.size_y):
            for i in range(self.size_x):
                self.graph[j][i] = Node(self.graph[j][i], j, i)
        for j in range(self.size_y):
            for i in range(self.size_x):
                node = self.graph[j][i]
                # y direction
                if node.pos.y > 0:
                    node.adj += [self.graph[j-1][i]]
                if node.pos.y < self.size_y - 1:
                    node.adj += [self.graph[j+1][i]]
                # x direction
                if node.pos.x > 0:
                    node.adj += [self.graph[j][i-1]]
                if node.pos.x < self.size_x - 1:
                    node.adj += [self.graph[j][i+1]]
        for row in self.graph:
            print([node.__str__() for node in row])
            for node in row:
                print(f'\t{[w.__str__() for w in node.adj]}')

    def run_dijkstras():
        end = None

def main():
    fname = 'st'
    graph = Graph(fname)
    q = MinHeap()
    q.add(Node(3, 0, 0))
    q.add(Node(1, 0, 0))
    q.add(Node(2, 0, 0))
    print([n.__str__() for n in q.heap])

if __name__ == "__main__":
    main()