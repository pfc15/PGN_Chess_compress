import chess
import chess.pgn
from chessboard import display
from time import sleep

with open("teste.pgn", 'r') as fp:
    jogo = chess.pgn.read_game(fp)
    game_board = display.start()
    board = jogo.board()
    display.update(board.fen(), game_board)


while True:
    for move in jogo.mainline_moves():
        board.push(move)
        display.update(board.fen(), game_board)
        sleep(1)
        display.check_for_quit()