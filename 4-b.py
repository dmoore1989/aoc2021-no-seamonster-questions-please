f = open("4in.txt", "r")
output = f.readlines()

bingo_pastabilities = [
    [(0,0), (0,1), (0,2), (0,3), (0,4)],
    [(1,0), (1,1), (1,2), (1,3), (1,4)],
    [(2,0), (2,1), (2,2), (2,3), (2,4)],
    [(3,0), (3,1), (3,2), (3,3), (3,4)],
    [(4,0), (4,1), (4,2), (4,3), (4,4)],
    [(0,0), (1,0), (2,0), (3,0), (4,0)],
    [(0,1), (1,1), (2,1), (3,1), (4,1)],
    [(0,2), (1,2), (2,2), (3,2), (4,2)],
    [(0,3), (1,3), (2,3), (3,3), (4,3)],
    [(0,4), (1,4), (2,4), (3,4), (4,4)]
]

def check_numbers(boards, numbers):
    for number in numbers:
        for x, board in enumerate(boards):
            for y, line in enumerate(board):
                for z, space in enumerate(line):
                    if space == int(number):
                        boards[x][y][z] = 'x'
        deleted_boards = []
        for idx, board in enumerate(boards):
            if thats_a_bingo(board):
                if len(boards) == 1:
                    print(calc_bingo_score(board, number))
                    return
                else:
                    del boards[idx]

def thats_a_bingo(board):
    for bingo_pastability in bingo_pastabilities:
        if thats_a_bingo_row(board, bingo_pastability):
            return True
    return False
    
def thats_a_bingo_row(board, bingo_pastability):
    for item in bingo_pastability:
        if board[item[0]][item[1]] != 'x':
            return False
    return True

def calc_bingo_score(board, number):
    print(board, number)
    sum = 0
    for line in board:
        for num in line:
            if num != 'x':
                sum += num
    return int(number) * sum

numbers = output[0].split(',')
boards = []
board = []
for num in range(2, len(output)):
    if output[num] != '\n':
        line = []
        for char in range(0, 14, 3):
            line.append(int(output[num][char : char+2]))
        board.append(line)
    else:
        boards.append(board)
        board = []
boards.append(board)
# print(boards)
check_numbers(boards, numbers)