def nextMove(posr, posc, board):
    for i in range(5):
        if 'd' in board[i]:
            a = board[i].index('d')
            b = i
            break
            
    print("LEFT" if a < posc else "RIGHT" if a > posc else "UP" if b < posr else "DOWN" if b > posr else "CLEAN")
            
    
  

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
