from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=20)

#Label
lable = Label(text=" is equal to:")
lable.grid(column=0, row=1)

#Entries
entry = Entry(width=10)
#Add some text begin
entry.insert(END, string="0")

entry.grid(column=1, row=0)

#Label_result
lable_result = Label(text="0")
lable_result.grid(column=1, row=1)

#Button calculate
def action():
    lable_result["text"] = round((int(entry.get()) * 1.61))

butto = Button(text="Calculate", command=action)
butto.grid(column=1,row=2)

#Label_miles
lable_miles = Label(text="Miles")
lable_miles.grid(column=2, row=0)

#Label_km
lable_km = Label(text="km")
lable_km.grid(column=2, row=1)








window.mainloop()

