import tkinter as tk
from ttkbootstrap import Style
# no win or lose check

# functions
def button_on_click(row, col):
    global player_turn
    if player_turn == 0:
        if list[row][col]["text"] == "":
            list[row][col].config(text="O")
            player_turn = 1
    elif player_turn == 1:
        if list[row][col]["text"] == "":
            list[row][col].config(text="X")
            player_turn = 0

# window adjust
window = tk.Tk()
style = Style("darkly")
window.geometry("390x380")
window.title("Tic-Tac-Toe")

# widgets
list = [[None, None, None] for _ in range(3)]
player_turn = 0  # 0 for X, 1 for O

for rows in range(3):
    for cols in range(3):
        list[rows][cols] = tk.Button(
            master=window,
            font=('Helvetica', 14, 'bold'),
            width= 10, height=5,
            text="",
            borderwidth=2,
            relief="solid",
            command=lambda r=rows, c=cols: button_on_click(r, c)
        )
        list[rows][cols].grid(row=rows, column=cols, padx=2, pady=2)

# run
window.mainloop()
