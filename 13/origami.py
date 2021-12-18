def get_dimensions(fname):
    max_x = 0
    max_y = 0
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            x, y = line.split(',')
            x, y, = int(x), int(y)
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    size_x = max_x + 1
    size_y = max_y + 1
    return size_x, size_y


def read_data(fname, size_x, size_y):
    paper = [['.'] * size_x for _ in range(size_y)]
    instructions = []
    with open(fname) as f:
        # gather dots
        count = 0
        for line in f:
            line = line.strip()
            if line == "":
                break
            count += 1
            x, y = line.split(',')
            x, y = int(x), int(y)
            paper[y][x] = '#'
        print(f'{count} total starting dots')
        # gather instructions
        for line in f:
            axis, val = line.strip().split()[2].split('=')
            val = int(val)
            instructions += [(axis, val)]
    return paper, instructions


def abs(x):
    if x < 0:
        return -1 * x
    return x


def display(paper):
    count = 0
    for j in range(len(paper)):
        for i in range(len(paper[0])):
            if paper[j][i] == '#':
                count += 1
            print(paper[j][i], end="")
        print()
    print(f'{count} Dots.')
    print()


def fold_vert(paper, axis, dim_x, dim_y):
    for j in range(axis):
        for i in range(dim_x):
            if paper[j][i] == '#' or paper[dim_y - 1 - j][i] == '#':
                paper[j][i] = '#'
    # 11 // 2 = 5 01234 5 6789X
    # 10 // 2 = 5 01234 56789
    return paper[:axis]



def fold_horiz(paper, axis, dim_x, dim_y):
    for j in range(dim_y):
        for i in range(axis):
            if paper[j][i] == '#' or paper[j][dim_x - 1 - i] == '#':
                paper[j][i] = '#'
    # 11 // 2 = 5 01234 5 6789X
    # 10 // 2 = 5 01234 56789
    return [line[:axis] for line in paper]


def fold_paper(paper, instructions, dim_x, dim_y):
    display(paper)
    size_x = dim_x
    size_y = dim_y
    curr_paper = paper
    for instruction in instructions:
        if instruction[0] == 'y':
            curr_paper = fold_vert(curr_paper, instruction[1], size_x, size_y)
        else:
            curr_paper = fold_horiz(curr_paper, instruction[1], size_x, size_y)
        size_y = len(curr_paper)
        size_x = len(curr_paper[0])
        display(curr_paper)
        print(f"size_x: {size_x}, size_y: {size_y}")


def perform_instructions(paper, instructions, dim_x, dim_y):
    size_x = dim_x
    size_y = dim_y
    curr_paper = paper
    for instruction in instructions:
        high = -instruction[1]
        low = instruction[1]
        if instruction[0] == 'x':
            high += size_x
        else: # instruction[0] == 'y'
            high += size_y
        cust_range = abs(low)
        if abs(high) < cust_range:
            cust_range = abs(high)
        print(f'cust_range: {cust_range}')
        if instruction[0] == 'x':
            mod = 0
            if (size_x % 2 == 0):
                mod = 1
            for i in range(cust_range):
                for j in range(size_y):
                    if curr_paper[j][instruction[1] + i] == '#' or curr_paper[j][instruction[1] - i] == '#':
                        curr_paper[j][instruction[1] - i] = '#'
            for j in range(len(curr_paper)):
                curr_paper[j] = curr_paper[j][:instruction[1] + mod]
            size_x = len(curr_paper[0])
        else: # instruction[0] == 'y'
            mod = 0
            if (size_y % 2 == 0):
                mod = 1
            for j in range(cust_range):
                #print(j)
                for i in range(size_x):
                    #print(f'\t{i}')
                    if curr_paper[instruction[1] + j][i] == '#' or curr_paper[instruction[1] - j][i] == '#':
                        curr_paper[instruction[1] - j][i] = '#'
            curr_paper = curr_paper[:instruction[1] + mod]
            size_y = len(curr_paper)
        print()
        display(curr_paper)
        print(f'({len(curr_paper)}, {len(curr_paper[0])})')
    return curr_paper

def main():
    fname = 'test'
    dim_x, dim_y = get_dimensions(fname)
    print(f'X-dim: {dim_x}\nY-dim: {dim_y}')
    paper, instructions = read_data(fname, dim_x, dim_y)
    #for line in instructions:
    #    print(line)
    #display(paper)
    #paper = perform_instructions(paper, instructions, dim_x, dim_y)
    fold_paper(paper, instructions, dim_x, dim_y)

if __name__ == "__main__":
    main()