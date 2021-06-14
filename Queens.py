import math
import sys

#put queen in square DONE
def placeQueen(b, i, j):
    b[i][j] = 1
    b[i][0] = j

    #initializing everything from the column down DONE
    for x in range(i+1, len(b)): 
        b[x][j]-=1

    #diagonals DONE
    for k in range(i+1, len(b)):
        for l in range(1,len(b)):
            if abs(k-i) == abs(l-j):
                b[k][l] -= 1

#take queen out of square DONE
def removeQueen(b, i, j):
    b[i][j] = 0
    b[i][0] = 0

    #initializing everything from the column down DONE 
    for x in range(i+1, len(b)): 
        b[x][j]+=1

    #diagonals DONE 
    for k in range(i+1, len(b)):
        for l in range(1,len(b)):
            if abs(k-i) == abs(l-j):
                b[k][l] += 1

#print the column in which the queen is placed within that row DONE
def printBoard(b):
    solution = [b[i][0] for i in range(1, len(b))]
    print(tuple(solution))
        

#find number of solutions if no -v else print solutions DONE
def findSolutions(B, i, mode):
    accsum = 0
    if i > len(B)-1:
        if mode == "-v":
            printBoard(B)
        return 1
    else:
        for j in range(1,len(B)):
            if B[i][j] == 0:
                placeQueen(B, i, j)
                accsum += int(findSolutions(B, i+1, mode))
                removeQueen(B, i, j)
    return accsum

#usage error message DONE
def usage():
    print("Usage: python3 Queens.py [-v] number" , file=sys.stderr)
    print("Option: -v verbose output, print all solutions", file=sys.stderr)
    exit()

#main function DONE
def main():

    if len(sys.argv) == 1:
        usage()
    elif sys.argv[1] == "-v" and len(sys.argv) == 2:
        usage()        
    elif sys.argv[1] == "-v":
        verbose = sys.argv[1]
        try:
            n = int(sys.argv[2]) + 1
        except ValueError:
            usage()
    else:
        try:
            n = int(sys.argv[1]) + 1
            verbose = ''
        except ValueError:
            usage()

    board = []
    r = n * [0]

    for x in range(n):
        board.append(r[:])

    numSol = findSolutions(board, 1, verbose)
    print("%d-Queens has %s solutions" % (n-1, numSol))

if __name__ == "__main__":
    main()
    