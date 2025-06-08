import re

def main():
    again = True
    while(again):
        board = [["e" for x in range(3)] for y in range (3)]


        boardPrinter(board)

        times: int = 0
        x: bool = True
        while(times < 9):
            inm = input("input your move: ")
            if(re.match('([1-3][1-3])', inm) and board[int(inm[0])-1][int(inm[1])-1] == "e"):
                if(x):
                    board[int(inm[0])-1][int(inm[1])-1] = "x"
                else:
                    board[int(inm[0])-1][int(inm[1])-1] = "o"

                boardPrinter(board)
                if gameOver(board):
                    if (x):
                        print("X is the winner")
                    else:
                        print("O is the winner")

                    break

                x = not x
                times += 1

            else:
                print("invalid input")

        if(times >= 9):
            print("Tie")

        if(input("go again? [y/n]\n") == "n" or input("go again? [y/n]\n") == "N"):
            again = False

def boardPrinter(board):
    for i in board:
        print(i)

def inRow(board):
    for i in range(3):
        if((board [i][0] == "o" or board[i][0] == "x")
           and (board[i][0] == board[i][1] == board[i][2])):
            return True
    return False

def inCol(board):
    for i in range(3):
        if ((board [0][i] == "o" or board[0][i] == "x")
            and ( board[0][i] == board[1][i] == board[2][i])):
            return True
    return False

def inDia(board):
    if((board [1][1] == "o" or board[1][1] == "x")
       and ((board[0][0] == board[1][1] == board[2][2])
       or (board[2][2] == board[1][1] == board[0][0]))):
        return True
    else:
        return False

def gameOver(board):
    if(inDia(board) or inRow(board) or inCol(board)):
        return True
    else:
        return False
if __name__ == "__main__":
    main()
