def main():
    with open('input') as f:
        sums = [0, 0, 0]
        curr_iter = 0
        # read first 3 lines
        i = 0
        for line in f:
            line = int(line.strip())
            sums[curr_iter] = line
            curr_iter += 1
            if curr_iter == 3:
                curr_iter = 0
                break
            continue
        # do the work
        count = 0
        last = sums[0] + sums[1] + sums[2]
        for line in f:
            line = int(line.strip())
            sums = [sums[1], sums[2], line]
            if sums[0] + sums[1] + sums[2] > last:
                count += 1
            last = sums[0] + sums[1] + sums[2]
        print(count)

if __name__ == "__main__":
    main()