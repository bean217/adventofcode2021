class Bingo:
    def __init__(self):
        self.num_seq = []
        self.boards = []

    def set_num_seq(self, num_seq):
        self.num_seq = num_seq

    def add_board(self, board):
        self.boards += [board]

class Board:
    def __init__(self):
        self.board = [[0]*5]*5

    def __str__(self):
        result = ""
        for j in range(5):
            for i in range(5):
                if (self.board[j][i] < 10):
                    result += " "
                result += f'{str(self.board[j][i])}'
                if (i < 4):
                    result += " "
            result += "\n"
        return result

def main():
    with open('test') as f:
        # first line is the game number sequence
        bingo = Bingo()
        for line in f:
            bingo.set_num_seq([int(i) for i in line.strip().split(',')])
            break
        print(bingo.num_seq)
        # Create boards
        board = Board()
        row_num = 0
        for line in f:
            line = line.strip()
            if line == "":
                # new board
                board = Board()
                row_num = 0
                continue
            line = [int(i) for i in line.split()]
            board.board[row_num] = line
            row_num += 1
            if row_num == 5:
                bingo.add_board(board)
        for b in bingo.boards:
            print(b)


if __name__ == "__main__":
    main()