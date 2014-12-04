class Game:

    WIN_LINES = ([])

    def __init__(self):
        self._board = 3 * [3 * [0]]

    def make_turn(self, player_symbol, x, y):
        self._board[x][y] = player_symbol

    def check_for_end_game(self):
        
