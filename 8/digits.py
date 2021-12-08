# 0: 6
# 1: 2
# 2: 5
# 3: 5
# 4: 4
# 5: 5
# 6: 6
# 7: 3
# 8: 7
# 9: 6

# 2: 1
# 3: 7
# 4: 4
# 5: 2, 3, 5
# 6: 0, 6, 9
# 7: 8

# part 1 code
def count_easy_digits(fname):
    count = 0
    with open(fname) as f:
        for line in f:
            line = line.strip()
            line = line.split('|')[1].split()
            #print(line)
            for seq in line:
                if len(seq) in (2, 3, 4, 7):
                    count += 1
    return count


# part 2 code
def count_all_digits(fname):
    return 0

def main():
    fname = 'test'
    num_digits = count_all_digits(fname)
    print(f'Number of Digits: {num_digits}')

if __name__ == "__main__":
    main()