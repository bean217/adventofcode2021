def read_heightmap(fname):
    heightmap = []
    with open(fname) as f:
        for line in f:
            heightmap += [[int(char) for char in line.strip()]]
    return heightmap


def get_total_risk(hm, y_dim, x_dim):
    total_risk = 0
    for j in range(y_dim):
        for i in range(x_dim):
            adj = []
            if i > 0:
                adj += [hm[j][i-1]]
            if i < x_dim - 1:
                adj += [hm[j][i+1]]
            if j > 0:
                adj += [hm[j-1][i]]
            if j < y_dim - 1:
                adj += [hm[j+1][i]]
            #print(hm[j][i])
            #print(f'\t{adj}')
            isLowPoint = True
            for val in adj:
                isLowPoint = isLowPoint and hm[j][i] < val
            if isLowPoint:
                total_risk += hm[j][i] + 1
                #print('\t isLowPoint')
    return total_risk

def display(hm):
    for row in hm:
        for val in row:
            if val == 10:
                print('-', end=" ")
            else:
                print(val, end=" ")
        print()

def get_largest_basins_product(hm, y_dim, x_dim):
    # max_three[0] = largest, max_three[2] = smallest
    max_three = []
    for j in range(y_dim):
        for i in range(x_dim):
            # has already been visited or is high point
            if hm[j][i] >= 9:
                continue
            # otherwise
            # find adjacents that are not high points
            adj = [(j, i)]
            size = 0
            # mark as visited
            hm[j][i] = 10
            while len(adj) != 0:
                y, x = adj.pop()
                size += 1
                if x > 0:
                    if hm[y][x-1] < 9:
                        adj += [(y, x-1)]
                        # mark as visited
                        hm[y][x-1] = 10
                if x < x_dim - 1:
                    if hm[y][x+1] < 9:
                        adj += [(y, x+1)]
                        # mark as visited
                        hm[y][x+1] = 10
                if y > 0:
                    if hm[y-1][x] < 9:
                        adj += [(y-1, x)]
                        # mark as visited
                        hm[y-1][x] = 10
                if y < y_dim - 1:
                    if hm[y+1][x] < 9:
                        adj += [(y+1, x)]
                        # mark as visited
                        hm[y+1][x] = 10
            max_three += [size]
    # sort and slice top three in list
    max_three.sort(reverse=True)
    max_three = max_three[:3]
    return max_three[0] * max_three[1] * max_three[2]

def main():
    fname = 'input'
    heightmap = read_heightmap(fname)
    size_y = len(heightmap)
    size_x = len(heightmap[0])
    print(f'Dimensions: (y: {size_y}, x: {size_x})')
    if size_x <= 20 and size_y <= 10:
        display(heightmap)
    risk_level_sum = get_total_risk(heightmap, size_y, size_x)
    print(f'Total Risk Sum: {risk_level_sum}')
    max_basins_product = get_largest_basins_product(heightmap, size_y, size_x)
    print(f'Largest Three Basins Product: {max_basins_product}')


if __name__ == "__main__":
    main()