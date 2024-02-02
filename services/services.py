class ChessboardService:
    def __init__(self):
        # Mapping of column letters to their corresponding numbers
        self.row_mapping = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        
        # Length of the chessboard
        self.length = 8
        
        # Directions for the Bishop to move diagonally
        self.bishop_directions = [
            {"row": 1, "col": 1},
            {"row": 1, "col": -1},
            {"row": -1, "col": 1},
            {"row": -1, "col": -1},
        ]

        # Directions for the Rook to move horizontally or vertically
        self.rook_directions = [
            {"row": 1, "col": 0},
            {"row": -1, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": -1},
        ]

        # Directions for the Knight to move in an L-shaped pattern
        self.knight_directions = [
            {"row": 2, "col": 1},
            {"row": 2, "col": -1},
            {"row": -2, "col": 1},
            {"row": -2, "col": -1},
            {"row": 1, "col": 2},
            {"row": 1, "col": -2},
            {"row": -1, "col": 2},
            {"row": -1, "col": -2},
        ]

    def get_current_positions_dimension(self, position):
        try:
            # Calculate the row dimension
            row = self.length - int(position[1]) + 1

            # Retrieve the column dimension using the row_mapping
            column = self.row_mapping[position[0]]

            return {"row": row, "column": column}
        except Exception as e:
            raise e

    def get_current_positions(self, dimension):
        try:
            # Calculate the row position
            row = self.length - dimension["row"] + 1

            # Find the column position
            column = [key for key, value in self.row_mapping.items() if value == dimension["col"]][0]

            return f"{column}{row}"
        except Exception as e:
            raise e

    def get_all_knight_moves(self, current_position):
        try:
            dimentions =  self.get_current_positions_dimension(current_position)
            row_dimension = dimentions['row']
            column_dimension = dimentions['column']

            directions = self.knight_directions # Define possible directions the Knight can move

            moves = [current_position]

            for direction in directions:
                # Calculate new row and column positions based on the direction
                new_row = row_dimension + direction["row"]
                new_col = column_dimension + direction["col"]

                if 1 <= new_row <= 8 and 1 <= new_col <= 8:
                    move =  self.get_current_positions({"row": new_row, "col": new_col})
                    moves.append(move)
                else:
                    break # Stop iterating in this direction if out of bounds

            return moves
        except Exception as e:
            raise e

    def get_all_moves(self, current_position, piece):
        try:
            dimentions =  self.get_current_positions_dimension(current_position)
            row_dimension = dimentions['row']
            column_dimension = dimentions['column']

            if piece == "Bishop":
                directions = self.bishop_directions # Define possible directions the Bishop can move
            elif piece == "Rook":
                directions = self.rook_directions
            elif piece == "Queen":
                directions = [*self.rook_directions, *self.bishop_directions] # Queen can move both directions of Rook and Bishop

            moves = [current_position] # Initialize an list with the current position as the starting move

            for direction in directions:
                for i in range(1, 8):
                    new_row = row_dimension + i * direction["row"]
                    new_col = column_dimension + i * direction["col"]

                    if 1 <= new_row <= 8 and 1 <= new_col <= 8: # // Check if the new position is within the chessboard boundaries
                        move =  self.get_current_positions({"row": new_row, "col": new_col})
                        moves.append(move)
                    else:
                        break # Stop iterating in this direction if out of bounds

            return moves
        except Exception as e:
            raise e

    def get_all_piece_moves(self, params):
        try:
            all_bishop_moves =  self.get_all_moves(params["postions"]["Bishop"], "Bishop")
            all_rook_moves =  self.get_all_moves(params["postions"]["Rook"], "Rook")
            all_queen_moves =  self.get_all_moves(params["postions"]["Queen"], "Queen")
            all_knight_moves =  self.get_all_knight_moves(params["postions"]["Knight"])

            return {
                "all_bishop_moves": all_bishop_moves,
                "all_rook_moves": all_rook_moves,
                "all_queen_moves": all_queen_moves,
                "all_knight_moves": all_knight_moves,
            }
        except Exception as e:
            raise e

    def get_knight_valid_moves(self, params):
        try:
            # Get all possible moves for each piece on the chessboard
            all_piece_moves =  self.get_all_piece_moves(params)
            all_bishop_moves = all_piece_moves['all_bishop_moves']
            all_rook_moves = all_piece_moves['all_rook_moves']
            all_queen_moves = all_piece_moves['all_queen_moves']
            all_knight_moves = all_piece_moves['all_knight_moves']

            # Combine moves of other pieces into a single array
            all_others_moves = [*all_bishop_moves, *all_rook_moves, *all_queen_moves, params['postions']['Knight']]

            # Filter out Knight moves that overlap with moves of other pieces
            valid_moves = [move for move in all_knight_moves if move not in all_others_moves]

            return {"valid_moves": valid_moves}
        except Exception as e:
            raise e

    def get_queen_valid_moves(self, params):
        try:
            all_piece_moves =  self.get_all_piece_moves(params)
            all_bishop_moves = all_piece_moves['all_bishop_moves']
            all_rook_moves = all_piece_moves['all_rook_moves']
            all_queen_moves = all_piece_moves['all_queen_moves']
            all_knight_moves = all_piece_moves['all_knight_moves']


            all_others_moves = [*all_bishop_moves, *all_rook_moves, *all_knight_moves, params['postions']['Queen']]

            # Filter out Queen moves that overlap with moves of other pieces
            valid_moves = [move for move in all_queen_moves if move not in all_others_moves]

            return {"valid_moves": valid_moves}
        except Exception as e:
            raise e

    def get_rook_valid_moves(self, params):
        try:
            all_piece_moves =  self.get_all_piece_moves(params)
            all_bishop_moves = all_piece_moves['all_bishop_moves']
            all_rook_moves = all_piece_moves['all_rook_moves']
            all_queen_moves = all_piece_moves['all_queen_moves']
            all_knight_moves = all_piece_moves['all_knight_moves']

            all_others_moves = [*all_bishop_moves, *all_queen_moves, *all_knight_moves, params['postions']['Rook']]
            # Filter out Rook moves that overlap with moves of other pieces
            valid_moves = [move for move in all_rook_moves if move not in all_others_moves]

            return {"valid_moves": valid_moves}
        except Exception as e:
            raise e

    def get_bishop_valid_moves(self, params):
        try:
            all_piece_moves =  self.get_all_piece_moves(params)
            all_bishop_moves = all_piece_moves['all_bishop_moves']
            all_rook_moves = all_piece_moves['all_rook_moves']
            all_queen_moves = all_piece_moves['all_queen_moves']
            all_knight_moves = all_piece_moves['all_knight_moves']

            all_others_moves = [*all_rook_moves, *all_queen_moves, *all_knight_moves, params['postions']['Bishop']]
            # Filter out Bishop moves that overlap with moves of other pieces
            valid_moves = [move for move in all_bishop_moves if move not in all_others_moves]

            return {"valid_moves": valid_moves}
        except Exception as e:
            raise e
