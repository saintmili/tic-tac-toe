from models import Player, Game
        


def start_game_commandline(game):
    elements = game.elements
    players = game.players
    if len(players) != game.player_count:
        return print('not enough players')
    flag = 0
    for turn in range(game.demension * game.demension):
        print(f'{game.players[0].get_color()}: x     {game.players[1].get_color()}: o')
        print('----------')
        for row in range(game.demension):
            test = '| '
            for col in range(game.demension):
                test = test + f'{game.elements[row][col]} | '
            print(test)
            print('----------')
        if flag == 0:
            given_position = input(f'{game.players[0].get_color()} turn:')
            game.elements[int(given_position[0])][int(given_position[1])] = 'x'
            flag = 1
        else:
            given_position = input(f'{game.players[1].get_color()} turn:')
            game.elements[int(given_position[0])][int(given_position[1])] = 'o'
            flag = 0

        if game.win_check(given_position):
            return print((f'{elements[int(given_position[0])][int(given_position[1])]} won'))
    return print('Tie!')




def start_game_gui(game):
    import tkinter as tk


    window = tk.Tk()
    for i in range(game.demension):
        for j in range(game.demension):
            frame = tk.Frame(master=window, relief = tk.RAISED, borderwidth=5)
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f'{game.elements[i][j]}')
            label.pack()
    window.mainloop()



game1 = Game(3,3,2)
player1 = Player('red', 0)
game1.add_player(player1)
player2 = Player('blue', 1)
game1.add_player(player2)
start_game_commandline(game1)
start_game_gui(game1)

