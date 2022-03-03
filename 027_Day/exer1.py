import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="I am a Label",font=("Arial", 16))
# my_label.pack(side="left")
# my_label.place(x=100,y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)

#Button
def button_clicked():
    my_label["text"] = input.get()

my_button = tkinter.Button(text="Click me", command=button_clicked)
# my_button.pack()
my_button.grid(column=1,row=1)


my_button2 = tkinter.Button(text="Click me", command=button_clicked)
# my_button.pack()
my_button2.grid(column=6,row=0)

#Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=5, row=2)




window.mainloop()