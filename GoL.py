import curses
import time
import random
import copy

class termController:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()

    def reportState(self, board):
        for i in range(len(board)):
            self.stdscr.addstr(i, 0, board[i])

        self.stdscr.refresh()

    def __del__(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()

class gameOfLife():
    def __init__(self, row, columns, saveFile = None):
        self.term = termController()
        self.board = []
        self.same = 0
        
        if saveFile == None:
            for i in range(row):
                toAppend = ""
                for j in range(columns):
                    toAppend += "#" if random.randint(0,1) == 1 else " "
                self.board.append(toAppend)
        else:
            f = open(saveFile, 'r')
            self.board = f.readlines()
            f.close()
            print(len(self.board[0]))
            if len(self.board) != row or len(self.board[0]) != columns:
                print("Invalid Configuration File Provided")
                exit(-1)
            
        self.term.reportState(self.board)
        time.sleep(1)

    def runGame(self):
        done = False
        while (not done):
            done = True
            for i in self.board:
                if i.strip() != "":
                    done  = False
            nextGen = gameOfLife.evolve(self.board)
            if(self.board == nextGen):
                self.same += 1
            self.board = nextGen

            self.term.reportState(self.board)
            time.sleep(1)
            if (self.same >= 10):
                done = True
           
    @staticmethod
    def evolve(board):
        retBoard = copy.deepcopy(board)
        for i in range(len(board)):
            curLine = list(board[i])
            for j in range(len(curLine)):
                nextGen = gameOfLife.evaluatePop(board,i,j)
                curLine[j] = nextGen

            retBoard[i] = "".join(curLine)
        return retBoard

    @staticmethod
    def evaluatePop(board, i, j):
        neighbour = 0
        ret = '#'

        if ((i - 1) >= 0):
            neighbour += 1 if board[i-1][j] == '#' else 0

        if i + 1 < len(board):
            neighbour += 1 if board[i+1][j] == '#' else 0

        if (j - 1 >= 0):
            neighbour += 1 if board[i][j-1] == '#' else 0

        if j + 1 < len(board[0]):
            neighbour += 1 if board[i][j+1] == '#' else 0
        
        if board[i][j] == '#':
            if ((neighbour < 2) or (neighbour > 3)):
                ret = ' '
        else:
            if neighbour != 3:
                ret = ' '
        return ret  
                  
    def __del__(self):
        del self.term
        pass

if __name__ == "__main__":
    G = gameOfLife(20, 40, "test.txt")

    G.runGame()

    del G


