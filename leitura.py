import chess.pgn

pgn = open("./minhas_partidas.pgn")



first_game = chess.pgn.read_game(pgn)

print(first_game.headers)
