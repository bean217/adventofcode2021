def process_line(line_str):
    line = line_str.strip().split(' -> ')
    line = [pos.split(',') for pos in line]
    for pos in line:
        for i in range(2):
            pos[i] = int(pos[i])
    return line

def get_dimensions(filename):
    max_x = 0
    max_y = 0
    with open(filename) as f:
        for line in f:
            line = process_line(line)
            for pos in line:
                if pos[0] > max_x:
                    max_x = pos[0]
                if pos[1] > max_y:
                    max_y = pos[1]
    return (max_x + 1, max_y + 1)

# returns true if vent orientation is horizontal
def is_horizontal(positions):
    del_y = positions[0][1] - positions[1][1]
    return del_y == 0

def get_custom_range(positions):
    del_x = positions[1][0] - positions[0][0]
    del_y = positions[1][1] - positions[0][1]
    if del_x == 0 and del_y == 0:
        return range(1)
    if del_x == 0:
        if del_y < 0:
            return range()
        return range()

    #TODO: CONTINUE HERE TOMORROW!!!



def populate_field(filename, size_x, size_y):
    field = [[0]*size_x]*size_y
    with open(filename) as f:
        for line in f:
            line = process_line(line)
            if is_horizontal(line):
                pass
            else:
                pass


def main():
    fname = 'test'
    size_x, size_y = get_dimensions(fname)
    print(f'Max X: {size_x}')
    print(f'Max Y: {size_y}')
    field = populate_field(fname, size_x, size_y)


if __name__ == "__main__":
    main()