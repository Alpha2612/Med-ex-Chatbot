#Creating GUI with tkinter
from tkinter import *
from main import get_response



def click(*args):
    global flag
    if flag:
        EntryBox.delete("0.0",END)
        flag=False
  
# call function when we leave entry box
def leave(*args):
    EntryBox.delete("0.0",END)
    EntryBox.insert(END, 'At your service')
    base.focus()

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#040008", font=("Verdana", 12 ))
    
        res = get_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

flag=True

base = Tk()
base.title("Med-ex")
base.geometry("600x800")
base.resizable(width=False, height=False)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5, bd=0, bg="#25be39", activebackground="#25be39",fg='#ffffff',command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox.insert(END,'At your service....')
EntryBox.pack(pady=10)

# Use bind method
EntryBox.bind("<Button-1>", click)


# Place all components on the screen
scrollbar.place(x=586,y=6, height=680)
ChatLog.place(x=6,y=6, height=680, width=580)
EntryBox.place(x=6, y=700, height=90, width=470)
SendButton.place(x=490, y=700, height=90, width=100)

base.mainloop()