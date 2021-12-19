class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def add(self, val):
        self.size += 1
        self.heap += [val]
        index = self.size - 1
        if index != 0:
            while self.heap[(index-1)//2] > val:
                temp = self.heap[(index-1)//2]
                self.heap[(index-1)//2] = val
                self.heap[index] = temp
                index = (index-1)//2
                if index == 0:
                    break

    def remove(self):
        if self.size > 0:
            self.size -= 1
            val = self.heap[0]
            bottom = self.heap.pop()
            if self.size > 0:
                self.heap[0] = bottom
                index = 0
                while index < self.size:
                    print(index)
                    i_temp = 0

                    left_val = None
                    right_val = None

                    if (index*2)+1 < self.size:
                        left_val = self.heap[(index*2)+1]
                    if (index*2)+2 < self.size:
                        right_val = self.heap[(index*2)+2]

                    if left_val == None and right_val == None:
                        break
                    elif right_val == None:
                        i_temp = (index*2)+1 
                    else:
                        if left_val < right_val:
                            i_temp = (index*2)+1
                        else:
                            i_temp = (index*2)+2
                    if self.heap[index] > self.heap[i_temp]:
                        temp = self.heap[index]
                        self.heap[index] = self.heap[i_temp]
                        self.heap[i_temp] = temp
                        index = i_temp
                    else:
                        break        
            return val

    def __str__(self):
        return self.heap.__str__()

class Graph:
    def __init__(self, fname):
        self.graph = []
        with open(fname) as f:
            for line in f:
                self.graph += [[int(val) for val in line.strip()]]
        self.visited = set()
    
    def run_dijkstras(self):
        # (y, x)
        start = (0, 0)
        end = (len(self.graph), len(self.graph[0]))
        q = MinHeap()
        

def read_graph(fname):
    graph = []
    with open(fname) as f:
        for line in f:
            graph += [[int(val) for val in line.strip()]]
    return graph


def main():
    fname = 'test'
    graph = read_graph(fname)
    #for row in graph:
    #    print(row)
    heap = MinHeap()
    

if __name__ == "__main__":
    main()