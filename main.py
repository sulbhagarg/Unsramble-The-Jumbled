import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle

def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 
             'mathematics', 'player', 'condition', 'reverse', 
             'water', 'board', 'geeks']
    pick = random.choice(words)
    return pick 

def jumble(word): 
    random_word = random.sample(word, len(word)) 
    jumbled = ''.join(random_word) 
    return jumbled 

def initial():
    global picked_word, points, total
    points = int(0)
    total = int(1)
    picked_word = choose()
    jumbled_word = jumble(picked_word)
    lbl1.configure(text = jumbled_word)

def ans_check():
    user_input = e1.get()
    global points, total
    if user_input == picked_word:
        points = points + 1
        msg = "Correct!!! Your Current Score is: " + str(points) + " / " + str(total)
        messagebox.showinfo("Success", msg)
        Reset()
    else:
        msg = "Not Correct!!! Your Current Score is: " + str(points) + " / " + str(total)
        messagebox.showinfo("Error", msg)
        e1.delete(0, END)

def Reset():
    global picked_word, total
    total = total + 1
    picked_word = choose()
    jumbled_word = jumble(picked_word)
    lbl1.configure(text = jumbled_word)
    e1.delete(0, END)

def new_game():
    global points, total
    total = total - 1
    messagebox.showinfo("Success", "Your game score is: " + str(points) + " out of " + str(total))
    points = int(0)
    total = int(0)
    Reset()

root = tkinter.Tk()
root.geometry("400x400")
root.title("Unsramble The Jumbled")
root.configure(background="#000000")

lbl1 = Label(root, font='times 20', bg="#000000", fg="#ffffff")
lbl1.pack(pady=30, ipady=10, ipadx=10)

answer = StringVar()
e1 = Entry(root, textvariable=answer)
e1.pack(ipady=5, ipadx=5)

button1 = Button(root, text="Check", width=20, command=ans_check)
button1.pack(pady=40)

button2 = Button(root, text="Next", width=20, command=Reset)
button2.pack()

button3 = Button(root, text="New Game", width=20, command=new_game)
button3.pack(pady=40)

initial()

root.mainloop()
