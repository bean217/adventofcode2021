import heapq


def read_graph(fname):
    graph = []
    with open(fname) as f:
        for line in f:
            graph += [[int(val) for val in line.strip()]]
    sy = len(graph)
    sx = len(graph[0])
    chitons = {}
    for y in range(sy):
        for x in range(sx):
            chitons[(x, y)] = graph[y][x]
    
    with open(fname) as f:
        r = f.read()
    augmented = {}
    graph = [[int(x) for x in y]*5 for y in r.split('\n')]*5
    for x in range(sx*5):
        for y in range(sy*5):
            augmented[(x, y)] = ( (x//sx) + (y//sy) + graph[y][x] ) if ( (x//sx) + (y//sy) + graph[y][x] ) <= 9 else ( (x//sx) + (y//sy) + graph[y][x] ) % 10 + 1
    return augmented, chitons, sx, sy


def dijkstras(chitons, sx, sy):
    # (x, y)
    start = (0, 0)
    end = (sx-1, sy-1)
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    distances = {}
    for k in chitons.keys():
        distances[k] = float('inf')
    distances[start] = 0
    # pq contains (current distance to node, node position)
    pq = [(0, start)]
    while len(pq) > 0:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            # current distance to node is greater than the stored distances, so we dont need to evaluate it
            continue
        x, y = curr_node
        for dx, dy in d:
            x1 = x+dx
            y1 = y+dy
            if 0 <= x1 <= end[0] and 0 <= y1 <= end[1]:
                cost = curr_dist + chitons[(x1, y1)]
                if cost < distances[(x1, y1)]:
                    distances[(x1, y1)] = cost
                    heapq.heappush(pq, (cost, (x1, y1)))
    return distances[end]


def main():
    fname = 'input'
    augmented, chitons, sx, sy = read_graph(fname)
    dist = dijkstras(chitons, sx, sy)
    print(f'Risk: {dist}')
    dist = dijkstras(augmented, sx*5, sy*5)
    print(f'Risk: {dist}')


if __name__ == "__main__":
    main()