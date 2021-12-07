class Bingo:
    def __init__(self):
        self.winner = []
        self.num_seq = []
        self.boards = []

    def set_num_seq(self, num_seq):
        self.num_seq = num_seq

    def add_board(self, board):
        self.boards += [board]

    def run_game(self):
        winner = None
        for val in self.num_seq:
            for i in range(len(self.boards)):
                self.boards[i].check_for_val(val)
                if self.boards[i].isWon:
                    winner = (i, self.boards[i].calc_score(val))
                    break
            if winner:
                break
        self.winner += [winner]
    
    def run_game_last_winner(self):
        winner = None
        for val in self.num_seq:
            for i in range(len(self.boards)):
                if self.boards[i].isWon:
                    continue
                self.boards[i].check_for_val(val)
                if self.boards[i].isWon:
                    winner = (i, self.boards[i].calc_score(val))
                    self.winner += [winner]
                

class Board:
    def __init__(self):
        self.board = [[0]*5 for _ in range(5)]
        self.calledRows = [0]*5
        self.calledCols = [0]*5
        self.avail_nums = set()
        self.isWon = False

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
    
    def check_for_val(self, val):
        # find value in board
        if val in self.avail_nums:
            self.avail_nums.remove(val)
            val_pos = None
            for j in range(5): # j ~= row
                for i in range(5): # i ~= col
                    if self.board[j][i] == val:
                        val_pos = (j, i)
            if val_pos:
                self.calledRows[val_pos[0]] += 1
                self.calledCols[val_pos[1]] += 1
            for q in self.calledRows:
                if q == 5:
                    self.isWon = True
            for q in self.calledCols:
                if q == 5:
                    self.isWon = True
    
    def calc_score(self, last_called_val):
        sum = 0
        for val in self.avail_nums:
            sum += val
        return sum * last_called_val

def main():
    with open('input') as f:
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
            board.board[row_num] = [int(i) for i in line.split()]
            for val in board.board[row_num]:
                board.avail_nums.add(val)
            row_num += 1
            if row_num == 5:
                bingo.add_board(board)
    for b in bingo.boards:
        print(b)
    # bingo.run_game()
    bingo.run_game_last_winner()
    print(bingo.winner[-1])    

if __name__ == "__main__":
    main()