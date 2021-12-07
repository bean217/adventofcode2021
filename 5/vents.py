from enum import Enum

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

class LineType(Enum):
    DIAG = 0
    VERT = 1
    HORIZ = 2

# returns true if vent orientation is horizontal
def get_line_type(positions):
    del_x = positions[0][0] - positions[1][0]
    del_y = positions[0][1] - positions[1][1]
    if del_x < 0:
        del_x *= -1
    if del_y < 0:
        del_y *= -1
    if del_x > 0 and del_y > 0:
        return LineType.DIAG
    elif del_y > 0 and del_x == 0:
        return LineType.VERT
    else:
        return LineType.HORIZ

def get_custom_range(positions):
    del_x = positions[1][0] - positions[0][0]
    del_y = positions[1][1] - positions[0][1]
    if del_x == 0 and del_y == 0:
        return range(1)
    if del_x == 0:
        if del_y < 0:
            return range(positions[0][1], positions[0][1] + del_y - 1, -1)
        return range(positions[0][1], positions[1][1] + 1)
    if del_y == 0:
        if del_x < 0:
            return range(positions[0][0], positions[0][0] + del_x - 1, -1)
        return range(positions[0][0], positions[1][0] + 1)

def get_diag_custom_range(positions):
    del_x = positions[1][0] - positions[0][0]
    del_y = positions[1][1] - positions[0][1]
    range_horiz = None
    range_vert = None
    if del_y < 0:
        range_vert = range(positions[0][1], positions[0][1] + del_y - 1, -1)
    else:
        range_vert = range(positions[0][1], positions[1][1] + 1)
    if del_x < 0:
        range_horiz = range(positions[0][0], positions[0][0] + del_x - 1, -1)
    else:
        range_horiz = range(positions[0][0], positions[1][0] + 1)
    return zip(range_vert, range_horiz)
    

def display(field):
    for row in field:
        for val in row:
            if val == 0:
                print(". ", end="")
            else:
                print(f'{val} ', end="")
        print()

def populate_field(filename, size_x, size_y):
    field = [[0]*size_x for _ in range(size_y)]
    with open(filename) as f:
        for line in f:
            line = process_line(line)
            line_type = get_line_type(line)
            if line_type != LineType.DIAG:
                cust_range = get_custom_range(line)
                #print(f'({line[0][0]}, {line[0][1]}) -> ({line[1][0]}, {line[1][1]})')
                #print(f'\tLT: {line_type}')
                #print(f'\t{cust_range}')
                
                if line_type == LineType.HORIZ:
                    for i in cust_range:
                        field[line[0][1]][i] += 1
                else:
                    # line_type == LineType.VERT
                    for i in cust_range:
                        field[i][line[0][0]] += 1
            else:
                cust_range = get_diag_custom_range(line)
                #print(f'({line[0][0]}, {line[0][1]}) -> ({line[1][0]}, {line[1][1]})')
                #print(f'\tLT: {line_type}')
                #print(f'\t{cust_range}')
                for j, i in cust_range:
                    field[j][i] += 1

        #display(field)
        return field

def count_intersects(field):
    count = 0
    for row in field:
        for var in row:
            if var > 1:
                count += 1
    return count

def main():
    fname = 'input'
    size_x, size_y = get_dimensions(fname)
    print(f'Max X: {size_x}')
    print(f'Max Y: {size_y}')
    field = populate_field(fname, size_x, size_y)
    print(count_intersects(field))


if __name__ == "__main__":
    main()