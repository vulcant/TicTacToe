import random


class TicTacToe:
    def __init__(self):
        self._player = {'marker': ''}
        self._computer = {'marker': '', 'play_style': 'random'}
        self._board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                       'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                       'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}
        self._VALID_MARKERS = ['X', 'O']  # only these markers are allowed
        self._valid_moves = list(self._board.keys())  # all moves are valid at the start
        self._next_move = random.choice(['player', 'computer'])
        self._turn_number = 1  # restricted to be between 1 and 9

    @property
    def winner(self) -> str:
        """
        This property checks who the winner of the game is.
        :return: only returns one of the following strings {'undecided', 'draw', 'computer', 'player'}
        """
        if self._turn_number < 5:
            # game cannot possibly be won until the first player has gone at least 3 times. This happens by turn 5
            # until then, don't bother checking win conditions
            return 'undecided'
        # TODO: create the win logic to check if someone has won, or the game is a draw
        return 'undecided'

    def __str__(self):
        """Over ride the string magic method to print the game board"""
        print('{0}|{1}|{2}'.format(self._board['top-L'], self._board['top-M'], self._board['top-R']))
        print('-+-+-')
        print('{0}|{1}|{2}'.format(self._board['mid-L'], self._board['mid-M'], self._board['mid-R']))
        print('-+-+-')
        print('{0}|{1}|{2}'.format(self._board['bot-L'], self._board['bot-M'], self._board['bot-R']))

