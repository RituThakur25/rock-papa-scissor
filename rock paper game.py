from tkinter import *

import random

def play_game(player_choice):
    choices=["rock","paper","scissor"]
    computer_choice=random.choice(choices)
    lbl2.config(text=f"computer choose-{computer_choice}")
    if computer_choice==player_choice:
        lbl3.config(text="match tie")
    elif(player_choice=="rock" and computer_choice=="scissor") or (player_choice=="paper" and computer_choice=="rock") or (player_choice=="scissor" and computer_choice=="paper"):
        lbl3.config(text="you win")
    else:
        lbl3.config(text="computer win")
window=Tk()
window.geometry("800x500")
window["bg"]="skyblue"
window.title("ROCK_PAPER_SCISSOR_GAME")

lbl1=Label(window,text="ROCK_PAPER_SCISSOR_GAME",font="arial 30 bold",bg="blue",fg="white")
lbl1.pack()
        
btn=Button(window,text="Rock",padx=50,pady=30,command=lambda:play_game("rock"))
btn.place(x=70,y=150)

btn=Button(window,text="Paper",padx=50,pady=30,command=lambda:play_game("paper"))
btn.place(x=340,y=150)
        
btn=Button(window,text="Scissor",padx=50,pady=30,command=lambda:play_game("scissor"))
btn.place(x=610,y=150)
        
lbl2= Label(window,font="arial 20 bold")
lbl2.place(x=300,y=300)
lbl3= Label(window,font="arial 20 bold")
lbl3.place(x=300,y=400)
mainloop()
