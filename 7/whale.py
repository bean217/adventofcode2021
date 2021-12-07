def abs(x):
    if x < 0:
        return x * -1
    return x

def round(x):
    if x - int(x) > 0.5:
        return int(x+1)
    return int(x)

def get_init_crab_pos(filename):
    poses = []
    max_pos = 0
    num_vals = 0
    with open(filename) as f:
        for line in f:
            poses += [int(val) for val in line.strip().split(',')]
    for val in poses:
        if val > max_pos:
            max_pos = val
    pos_freq = [0]*(max_pos + 1)
    for val in poses:
        pos_freq[val] += 1
        num_vals += 1
    isEven = False
    if num_vals % 2 == 0:
        isEven = True
    poses = []
    for i in range(len(pos_freq)):
        poses += [i]*pos_freq[i]
    if isEven:
        median = round((poses[num_vals // 2] + poses[(num_vals // 2) - 1]) / 2) 
    else:
        median = poses[num_vals // 2]
    return (pos_freq, median, max_pos)


def calc_fuel_cost(pos_freq, median):
    total = 0
    for i in range(len(pos_freq)):
        total += pos_freq[i] * abs(i - median)
    return total


def crab_math_fuel_cost(pos_freq, max_pos):
    # using memoization
    crab_sums = [0]*(max_pos + 1)
    for i in range(1, max_pos + 1):
        crab_sums[i] = crab_sums[i - 1] + i
    # brute force find min_cost using memoized array
    min_cost = 0
    for i in range(max_pos + 1):
        if i > 0:
            temp = 0
            for j in range(max_pos + 1):
                temp += pos_freq[j] * crab_sums[abs(j - i)]
            if temp < min_cost:
                min_cost = temp
            else:
                break
        else:
            for j in range(max_pos + 1):
                min_cost += pos_freq[j] * crab_sums[j]
    return min_cost


def main():
    fname = 'input'
    pos_freq, median, max_pos = get_init_crab_pos(fname)
    #print(pos_freq)
    #print(f'Median: {median}')
    # challenge 1:
    # cost = calc_fuel_cost(pos_freq, median)
    # challenge 2:
    cost = crab_math_fuel_cost(pos_freq, max_pos)
    print(cost)

if __name__ == "__main__":
    main()