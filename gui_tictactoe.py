# Tic Tac Toe game with a GUI
# Version 1.0
# Author: Bernhard Raab
# Imports
import tkinter as tk
from tkinter import messagebox

root = tk.Tk() # this indicates the beginning of the interface

# canvas
canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(columnspan=3, rowspan=3)


# handle turns
player = True  # True == Player X
count = 0 # counts the number of turns


# Winner by default
winner = None

# Handle clicked buttons
def btn_clicked(btn_nr):
    global player, count

    if btn_nr["text"] == " " and player:
        btn_nr["text"] = "X"
        player = False
        count += 1
        check_for_winner()
    elif btn_nr["text"] == " " and player == False:
        btn_nr["text"] = "O"
        player = True
        count += 1
        check_for_winner()
    else:
        messagebox.showerror("Tic Tac Toe",
                             "Box has already been selected! Click another one")



# Create reset function to restart game
def start_game():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global player, count
    player = True
    count = 0
    # Add play buttons
    b1 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,
                   command=lambda: btn_clicked(b1))
    b2 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,
                   command=lambda: btn_clicked(b2))
    b3 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,

                   command=lambda: btn_clicked(b3))
    b4 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,
                   command=lambda: btn_clicked(b4))
    b5 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,
                   command=lambda: btn_clicked(b5))
    b6 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,

                   command=lambda: btn_clicked(b6))
    b7 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,
                   command=lambda: btn_clicked(b7))
    b8 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,
                   command=lambda: btn_clicked(b8))
    b9 = tk.Button(root, text=" ", font="Raleway", height=2, width=4,
                   command=lambda: btn_clicked(b9))


    # Display boxes
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

# Create Menu
menu = tk.Menu(root)
root.config(menu=menu)

# Create Options
options_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=start_game)

#__________________________________________

# disable all the buttons
def disable_all_buttons():
    b1.config(state=tk.DISABLED)
    b2.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)

    b4.config(state=tk.DISABLED)
    b5.config(state=tk.DISABLED)
    b6.config(state=tk.DISABLED)

    b7.config(state=tk.DISABLED)
    b8.config(state=tk.DISABLED)
    b9.config(state=tk.DISABLED)


# Check if there is a winner and if who won
def check_for_winner():

    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
        messagebox.showinfo("Tic Tac Toe", "{} is the winner!".format(winner))
    elif column_winner:
        winner = column_winner
        messagebox.showinfo("Tic Tac Toe", "{} is the winner!".format(winner))
    elif diagonal_winner:
        winner = diagonal_winner
        messagebox.showinfo("Tic Tac Toe", "{} is the winner!".format(winner))
    else:
        check_for_tie()
        winner = None


# Check if there is a winner in rows
def check_rows():

    row_1 = b1["text"] == b2["text"] == b3["text"] != " "
    row_2 = b4["text"] == b5["text"] == b6["text"] != " "
    row_3 = b7["text"] == b8["text"] == b9["text"] != " "

    # check which row has won
    if row_1:
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        disable_all_buttons()
        return b1["text"]

    elif row_2:
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        disable_all_buttons()
        return b4["text"]

    elif row_3:
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        disable_all_buttons()
        return b7["text"]

    else:
        return


# Check if there is a winner in columns
def check_columns():

    column_1 = b1["text"] == b4["text"] == b7["text"] != " "
    column_2 = b2["text"] == b5["text"] == b8["text"] != " "
    column_3 = b3["text"] == b6["text"] == b9["text"] != " "

    # check which column has won
    if column_1:
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        disable_all_buttons()
        return b1["text"]

    elif column_2:
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        disable_all_buttons()
        return b2["text"]

    elif column_3:
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        disable_all_buttons()
        return b3["text"]

    else:
        return

# Check if there is a winner in the diagonals
def check_diagonals():

    diagonal_1 = b1["text"] == b5["text"] == b9["text"] != " "
    diagonal_2 = b3["text"] == b5["text"] == b7["text"] != " "

    # check which diagonal has won
    if diagonal_1:
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        disable_all_buttons()
        return b1["text"]

    if diagonal_2:
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        disable_all_buttons()
        return b3["text"]


# Check if there is a tie
def check_for_tie():
    # if no one has won yet, check if there are empty spots in list
    if count == 9 and winner==None:
        messagebox.showinfo("Tic Tac Toe", "It is a tie!")
    return

start_game()

root.mainloop() # this indicates the end of the interface
