import tkinter as tk
from tkinter import messagebox

wn= tk.Tk()
wn.title("Tic Tac Toe by @11dome11")

def disable_all_button():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")
    
def check_won():
    global winner
    winner= False
    if b1["text"]== "X" and b2["text"]== "X" and b3["text"]== "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player X wins!")
        disable_all_button()
    elif b4["text"]== "X" and b5["text"]== "X" and b6["text"]== "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player X wins!")
        disable_all_button()
    elif b7["text"]== "X" and b8["text"]== "X" and b9["text"]== "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player X wins!")
        disable_all_button()
    elif b1["text"]== "X" and b4["text"]== "X" and b7["text"]== "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player X wins!")
        disable_all_button()
    elif b2["text"]== "X" and b5["text"]== "X" and b8["text"]== "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player X wins!")
        disable_all_button()
    elif b3["text"]== "X" and b6["text"]== "X" and b9["text"]== "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player X wins!")
        disable_all_button()
    elif b1["text"]== "X" and b5["text"]== "X" and b9["text"]== "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player X wins!")
        disable_all_button()
    elif b3["text"]== "X" and b5["text"]== "X" and b7["text"]== "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player X wins!")
        disable_all_button()
    elif b1["text"]== "O" and b2["text"]== "O" and b3["text"]== "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player O wins!")
        disable_all_button()
    elif b4["text"]== "O" and b5["text"]== "O" and b6["text"]== "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player O wins!")
        disable_all_button()
    elif b7["text"]== "O" and b8["text"]== "O" and b9["text"]== "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player O wins!")
        disable_all_button()
    elif b1["text"]== "O" and b4["text"]== "O" and b7["text"]== "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player O wins!")
        disable_all_button()
    elif b2["text"]== "O" and b5["text"]== "O" and b8["text"]== "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player O wins!")
        disable_all_button()
    elif b3["text"]== "O" and b6["text"]== "O" and b9["text"]== "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player O wins!")
        disable_all_button()
    elif b1["text"]== "O" and b5["text"]== "O" and b9["text"]== "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player O wins!")
        disable_all_button()
    elif b3["text"]== "O" and b5["text"]== "O" and b7["text"]== "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe by @11dome11","Player O wins!")
        disable_all_button()
    
    if count==9 and winner==False:
         messagebox.showinfo("Tic Tac Toe by @11dome11","It's a Tie!")
         disable_all_button()
         
def b_click(b):
    global clicked, count
    if b["text"]==" " and clicked==True:
        b.config(text="X")
        clicked=False
        count+=1
        check_won()
    elif b["text"]==" " and clicked==False:
        b.config(text="O")
        clicked=True
        count+=1
        check_won()
    else:
        messagebox.showerror("Tic Tac Toe by @11dome11", "Box has already been selected\nPick another box")

def restart():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked, count
    clicked=True
    count=0
    
    b1= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b1))
    b2= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b2))
    b3= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b3))
    b4= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b4))
    b5= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b5))
    b6= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b6))
    b7= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b7))
    b8= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b8))
    b9= tk.Button(wn, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", activebackground="white",command=lambda: b_click(b9))
    
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


my_menu= tk.Menu(wn)
wn.config(menu=my_menu)
option_menu=tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Option", menu=option_menu)
option_menu.add_command(label="Restart game", command=lambda:restart())


restart()
wn.mainloop()



