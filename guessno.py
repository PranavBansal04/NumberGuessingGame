
#importing tkinter and random module
from tkinter import *
import random
import time


#creating GUI class
class GUI:
    #__init__ method with dfault parameter
    def __init__(self):
        #generating random integer
        self.randint=random.randint(1,1000)
        #printing the generated integer for reference
        #comment the below line if you are done with checking, it will not be needed
        print(self.randint)
        #initializing round number to 1
        self.round_no=1
        #create tkinter window
        self.root=Tk()
        #a variable which will be used for display text in Label
        self.display_text=StringVar()
        #variable for storing the text from tkinter entry
        self.text_input=StringVar()
        #display text in the starting
        self.display_text.set("\tRound : "+str(self.round_no))
        #title for the window
        self.root.title("Number Guessing Game")
        #settign background color
        self.root.configure(background="white")
        #Label with text asking for number input, bg->background color
        #positioning of the widgets(Label,entry,button) is done using place()
        Label(self.root,text="Guess a number from 1 to 1000: ",bg="white",font="15,bold").place(relx=0.1,rely=0.05)
        #Entry where number will be entered, we can keep the text inside entry a variable
        #it doesent need to be fixed, for that textvariable instead of text is used, bd->border
        self.e=Entry(self.root,bd=3,width=7,textvariable=self.text_input).place(relx=0.4,rely=0.25)
        #label with variable display text
        Label(self.root,textvariable=self.display_text,bg="white",font=("arial",10,"bold")).place(relx=0,rely=0.42)
        #button for processing the input, command for it calls the check function
        self.b=Button(self.root,text="Enter",bg="white",command=self.check).place(relx=0.41,rely=0.75)
        #button for closing the window
        self.b1=Button(self.root,text="close",bg="white",command=self.root.destroy).place(relx=0.41,rely=0.85)
        #widow size can be manipulated using geometry
        self.root.geometry("300x200")
        #infinite loop so window does not get closed
        self.root.mainloop()

    #this function will be called when button is pressed
    def check(self):
        #storing the data of entry in tkinter window inside a variable
        entry_value=self.text_input.get()
        #clearing the data inside the entry
        self.text_input.set("")
        #now the code will try to convert the input value to integer
        #if the value cant be converted to integer then it will give error
        #and an exception will be raised
        try:
            entry_value=int(entry_value)
            #now although the value is successfully but
            #it can still be greater than 1000 or less than 0
            #which is also an invalid input
            if(entry_value<0 or entry_value>1000):
                self.display_text.set("Round : "+str(self.round_no)+"\nInvalid Input.\nEnter a valid integer.")

            #we need to store the previous value in a variable
            #as we need it later
            #there will be no previous value for the first round
            #so we need to update the value of previous_value variable in the starting only
            else:
                if(self.round_no==1):
                    self.previous_no=entry_value
                #if the user guesses the generated random number correctly
                #then a message with number of attempts will be shown
                #number of attempts will be equal to round number
                if(entry_value==self.randint):
                    self.display_text.set("You have guessed correctly!\nYou took "+str(self.round_no)+" attempts.\nNew Round started.")
            
                    #reset the round number
                    self.round_no=0
                    #generate a new random integer
                    self.randint=random.randint(1,1000)
                    print(self.randint)
                    
                #otherwise input value can either be greater or less than the generated number
                else:
                    #if the input value is greater
                    if(entry_value>self.randint):
                        #for the first round no comparison can be made with previous value
                        #so the display message will be shown accordingly
                        if(self.round_no==1):
                            self.display_text.set("Round : "+str(self.round_no)+"\nValue is greater than the Number.")
                        #if its not the first round then we need to compare the entered value
                        #with previous value
                        else:
                            #if the entered value is closer to the number than previous value
                            if(abs(self.previous_no-self.randint)>abs(entry_value-self.randint)):
                               self.display_text.set("Round : "+str(self.round_no)+"\nValue is greater than the Number.\nYou are moving closer from previous number.")
                            #if the entered value is farther from the number than previous value 
                            else:
                               self.display_text.set("Round : "+str(self.round_no)+"\nValue is greater than the Number.\nYou are moving farther from previous number")
                    #if input value is less than the genrated random integer
                    else:
                        #no comparison for the first round as we dont have any previous value
                        if(self.round_no==1):
                            self.display_text.set("Round : "+str(self.round_no)+"\nValue is less than the Number.")
                        #if its not the first round then display message will be shown accordingly
                        else:
                            if(abs(self.previous_no-self.randint)>abs(entry_value-self.randint)):
                                self.display_text.set("Round : "+str(self.round_no)+"\nValue is less than the Number.\nYou are moving closer from previous number.")
                            else:
                                self.display_text.set("Round : "+str(self.round_no)+"\nValue is less than the Number.\nYou are moving farther from previous number")
                #finally we need to update the value of previous_no variable
                #as the program is moving to the next round
                #this value will be used in the next round
                self.previous_no=entry_value
                #updating round number
                self.round_no+=1
        #if exception is raised then proper message will be shown thorugh
        #display_text variable
        except Exception:
            self.display_text.set("Round : "+str(self.round_no)+"\nInvalid Input.\nEnter a valid integer.")

#calling GUI class to initiate the program
GUI()


        
