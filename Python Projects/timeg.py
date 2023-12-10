from tkinter import *
import time

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="BLUE", font=("Helvetica", 50), bg="lightgreen")
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

root = Tk()
app=App(root)
root.wm_title("Tkinter clock")
root.geometry("200x200")
root.after(1000, app.update_clock)
root.mainloop()