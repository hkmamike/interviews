#!/usr/bin/env python3

import os
import time
os.system('clear')

class Game():

    def __init__(self):
        self.cells = [" "] * 10
        self.turn = "O"
        self.next = {"O":"X", "X":"O"}

    def display_header(self):
        print("----------------------")
        print("Welcome to Tic Tac Toe")
        print("----------------------")

    def display_board(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]) )
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]) )
        print("-----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]) )

    def reload_screen(self):
        os.system('clear')
        self.display_header()
        self.display_board()

    def update_cell(self, cellId, player):
        self.cells[cellId] = player
        self.turn = self.next[player]
        print(self.turn)

    def checkMove(self, cellID):
        if self.cells[cellID] == " ":
            return True
        else:
            return False

    def checkCondition(self, cells):
        if cells[1] == cells[2] == cells[3]:
            if cells[1] == "X":
                return 

game = Game()

while True:
    game.reload_screen()

    winCondition = game.checkCondition()
    if winCondition == 1:
        print('Player X won!')
    elif winCondition == 2:
        print('Player O won!')
    elif winCondition == 3:
        print("It's a tie!")

    if game.turn == "X":
        x_move = int(raw_input("\nX's turn. Please choose cell 1-9 > "))
        if game.checkMove(x_move):
            game.update_cell(x_move, "X")
        else:
            print("invalid move detected. It is still X's turn ")
            time.sleep(1)
            continue
    else:
        o_move = int(raw_input("\nO's turn. Please choose cell 1-9 > "))
        if game.checkMove(o_move):
            game.update_cell(o_move, "O")
        else:
            print("invalid move detected. It is still O's turn ")
            time.sleep(1)
            continue