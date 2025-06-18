#@patrikcath
#not my best work but it gets the job done and I ran out of bugs to fix. Cleaning up the code and extra functionality will come soon.

#imports
from tkinter import Tk, Label, Button, Entry, W, PhotoImage, TclError
from random import seed, randint
from time import time

#set up modules
seed(time)
root = Tk()
root.title("Dice simulator")

#setting the program's icon is inside a try-except to make it marginally easier to share the code. It'll be changed in a future version
try:
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False,icon)
except TclError:#TclError happens when a file does not exist
    print("Missing icon.png")

def generate():
    #roll a dice with a specified amount of sides a specified number of times, then apply modifiers and advantages
    rolls = []
    try:
        #get inputs
        numberOfDice = int(diceInputEntry.get())
        sidesPerDice = int(sidesInputEntry.get())
        modifier = int(modifierInputEntry.get())
        advantage = int(advantageInputEntry.get())

        #roll the dice
        for i in range(numberOfDice+abs(advantage)):
            diceRoll = randint(1,sidesPerDice)
            rolls.append(diceRoll)

        #display the rolls
        rollsLabel.configure(text=f"Rolls: {str(rolls)[1:-1]}")

        #process advantage, display what the dis/advantage is if there is one
        #advantage adds extra dice to the roll. positive advantage removes the lowest dice of the roll, negative advantage removes the highest dice
        if advantage > 0:#positive advantage
            advantageLabel.configure(text=f"Rolling with a +{advantage} advantage")
            for i in range(0,advantage):
                rolls.pop(rolls.index(min(rolls)))
        elif advantage < 0:#disadvantage
            advantageLabel.configure(text=f"Rolling with a {advantage} disadvantage")
            for i in range(0,advantage):
                rolls.pop(rolls.index(max(rolls)))
        else:#no dis/advantage
            advantageLabel.configure(text="")

        #display and apply the modifier
        #modifier adds or subtracts a value from the final result
        if modifier > 0:
            modifierLabel.configure(text=f"Modifier: +{modifier}")
        elif modifier < 0:
            modifierLabel.configure(text=f"Modifier: {modifier}")
        else: modifierLabel.configure(text="")
        rolls.append(modifier)
        
        #display the result
        totalLabel.configure(text=f"Total: {sum(rolls)}")

    except ValueError:#should only come up if one of the inputs isn't a number
        pass#nothing happens - this line only exists because try statements require exception handling


#generate and place labels
Label(root, text="Number of dice: ").grid(row=0, column=0,sticky=W)
Label(root, text="Sides: ").grid(row=1, column=0,sticky=W)
Label(root, text="Modifier: ").grid(row=2,column=0,sticky=W)
Label(root, text="Advantage: ").grid(row=3,column=0,sticky=W)

#generate and place user inputs and set defaults
diceInputEntry = Entry(root)
diceInputEntry.grid(row=0, column=1,sticky=W)
diceInputEntry.insert(0,1)
sidesInputEntry = Entry(root)
sidesInputEntry.grid(row=1,column=1,sticky=W)
sidesInputEntry.insert(0,20)
modifierInputEntry = Entry(root)
modifierInputEntry.grid(row=2,column=1,sticky=W)
modifierInputEntry.insert(0,0)
advantageInputEntry = Entry(root)
advantageInputEntry.grid(row=3,column=1,sticky=W)
advantageInputEntry.insert(0,0)

#generate and place the roll button
generateButton = Button(root, text="Roll",command=generate).grid(row=4, column=0,columnspan=2,ipadx=10,ipady=5,pady=10)

#the output labels used to be initialised inside generate(), but that caused some really strange graphical bugs.
#the labels have high columnspans to stop columns from unintentionally shifting around
advantageLabel = Label(root)
advantageLabel.grid(row=5,column=0,sticky=W,columnspan=999)
modifierLabel = Label(root)
modifierLabel.grid(row=6,column=0,sticky=W,columnspan=999)
rollsLabel = Label(root)
rollsLabel.grid(row=7,column=0,sticky=W,columnspan=999)
totalLabel = Label(root)
totalLabel.grid(row=8,column=0,sticky=W,columnspan=999)

root.mainloop()