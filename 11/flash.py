#              TL         T       TR       L        R       BL       B       BR
ADJ_OFFSET = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def display(field):
    for row in field:
        print(row)


def get_init_field(fname):
    field = []
    with open(fname) as f:
        for line in f:
            field += [[int(char) for char in line.strip()]]
    return field


def isValidPos(y, x, dim_y, dim_x):
    # print(y, x)
    return y >= 0 and y < dim_y and x >= 0 and x < dim_x


def step_and_count_flashes(field, y_dim, x_dim):
    stack = []
    flashed_stack = []
    # level up
    for j in range(y_dim):
        for i in range(x_dim):
            field[j][i] += 1
            if field[j][i] > 9:
                stack.append((j, i))
    #display(field)
    #print()
    # consider flashes
    while len(stack) > 0:
        y, x = stack.pop()
        flashed_stack.append((y, x))
        # level up adj
        # print(stack)
        # print(f'popped: {y, x}')
        for dy, dx in ADJ_OFFSET:
            if isValidPos(y+dy, x+dx, y_dim, x_dim) and field[y+dy][x+dx] < 10:
                # print(f'({y+dy}, {x+dx}) is valid')
                field[y+dy][x+dx] += 1
                if field[y+dy][x+dx] == 10:
                    stack.append((y+dy, x+dx))
    count = len(flashed_stack)
    while len(flashed_stack) > 0:
        y, x = flashed_stack.pop()
        field[y][x] = 0
    display(field)
    return field, count


def count_flashes(field, rounds, y_dim, x_dim):
    flashes = 0
    curr_field = field
    for _ in range(rounds):
        temp_flashes = 0
        curr_field, temp_flashes = step_and_count_flashes(curr_field, y_dim, x_dim)
        flashes += temp_flashes
        print()
    return flashes

def main():
    fname = 'input'
    rounds = 100
    field = get_init_field(fname)
    display(field)
    print()
    y_dim = len(field)
    x_dim = len(field[0])
    flashes = count_flashes(field, rounds, y_dim, x_dim)
    print(f'Flashes: {flashes}')

if __name__ == "__main__":
    main()