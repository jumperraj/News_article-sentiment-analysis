from tkinter import *
from tkinter.ttk import Style

from pandastable import Table, TableModel
import Sentiment_analysis_engine

class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.master.geometry('1500x700')
            self.main.title('Table app')
            self.configure(bg="black")
            f = Frame(self.main)
            f.place(x=0,y=0)

            f.pack(fill=BOTH,expand=1,padx=30,pady=30)
            # df2 = TableModel.getSampleData()
            self.table = pt = Table(f, dataframe=Sentiment_analysis_engine.df2,
                                    showtoolbar=True, showstatusbar=True)
            self.initUI()
            pt.show()

        def initUI(self):
            self.style = Style()
            self.pack(fill=BOTH, expand=1)
            Button1 = Button(self, text="Generate Sentiment",
                                command=self.display,fg="black",bg="#d7f542",width=25,height=2,border=0,font="lucida 15 bold")
            Button1.place(x=600, y=0)
            Button1.bind("<Enter>", self.on_enter)
            Button1.bind("<Leave>", self.on_leave)

        def display(self):
            global screen
            screen = Toplevel(self.main)
            screen.title("Login")
            screen.geometry("1300x120")
            Label(screen, text=f"{Sentiment_analysis_engine.string}",fg="white",bg="black",borderwidth=2, font="time 15 ").pack(fill=BOTH)

        def on_enter(self,e):
            e.widget['background'] = 'green'

        def on_leave(self,e):
            e.widget['background'] = '#d7f542'





app = TestApp()
#launch the app
app.mainloop()