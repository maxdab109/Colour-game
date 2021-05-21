from tkinter import*
import random
from tkinter import messagebox
color = ['Red', 'Green', 'Yellow', 'Blue', 'White', 'Orange', 'Brown']

score = 0
timeleft = 30
def startGame(event):
    if  timeleft == 30:
        countdown()
    nextColour()
def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == color[1].lower():
            score += 1

        e.delete(0, END)
        random.shuffle(color)
        label.config(fg=str(color[1]), text=str(color[0]))
        scoreLabel.config(text="Score:" + str(score))
    else:
         messagebox.showinfo('Game Over', 'Your Score is=' + str(score))
def countdown():
        global timeleft
        if timeleft > 0:
            timeleft -= 1
            timeLabel.config(text="Timeleft:"+ str(timeleft))
            timeLabel.after(1000, countdown)


root = Tk()
root.title("COLORGAME")
root.geometry("900x650")
scoreLabel =  Label(root, text="Score:" + str(score))
scoreLabel.pack()
instructions = Label(root, text="Type in the colour of the words, and not the word text")
timeLabel =Label(root, text="Time left:" +str(timeleft))
timeLabel.pack()
label = Label(root, font=("Helvetica", 12))
label.pack()
e = Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()