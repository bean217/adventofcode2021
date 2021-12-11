POINT_MAP = {')': 3, ']': 57, '}': 1197, '>': 25137}
REVERSE = {'(': ')', '[': ']', '{': '}', '<': '>'} 


def isOpen(char):
    if char in {'(', '[', '{', '<'}:
        return True
    return False


def evaluate_line(line):
    stack = []
    for char in line:
        print(char, end="")
        if isOpen(char):
            stack.append(char)
        else:
            if len(stack) == 0:
                break
            popped = stack.pop()
            if char != REVERSE[popped]:
                return POINT_MAP[char]
    print()
    return 0


def get_syntax_score(fname):
    score = 0 
    with open(fname) as f:
        for line in f:
            line = line.strip()
            score += evaluate_line(line)
    return score


def main():
    fname = 'input'
    syntax_score = get_syntax_score(fname)
    print(syntax_score)

if __name__ == "__main__":
    main()