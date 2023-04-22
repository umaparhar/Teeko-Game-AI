import random
import math
import copy

class Teeko2Player:
    """ An object representation for an AI game player for the game Teeko2.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']

    def __init__(self):
        """ Initializes a Teeko2Player object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.

        Args:
            state (list of lists): should be the current state of the game as saved in
                this Teeko2Player object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.

                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).

        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """
        pieceCount = 0
        for index1, row in enumerate(state):
                for index2, entry in enumerate(row):
                    if(state[index1][index2] != " "):
                        pieceCount+=1
        if(pieceCount >= 8):
            drop_phase = False
        else:
            drop_phase = True   # TODO: detect drop phase

        if not drop_phase:
            # TODO: choose a piece to move and remove it from the board
            # (You may move this condition anywhere, just be sure to handle it)
            #
            # Until this part is implemented and the move list is updated
            # accordingly, the AI will not follow the rules after the drop phase!
            move = []
            newState = max_value(self, state, 1)[1]
            
            for index1, row in enumerate(state):
                for index2, entry in enumerate(row):
                    if (newState[index1][index2] == " " and state[index1][index2] != " "):
                        removeIndex = (index1, index2)
                    if (newState[index1][index2] != " " and state[index1][index2] == " "):
                        moveIndex = (index1, index2)
            move.append(moveIndex)
            move.append(removeIndex)


        # select an unoccupied space randomly
        # TODO: implement a minimax algorithm to play better
        
        else:
            move = []
            newState = max_value(self, state, 1)[1]
            for index1, row in enumerate(state):
                for index2, entry in enumerate(row):
                    if newState[index1][index2] != state[index1][index2]:
                        moveIndex = (index1, index2)
            move.insert(0, moveIndex)
        return move

    def succ(self, state):
        #find out if in drop phase
        dropCount = 0
        succList = []
        stateCopy = copy.deepcopy(state)
        for index1, row in enumerate(state):
            for index2, entry in enumerate(row):
                if entry == self.my_piece:
                    dropCount+=1
        
        if(dropCount < 4):
            for index1, row in enumerate(stateCopy):
                for index2, entry in enumerate(row):
                    if entry == " ":
                        currList = copy.deepcopy(stateCopy)
                        currList[index1][index2] = self.my_piece
                        succList.append(currList)
        else:
            for index1, row in enumerate(stateCopy):
                for index2, entry in enumerate(row):
                    if entry == self.my_piece:
                        if index1 != 0: #up space
                            if state[index1 - 1][index2] == " ":
                                currList1 = copy.deepcopy(stateCopy)
                                currList1[index1 - 1][index2] = self.my_piece
                                currList1[index1][index2] = " "
                                succList.append(currList1)
                        if index2 != 4: #right space
                            if state[index1][index2 + 1] == " ":
                                currList2 = copy.deepcopy(stateCopy)
                                currList2[index1][index2 + 1] = self.my_piece
                                currList2[index1][index2] = " "
                                succList.append(currList2)
                        if index1 != 4: #down space
                            if state[index1 + 1][index2] == " ":
                                currList3 = copy.deepcopy(stateCopy)
                                currList3[index1 + 1][index2] = self.my_piece
                                currList3[index1][index2] = " "
                                succList.append(currList3)
                        if index2 != 0: #left space
                            if state[index1][index2 - 1] == " ":
                                currList4 = copy.deepcopy(stateCopy)
                                currList4[index1][index2 - 1] = self.my_piece
                                currList4[index1][index2] = " "
                                succList.append(currList4)
                        if (index1 != 4 and index2 != 4): #right up diagonal
                            if state[index1 + 1][index2 + 1] == " ":
                                currList5 = copy.deepcopy(stateCopy)
                                currList5[index1 + 1][index2 + 1] = self.my_piece
                                currList5[index1][index2] = " "
                                succList.append(currList5)
                        if (index1 != 0 and index2 != 4): #left up diagonal
                            if state[index1 - 1][index2 + 1] == " ":
                                currList6 = copy.deepcopy(stateCopy)
                                currList6[index1 - 1][index2 + 1] = self.my_piece
                                currList6[index1][index2] = " "
                                succList.append(currList6)
                        if (index1 != 4 and index2 != 0): #right down diagonal
                            if state[index1 + 1][index2 - 1] == " ":
                                currList7 = copy.deepcopy(stateCopy)
                                currList7[index1 + 1][index2 - 1] = self.my_piece
                                currList7[index1][index2] = " "
                                succList.append(currList7)
                        if (index1 != 0 and index2 != 0): #right down diagonal
                            if state[index1 - 1][index2 - 1] == " ":
                                currList8 = copy.deepcopy(stateCopy)
                                currList8[index1 - 1][index2 - 1] = self.my_piece
                                currList8[index1][index2] = " "
                                succList.append(currList8)
        #tup = [tuple(e) for e in succList]
        #outputList = set(tup) #remove dupes
        return succList


    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                self.print_board()
                print(move)
                raise Exception("You don't have a piece there!")
            if abs(source_row - move[0][0]) > 1 or abs(source_col - move[0][1]) > 1:
                self.print_board()
                print(move)
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row)+": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")

    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this Teeko2Player object, or a generated successor state.

        Returns:
            int: 1 if this Teeko2Player wins, -1 if the opponent wins, 0 if no winner

        TODO: complete checks for diagonal and 3x3 square corners wins
        """

        opponentPiece = self.pieces
        #print(opponentPiece)
        #print(self.my_piece)
        #opponentPiece.remove(self.my_piece)

        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return 1 if row[i]==self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:
                    return 1 if state[i][col]==self.my_piece else -1

        # TODO: check \ diagonal wins

        #case1
        if state[0][0] == self.my_piece:
            if state[1][1] == self.my_piece:
                if state[2][2] == self.my_piece:
                    if state[3][3] == self.my_piece:
                        return 1
        
        if state[0][0] == opponentPiece[0]:
            if state[1][1] == opponentPiece[0]:
                if state[2][2] == opponentPiece[0]:
                    if state[3][3] == opponentPiece[0]:
                        return -1
        #case2
        if state[1][1] == self.my_piece:
            if state[2][2] == self.my_piece:
                if state[3][3] == self.my_piece:
                    if state[4][4] == self.my_piece:
                        return 1

        if state[1][1] == opponentPiece[0]:
            if state[2][2] == opponentPiece[0]:
                if state[3][3] == opponentPiece[0]:
                    if state[4][4] == opponentPiece[0]:
                        return -1
        #case3
        if state[0][1] == self.my_piece:
            if state[1][2] == self.my_piece:
                if state[2][3] == self.my_piece:
                    if state[3][4] == self.my_piece:
                        return 1
        
        if state[0][1] == opponentPiece[0]:
            if state[1][2] == opponentPiece[0]:
                if state[2][3] == opponentPiece[0]:
                    if state[3][4] == opponentPiece[0]:
                        return -1
        #case4
        if state[1][0] == self.my_piece:
            if state[2][1] == self.my_piece:
                if state[3][2] == self.my_piece:
                    if state[4][3] == self.my_piece:
                        return 1

        if state[1][0] == opponentPiece[0]:
            if state[2][1] == opponentPiece[0]:
                if state[3][2] == opponentPiece[0]:
                    if state[4][3] == opponentPiece[0]:
                        return -1
 
        # TODO: check / diagonal wins
        #case1
        if state[0][3] == self.my_piece:
            if state[1][2] == self.my_piece:
                if state[2][1] == self.my_piece:
                    if state[3][0] == self.my_piece:
                        return 1
        
        if state[0][3] == opponentPiece[0]:
            if state[1][2] == opponentPiece[0]:
                if state[2][1] == opponentPiece[0]:
                    if state[3][0] == opponentPiece[0]:
                        return -1
        #case2
        if state[0][4] == self.my_piece:
            if state[1][3] == self.my_piece:
                if state[2][2] == self.my_piece:
                    if state[3][1] == self.my_piece:
                        return 1
        
        if state[0][4] == opponentPiece[0]:
            if state[1][3] == opponentPiece[0]:
                if state[2][2] == opponentPiece[0]:
                    if state[3][1] == opponentPiece[0]:
                        return -1
        #case3
        if state[1][3] == self.my_piece:
            if state[2][2] == self.my_piece:
                if state[3][1] == self.my_piece:
                    if state[4][0] == self.my_piece:
                        return 1

        if state[1][3] == opponentPiece[0]:
            if state[2][2] == opponentPiece[0]:
                if state[3][1] == opponentPiece[0]:
                    if state[4][0] == opponentPiece[0]:
                        return -1
        #case4
        if state[1][4] == self.my_piece:
            if state[2][3] == self.my_piece:
                if state[3][2] == self.my_piece:
                    if state[4][1] == self.my_piece:
                        return 1

        if state[1][4] == opponentPiece[0]:
            if state[2][3] == opponentPiece[0]:
                if state[3][2] == opponentPiece[0]:
                    if state[4][1] == opponentPiece[0]:
                        return -1

        # TODO: check 3x3 square corners wins
        for index1 in range(2):
            for index2 in range(2):
                if state[index1][index2] == opponentPiece[0]:
                    if state[index1 + 2][index2] == opponentPiece[0]:
                        if state[index1][index2 + 2] == opponentPiece[0]:
                            if state[index1 + 2][index2 + 2] == opponentPiece[0]:
                                return -1
                if state[index1][index2] == self.my_piece:
                    if state[index1 + 2][index2] == self.my_piece:
                        if state[index1][index2 + 2] == self.my_piece:
                            if state[index1 + 2][index2 + 2] == self.my_piece:
                                return 1
        #print(self.my_piece)
        #print(self_number_of_pieces_in_row(self,state))
        #print(self.opp)
        #print(opponent_number_of_pieces_in_row(self, state))
        #max_value(self, state, 5)
        #print(self.succ(state))
        #print(state)
        return 0 # no winner yet

def heuristic_game_value(self, state):
    if (self.game_value(state) == 1):
        return 1
    if (self.game_value(state) == -1):
        return -1
    check = self_number_of_pieces_in_row(self, state) - opponent_number_of_pieces_in_row(self, state)
    if check == 0:
        return 0
    if check == 2:
        return 0.75
    if check == -2:
        return -0.75
    if check == 1:
        return 0.5
    if check == -1:
        return -0.5
    return 0


def self_number_of_pieces_in_row(self, state):
    max_count = 0
    for index1, row in enumerate(state):
        for index2, entry in enumerate(row):
            if entry == self.my_piece:
                countDown = 0
                for i in range(4 - index1): #down
                    if state[index1 + i][index2] == self.my_piece:
                        countDown += 1
                    else:
                        break
                if countDown > max_count:
                    max_count = countDown
                countUp = 0
                for j in range(index1 - 1): #up
                    if state[index1 - j][index2] == self.my_piece:
                        countUp += 1
                    else:
                        break
                if countUp > max_count:
                    max_count = countUp
                countRight = 0
                for m in range(4 - index2): #right
                    if state[index1][index2 + m] == self.my_piece:
                        countRight += 1
                    else:
                        break
                if countRight > max_count:
                    max_count = countRight
                countLeft = 0
                for n in range(index2 - 1): #left
                    if state[index1][index2 - n] == self.my_piece:
                        countLeft += 1
                    else:
                        break
                if countLeft > max_count:
                    max_count = countLeft
    if check_diagonal(self, state) > max_count:
        max_count = check_diagonal(self, state)
    
    return max_count

def opponent_number_of_pieces_in_row(self, state):
    max_count = 0
    for index1, row in enumerate(state):
        for index2, entry in enumerate(row):
            if entry == self.opp:
                countDown = 0
                for i in range(4 - index1): #down
                    if state[index1 + i][index2] == self.opp:
                        countDown += 1
                    else:
                        break
                if countDown > max_count:
                    max_count = countDown
                countUp = 0
                for j in range(index1 - 1): #up
                    if state[index1 - j][index2] == self.opp:
                        countUp += 1
                    else:
                        break
                if countUp > max_count:
                    max_count = countUp
                countRight = 0
                for m in range(4 - index2): #right
                    if state[index1][index2 + m] == self.opp:
                        countRight += 1
                    else:
                        break
                if countRight > max_count:
                    max_count = countRight
                countLeft = 0
                for n in range(index2 - 1): #left
                    if state[index1][index2 - n] == self.opp:
                        countLeft += 1
                    else:
                        break
                if countLeft > max_count:
                    max_count = countLeft
    if check_opponent_diagonal(self, state) > max_count:
        max_count = check_opponent_diagonal(self, state)
    
    return max_count


def check_diagonal(self, state):
    diagonalList = []
    
    diagonal1 = [[3,0], [2,1], [1,2], [0,3]]
    diagonal2 = [[4,0], [3,1], [2,2], [1,3]]
    diagonal3 = [[3,1], [2,2], [1,3], [0,4]]
    diagonal4 = [[4,1], [3,2], [2,3], [1,4]]
    diagonal5 = [[1,0], [2,1], [3,2], [4,3]]
    diagonal6 = [[0,0], [1,1], [2,2], [3,3]]
    diagonal7 = [[1,1], [2,2], [3,3], [4,4]]
    diagonal8 = [[0,1], [1,2], [2,3], [3,4]]

    diagonalList.append(diagonal1)
    diagonalList.append(diagonal2)
    diagonalList.append(diagonal3)
    diagonalList.append(diagonal4)
    diagonalList.append(diagonal5)
    diagonalList.append(diagonal6)
    diagonalList.append(diagonal7)
    diagonalList.append(diagonal8)

    count = 0
    pieces = []
    for index1, row in enumerate(state):
        for index2, entry in enumerate(row):
            if entry == self.my_piece:
                pieces.append([index1, index2])
    for diagonal in diagonalList:
        tup1 = [tuple(lst) for lst in diagonal]
        tup2 = [tuple(lst) for lst in pieces]
        
        currCount = len(set(tup1) & set(tup2))
        if (currCount > count and currCount != 1):
            count = currCount
    return count

def check_opponent_diagonal(self, state):
    diagonalList = []
    
    diagonal1 = [[3,0], [2,1], [1,2], [0,3]]
    diagonal2 = [[4,0], [3,1], [2,2], [1,3]]
    diagonal3 = [[3,1], [2,2], [1,3], [0,4]]
    diagonal4 = [[4,1], [3,2], [2,3], [1,4]]
    diagonal5 = [[1,0], [2,1], [3,2], [4,3]]
    diagonal6 = [[0,0], [1,1], [2,2], [3,3]]
    diagonal7 = [[1,1], [2,2], [3,3], [4,4]]
    diagonal8 = [[0,1], [1,2], [2,3], [3,4]]

    diagonalList.append(diagonal1)
    diagonalList.append(diagonal2)
    diagonalList.append(diagonal3)
    diagonalList.append(diagonal4)
    diagonalList.append(diagonal5)
    diagonalList.append(diagonal6)
    diagonalList.append(diagonal7)
    diagonalList.append(diagonal8)
    
    count = 0
    pieces = []
    for index1, row in enumerate(state):
        for index2, entry in enumerate(row):
            if entry == self.opp:
                pieces.append([index1, index2])
    for diagonal in diagonalList:
        tup1 = [tuple(lst) for lst in diagonal]
        tup2 = [tuple(lst) for lst in pieces]
        currCount = len(set(tup1) & set(tup2))
        if (currCount > count and currCount != 1):
            count = currCount
    return count

def max_value(self, state, depth):
    #max_value(self, state, 0)
    if self.game_value(state) == 1:
        return 1
    elif self.game_value(state) == -1:
        return -1
    elif depth == 0:
        return heuristic_game_value(self, state)
    else:
        currMax = -math.inf
        for s in self.succ(state):
            c = copy.deepcopy(currMax)
            
            if type(max_value(self, s, depth - 1)) == tuple:
                if(max_value(self, s, depth - 1)[0] > currMax):
                    currMax = max_value(self, s, depth - 1)[0]
                    bestSucc = s
            else:
                if(max_value(self, s, depth - 1) > currMax):
                    currMax = max_value(self, s, depth - 1)
                    bestSucc = s
    return currMax, bestSucc

def min_value(self, state, depth):
    #max_value(self, state, 0)
    if self.game_value(state) == 1:
        return 1
    elif self.game_value(state) == -1:
        return -1
    elif depth == 0:
        return heuristic_game_value(self, state)
    else:
        currMin = math.inf
        for s in self.succ(state):
            c = copy.deepcopy(currMin)
            if type(min_value(self, s, depth - 1)) == tuple:
                currMin = min(min_value(self, s, depth - 1)[0], currMin)
            else:
                currMin = min(min_value(self, s, depth - 1), currMin)
            if currMin != c:
                worstSucc = s
    return currMin, worstSucc

############################################################################
#
# THE FOLLOWING CODE IS FOR SAMPLE GAMEPLAY ONLY
#
############################################################################
def main():
    print('Hello, this is Samaritan')
    
    ai = Teeko2Player()
    piece_count = 0
    turn = 0
    
    # drop phase
    while piece_count < 8 and ai.game_value(ai.board) == 0:
        
        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved at "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                player_move = input("Move (e.g. B3): ")
                while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                    player_move = input("Move (e.g. B3): ")
                try:
                    ai.opponent_move([(int(player_move[1]), ord(player_move[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        piece_count += 1
        turn += 1
        turn %= 2

    # move phase - can't have a winner until all 8 pieces are on the board
    while ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved from "+chr(move[1][1]+ord("A"))+str(move[1][0]))
            print("  to "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            
            while not move_made:
                move_from = input("Move from (e.g. B3): ")
                while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                    move_from = input("Move from (e.g. B3): ")
                move_to = input("Move to (e.g. B3): ")
                while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                    move_to = input("Move to (e.g. B3): ")
                try:
                    ai.opponent_move([(int(move_to[1]), ord(move_to[0])-ord("A")),
                                    (int(move_from[1]), ord(move_from[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        turn += 1
        turn %= 2

    ai.print_board()
    if ai.game_value(ai.board) == 1:
        
        print("AI wins! Game over.")
    else:
        #ai.succ(ai.board)
        print("You win! Game over.")


if __name__ == "__main__":
    main()
