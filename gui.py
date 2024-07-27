import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pathlib
import chess
from leitura import ler_arquivo
from compress import *
import chess.pgn
import chess.svg
from chessboard import display
from time import sleep


# create the root window
root = tk.Tk()
root.title('zip de pgn')


def select_file():
    global path_var, acao_var
    if acao_var.get() == "compress" or acao_var.get() == "vizualização":
        filetypes = (
            ('pgn files', '*.pgn'),
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
    else:
        filetypes = (
            ('pgnin files', '*.pgnin'),
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=pathlib.Path().resolve(),
        filetypes=filetypes)
    path_var.set(filename)

def agir():
    global acao_var, path_var
    if acao_var.get() == "compress":
        if path_var.get()[-4:] == ".pgn":
            print("ta indo")
            compress(path=path_var.get())
            print("foi")
        else:
            print("tipo errado de arquivo! apenas arquivos .pgn")
    elif acao_var.get() == "decompress":
        if path_var.get()[-6:] == ".pgnin":
            print("ta indo")
            ler_arquivo(path_var.get())
            print("foi")
        else:
            print("tipo errado de arquivo!")
    elif acao_var.get() == "vizualização":
        print('oi')
        if path_var.get()[-4:] == ".pgn":
            lista_jogos = []
            with open(path_var.get(), 'r') as fp:
                jogo = chess.pgn.read_game(fp)
                print("ola")
                while jogo != None:
                    lista_jogos.append(jogo)
                    jogo = chess.pgn.read_game(fp)
                
            ver_jogo(lista_jogos[0])
    print(acao_var.get())

def ver_jogo(jogo):
    game_board = display.start()
    board = jogo.board()
    display.update(board.fen(), game_board)

    for move in jogo.mainline_moves():
        print(move)
        board.push(move)
        display.update(board.fen(), game_board)
        sleep(0.5)
        display.check_for_quit()
    
    print(jogo.headers["Termination"])
    display.terminate()


ultimo = 0
label_acao = tk.Label(text="ação: ")
label_acao.grid(row=1, column=1)
ultimo+=1
acoes = ["compress", "decompress", "vizualização"]
acao_var = tk.StringVar()
acao_var.set("compress")
acao = tk.OptionMenu(root, acao_var, *acoes)
acao.grid(row=1, column=2)
ultimo+=1
path_var = tk.StringVar()
path = tk.Entry(root, textvariable=path_var, width=60)
path.grid(row=2, column=2)
label_path = tk.Label(text="caminho arquivo: ")
label_path.grid(row=2, column=1)


# open button
open_button = ttk.Button(
    root,
    text='file_explorer',
    command=select_file
)

open_button.grid(row=2, column=3)
ultimo+=1
botao_go = ttk.Button(
    root,
    text="pronto!",
    command=agir,
)
botao_go.grid(row=3, column=2, padx=20, pady=20)


ultimo+=1
root.columnconfigure(0, weight=1)  # column on left
root.columnconfigure(ultimo, weight=1)  # column on right
root.rowconfigure(0, weight=1)     # row above
root.rowconfigure(ultimo, weight=1)     # row below

root.mainloop()
