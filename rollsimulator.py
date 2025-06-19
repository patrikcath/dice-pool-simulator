#@patrikcath

#imports
from tkinter import Tk, Label, Button, Entry, W, PhotoImage, TclError
from random import seed, randint
from time import time

def setup():
    #seed the RNGenerator
    seed(time)

    #set up tkinter
    root = Tk()
    root.title("Dice simulator")

    #attempt to set the program's icon
    try:
        icon = PhotoImage(file="icon.png")
        root.iconphoto(False,icon)
    except TclError:#TclError happens when a file does not exist
        print("Icon file not found")

    return root

def gridLabel(inRow, inColumn, inColumnspan=1, inText="", inSticky=W):
    #creates a label and places it using tkinter's grid system
    label = Label(root, text=inText)
    label.grid(row=inRow, column=inColumn, columnspan=inColumnspan, sticky=inSticky)
    return label

def gridEntry(inRow, inColumn, inDefault, inSticky=W):
    #creates an entry widget and places it using tkinter's grid system
    entry = Entry(root)
    entry.grid(row=inRow, column=inColumn,sticky=inSticky)
    entry.insert(0, inDefault)
    return entry

def generate():
    #roll a dice with a specified amount of sides a specified number of times, then apply modifiers and advantages and display the result
    try:
        #roll the dice
        rolls = [1] * (int(diceInputEntry.get()) + abs(int(advantageInputEntry.get())))
        for i in range(len(rolls)):
            rolls[i] = randint(1, int(sidesInputEntry.get()))

        #display the dice rolls
        rollsLabel.configure(text=f"Rolls: {str(rolls)[1:-1]}")

        #process advantage, display what the dis/advantage is if there is one
        if int(advantageInputEntry.get()) > 0:#if there's a advantage, remove n lowest rolls from the pool, where n is equivalent to the level of advantage
            advantageLabel.configure(text=f"Rolling with a +{int(advantageInputEntry.get())} advantage")
            for i in range(0,int(advantageInputEntry.get())):
                rolls.pop(rolls.index(min(rolls)))
        elif int(advantageInputEntry.get()) < 0:#if there's a disadvantage, remove n HIGHEST rolls from the pool, where n is equivalent to the level of disadvantage
            advantageLabel.configure(text=f"Rolling with a {int(advantageInputEntry.get())} disadvantage")
            for i in range(0,int(advantageInputEntry.get())):
                rolls.pop(rolls.index(max(rolls)))
        else:#if there's no advantage or disadvantage don't display anything
            advantageLabel.configure(text="")

        #display and apply the modifier
        #a modifier adds or subtracts a value from the final result
        if int(modifierInputEntry.get()) > 0:
            modifierLabel.configure(text=f"Modifier: +{int(modifierInputEntry.get())}")
        elif int(modifierInputEntry.get()) < 0:
            modifierLabel.configure(text=f"Modifier: {int(modifierInputEntry.get())}")
        else: modifierLabel.configure(text="")
        rolls.append(int(modifierInputEntry.get()))
        
        #display the result
        totalLabel.configure(text=f"Total: {sum(rolls)}")

    except ValueError:
        print("Failed to generate dice pool: one or more of the inputs isn't a number")

root = setup()

#label widgets to label the entry fields
gridLabel(0, 0, inText="Number of dice: ")
gridLabel(1, 0, inText="Sides: ")
gridLabel(2, 0, inText="Modifier: ")
gridLabel(3, 0, inText="Advantage: ")

#entry widgets to take user inputs
diceInputEntry = gridEntry(0, 1, 1)
sidesInputEntry = gridEntry(1, 1, 20)
modifierInputEntry = gridEntry(2, 1, 0)
advantageInputEntry = gridEntry(3, 1, 0)

#button widget to generate the dice pool (doesn't get a function because there's just one)
generateButton = Button(root, text="Roll",command=generate).grid(row=4, column=0, columnspan=2, ipadx=10, ipady=5, pady=10)

#label widgets to show the outputs
#the column span for these is very wide to stop them from affecting the width of the entire column.
advantageLabel = gridLabel(5, 0, 999)
modifierLabel = gridLabel( 6, 0, 999)
rollsLabel = gridLabel(7, 0, 999)
totalLabel = gridLabel(8, 0, 999)

root.mainloop()
