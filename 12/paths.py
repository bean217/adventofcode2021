# using DFS (uses a stack), modified for large and little caves


def display(graph):
    for key in graph.keys():
        print(f'{key}: {graph[key]}')


def is_small_cave(cave_str):
    return ord(cave_str[0]) >= ord('a') and ord(cave_str[0]) <= ord('z')


def evaluate_paths(graph, stack, visited=[], curr_path=[], paths=[]):
    print(f'visited: {visited}')
    curr = stack.pop()
    curr_path += [curr]
    if is_small_cave(curr):
        visited += [curr]

def construct_graph(fname):
    graph = dict()
    with open(fname) as f:
        for line in f:
            line = line.strip().split("-")
            if line[0] not in graph.keys():
                graph[line[0]] = []
            if line[1] not in graph.keys():
                graph[line[1]] = []
            graph[line[0]] += [line[1]]
            graph[line[1]] += [line[0]]
    return graph

def main():
    fname = 'test1'
    graph = construct_graph(fname)
    display(graph)
    stack = []
    stack.append("start")
    paths = evaluate_paths(graph, stack)
    print(paths)
if __name__ == "__main__":
    main()