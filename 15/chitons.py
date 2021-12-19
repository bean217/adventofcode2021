import sys

class Node:
    def __init__(self, value, y, x):
        self.val = value
        self.pos = (y, x)
        self.dist = sys.maxsize
        self.path = None
    
    def __str__(self):
        return f'[{self.val}]@{self.pos}'


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

class Graph:
    def __init__(self, fname):
        self.graph = []
        with open(fname) as f:
            for line in f:
                self.graph += [[int(val) for val in line.strip()]]
        self.size_y = len(self.graph)
        self.size_x = len(self.graph[0])
        self.visited = set()
    
    def run_dijkstras(self):
        # (y, x)
        start = (0, 0)
        end = None
        q = MinHeap()
        node = Node(self.graph[0][0], 0, 0)
        node.dist = 0
        q.add(node)
        
        #print([val for val in self.visited])
        while q.size > 0:
            v = q.remove()
            
            #print([val for val in self.visited])
            #print(v)
            if (f'{v.pos}' not in self.visited):
                if v.pos[0] == len(self.graph)-1 and v.pos[1] == len(self.graph[0])-1:
                    end = v
                self.visited.add(f'{v.pos}')
                adj = []
                # y direction
                if v.pos[0] > 0:
                    adj += [Node(self.graph[v.pos[0]-1][v.pos[1]], v.pos[0]-1, v.pos[1])]
                if v.pos[0] < self.size_y - 1:
                    adj += [Node(self.graph[v.pos[0]+1][v.pos[1]], v.pos[0]+1, v.pos[1])]
                # x direction
                if v.pos[1] > 0:
                    adj += [Node(self.graph[v.pos[0]][v.pos[1]-1], v.pos[0], v.pos[1]-1)]
                if v.pos[1] < self.size_x - 1:
                    adj += [Node(self.graph[v.pos[0]][v.pos[1]+1], v.pos[0], v.pos[1]+1)]
            for w in adj:
                w.dist = v.dist + w.val
                w.path = v
                if f'{w.pos}' not in self.visited:
                    q.add(w)
        curr = end
        string = ""
        while curr != None:
            string += f' {curr.pos} >'
            curr = curr.path
        print(string)
        return end.dist + self.graph[0][0]


def read_graph(fname):
    graph = []
    with open(fname) as f:
        for line in f:
            graph += [[int(val) for val in line.strip()]]
    return graph


def main():
    fname = 'test'
    graph = Graph(fname)
    #for row in graph:
    #    print(row)
    res = graph.run_dijkstras()
    print(f'Risk: {res}')

if __name__ == "__main__":
    main()