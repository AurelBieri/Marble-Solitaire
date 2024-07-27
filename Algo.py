import random

def StartGame():
    Population = Create_Population(40)
    for pop in Population:
        Fitness(pop)
    Crossover(Population)

##Algorithms
##=================================================================

def Create_Population(CountPop):
    Population = []
    i = 0
    while(CountPop > i):
        Population.append(PlayGame())
        i = i + 1
    return Population

def Fitness(board):
    Points = 0
    i = 0
    for row in board:
        if i >= 7:
            break
        for p in row:
            if p != -1:
                Points  += p
        i += 1
    board[8] = Points
    return board

def Crossover(Population):
    NewPopulation = []
    BestFitness = []
    ForCorssing = []
    ForMutation = []
    MaxFit = 1000
    WorstFit = 0

    ##Search the Board with highest fitness
    for pop in Population:
        if pop[8] < MaxFit:
            MaxFit = pop[8]
            M = pop
    NewPopulation.append[M]
    ForCorssing.append[M]

    ##Sort out the Boards with lowest finess
    for pop in Population:
        if pop[8] > WorstFit:
            WorstFit = pop[8]
    for pop in Population:
        if pop[8] > WorstFit:
            ForCorssing.append[pop]
    
    ##Corss the diffrent boards
    for pop in ForCorssing:
        NewBoard = []
        OtherBoard = ForCrossing[random.randint(0, ForCorssing.count)]
        i = pop[7].count / 2
        for n in i:
            NewBoard.append[pop[n]]
        i = OtherBoard[7].count / 2
        for n in i:
            NewBoard.append[OtherBoard[i + n]]
        NewPopulation.append[NewBoard]
    
    ##Mutation
    return NewPopulation




## Game
##==================================================================
def PlayGame():
    board = [
    [-1, -1, 1, 1, 1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1],
    [ 1,  1, 1, 1, 1,  1,  1],
    [ 1,  1, 1, 0, 1,  1,  1],
    [ 1,  1, 1, 1, 1,  1,  1],
    [-1, -1, 1, 1, 1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1]
    ]
    MovesUsed = []
    counts = 0
    while(counts < 32):
        valdimoves = FindValidMoves(board)
        move = []
        if(len(valdimoves) == 0):
            break
        else:
            move = valdimoves[random.randrange(len(valdimoves))]
            MovesUsed.append(move)
            board[move[0][0]][move[0][1]] = 1
            board[move[1][0]][move[1][1]] = 0
            board[move[2][0]][move[2][1]] = 0
        counts = counts + 1
    board.append(MovesUsed)
    board.append([])
    return board


def FindValidMoves(board):
    ValideMoves = []
    HBoard = []
    for RowId, Vrows in enumerate(board):
        for index, pos in enumerate(Vrows):
            if pos == 0:
                if (index >= 2):
                    if (Vrows[index - 2] == 1 and Vrows[index - 1] == 1):
                        ValideMoves.append([[RowId, index], [RowId, index - 2], [RowId, index - 1]])
                if(index < len(Vrows) - 2):
                    if (Vrows[index + 2] == 1 and Vrows[index + 1] == 1):
                        ValideMoves.append([[RowId, index], [RowId, index + 2], [RowId, index + 1]])
    Hrows = []
    i = 0
    while i < 7:
        p = 0
        Hrows = []
        while p < 7:
            rownum = board[p]
            Hrows.append(rownum[i])
            p = p + 1
        HBoard.append(Hrows)
        i = i +1

    for RowId, HRow in enumerate(HBoard):
        for index, pos in enumerate(HRow):
            if pos == 0:
                if (index >= 2):
                    if(HRow[index - 2] == 1 and HRow[index - 1] == 1):
                        ValideMoves.append([[index, RowId], [index - 2, RowId], [index - 1 ,RowId]])
                if( index < len(Vrows) - 2):
                    if(HRow[index + 2] == 1 and HRow[index + 1 ] == 1):
                        ValideMoves.append([[index, RowId], [index + 2, RowId], [index + 1, RowId]])
    return ValideMoves

StartGame()