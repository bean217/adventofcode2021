POINT_MAP = {')': 3, ']': 57, '}': 1197, '>': 25137}
C_POINT_MAP = {')': 1, ']': 2, '}': 3, '>': 4}
REVERSE = {'(': ')', '[': ']', '{': '}', '<': '>'} 


def isOpen(char):
    if char in {'(', '[', '{', '<'}:
        return True
    return False


def evaluate_line(line):
    stack = []
    for char in line:
        if isOpen(char):
            stack.append(char)
        else:
            if len(stack) == 0:
                # 0 indicates the line was finished
                return (0, '')
            popped = stack.pop()
            if char != REVERSE[popped]:
                # > 0 indicates an error
                return (POINT_MAP[char], '')
    remainder = ''
    c_score = 0
    while len(stack) > 0:
        pop = stack.pop()
        remainder += REVERSE[pop]
        c_score *= 5
        c_score += C_POINT_MAP[REVERSE[pop]]
    #print(line)
    print(f'\tc_score: {c_score}')
    print(f'\tremainder: {remainder}')
    return (c_score, remainder)


def get_syntax_score(fname):
    err_score = 0 
    cmplt_score_arr = []
    with open(fname) as f:
        for line in f:
            line = line.strip()
            l_score, remainder = evaluate_line(line)
            if remainder == '':
                err_score += l_score
            else:
                cmplt_score_arr += [l_score] 
    cmplt_score_arr.sort()
    return err_score, cmplt_score_arr[len(cmplt_score_arr) // 2]


def main():
    fname = 'input'
    err_score, cmplt_score = get_syntax_score(fname)
    print(f'Syntax Error Score: {err_score}')
    print(f'Completion String Score: {cmplt_score}')

if __name__ == "__main__":
    main()