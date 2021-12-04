def main():
    with open('input') as f:
        count = 0
        last = ""
        for line in f:
            line = int(line.strip())
            if last == "":
                last = line
                continue
            if line > last:
                count += 1
            last = line
    print(count)

if __name__ == "__main__":
    main()