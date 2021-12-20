import sys

class Node:
    def __init__(self, value, y, x):
        self.val = value
        self.pos = (y, x)
        self.dist = sys.maxsize
        self.path = None
        self.adj = []

    def __lt__(self, other):
        return self.dist < other.dist
    
    def __str__(self):
        return f'[{self.val}]{self.pos}'


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def add(self, node):
        self.size += 1
        self.heap += [node]
        index = self.size - 1
        if index != 0:
            while self.heap[(index-1)//2].dist > node.dist:
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
        for j in range(self.size_y):
            for i in range(self.size_x):
                self.graph[j][i] = Node(self.graph[j][i], j, i)
        for j in range(self.size_y):
            for i in range(self.size_x):
                node = self.graph[j][i]
                # y direction
                if j > 0:
                    node.adj += [self.graph[j-1][i]]
                if j < self.size_y - 1:
                    node.adj += [self.graph[j+1][i]]
                # x direction
                if i > 0:
                    node.adj += [self.graph[j][i-1]]
                if i < self.size_x - 1:
                    node.adj += [self.graph[j][i+1]]
        self.visited = set()
    
    def run_dijkstras(self):
        # (y, x)
        end = None
        q = MinHeap()
        node = self.graph[0][0]
        node.dist = 0
        q.add(node)
        
        #print([val for val in self.visited])
        while q.size > 0:
            v = q.remove()
            #print([val for val in self.visited])
            #print(v)
            if (f'{v.pos}' not in self.visited):
                if v.pos[0] == self.size_y-1 and v.pos[1] == self.size_x-1:
                    end = v
                self.visited.add(f'{v.pos}')
            for w in v.adj:
                if v.dist + w.val < w.dist:
                    w.dist = v.dist + w.val
                    w.path = v
                if f'{w.pos}' not in self.visited:
                    if w not in q.heap:
                        q.add(w)
                    else:
                        q.heap.sort()
        curr = end
        string = ""
        cost = 0
        print(end.path)
        while curr != None:
            if curr.path != None:
                cost += curr.val
            string = f' {curr.__str__()} >' + string
            curr = curr.path
        print(string)
        return end.dist


def read_graph(fname):
    graph = []
    with open(fname) as f:
        for line in f:
            graph += [[int(val) for val in line.strip()]]
    return graph


def main():
    fname = 'input'
    graph = Graph(fname)
    #for row in graph:
    #    print(row)
    res = graph.run_dijkstras()
    print(f'Risk: {res}')

if __name__ == "__main__":
    main()