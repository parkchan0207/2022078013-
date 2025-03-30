# 2022078013 박찬엽 틱택토
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def player_move(board):
    while True:
        try:
            row, col = map(int, input("행과 열을 입력하세요 (0-2) 예: 1 1: ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("이미 차있는 자리입니다. 다시 선택하세요.")
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 0에서 2 사이의 숫자로 입력하세요.")

def computer_move(board):
    row, col = random.choice(get_empty_cells(board))
    board[row][col] = "O"
    print(f"컴퓨터가 ({row}, {col}) 위치에 둡니다.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("틱택토 게임 시작!")
    print_board(board)
    
    for turn in range(9):
        if turn % 2 == 0:
            player_move(board)
        else:
            computer_move(board)
        
        print_board(board)
        
        if check_winner(board, "X"):
            print("축하합니다! 당신이 이겼습니다!")
            return
        elif check_winner(board, "O"):
            print("컴퓨터가 이겼습니다!")
            return
    
    print("무승부입니다!")

if __name__ == "__main__":
    tic_tac_toe()