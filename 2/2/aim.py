def main():
    with open('input') as f:
        aim = 0
        horiz = 0
        vert = 0
        for line in f:
            line = line.strip().split()
            line[1] = int(line[1])
            if (line[0] == 'up'):
                aim -= line[1]
            elif (line[0] == 'down'):
                aim += line[1]
            else:
                # line[0] == 'forward'
                horiz += line[1]
                vert += aim * line[1]
        print(f'horiz: {horiz}')
        print(f'vert: {vert}')
        print(f'h*v: {horiz * vert}')

if __name__ == "__main__":
    main()