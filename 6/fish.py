def get_init_fish_states(filename):
    init = [0]*9
    with open(filename) as f:
        for line in f:
            line = [int(val) for val in line.strip().split(',')]
            for val in line:
                init[val] += 1
    return init

def cycle_fish(fish_states, num_days):
    #print(fish_states)
    count = 0
    cust_range = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    for _ in range(num_days):
        holder = fish_states[0]
        for i in range(1, 9):
            fish_states[i-1] = fish_states[i]
        fish_states[6] += holder
        fish_states[8] = holder
        #print(fish_states)
    for val in fish_states:
        count += val
    return count

def main():
    fname = 'input'
    num_days = 256
    fish_states = get_init_fish_states(fname)
    print(cycle_fish(fish_states, num_days))


if __name__ == "__main__":
    main()