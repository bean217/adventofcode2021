# using DFS (uses a stack), modified for large and little caves


def display(graph):
    for key in graph.keys():
        print(f'{key}: {graph[key]}')


def copy(arr):
    a_copy = []
    for elem in arr:
            a_copy += [elem]
    return a_copy


def is_small_cave(cave_str):
    return ord(cave_str[0]) >= ord('a') and ord(cave_str[0]) <= ord('z')


def evaluate_paths(graph, stack, visited=[], curr_path=[], paths=[]):
    temp_stack = []
    curr = stack.pop()
    curr_path += [curr]
    if is_small_cave(curr):
        visited += [curr]
    if curr == "end":
        #print(curr_path)
        paths += [curr_path]
        return None
    for node in graph[curr]:
        if node not in visited:
            temp_stack += [node]
            #print("added")
            evaluate_paths(graph, temp_stack, copy(visited), copy(curr_path), paths)
    return paths


def construct_graph(fname):
    graph = dict()
    with open(fname) as f:
        for line in f:
            line = line.strip().split("-")
            if line[0] not in graph.keys():
                graph[line[0]] = []
            if line[1] not in graph.keys():
                graph[line[1]] = []
            if line[1] != "start" and line[0] != "end":
                graph[line[0]] += [line[1]]
            if line[0] != "start" and line[1] != "end":
                graph[line[1]] += [line[0]]
    return graph

def main():
    fname = 'input'
    graph = construct_graph(fname)
    display(graph)
    stack = []
    stack.append("start")
    paths = evaluate_paths(graph, stack)
    for path in paths:
        if len(path) > 7:
            print(path[:7] + ['...'])
        else:
            print(path)
    print(f'{len(paths)} paths.')


if __name__ == "__main__":
    main()