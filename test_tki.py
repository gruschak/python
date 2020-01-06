import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class MApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.frame1 = tk.Frame(self, background='Gray')
        self.frame1.pack(side='left')

        self.frame2 = tk.Frame(self, background='Gray')
        self.frame2.pack(side='right')

        self.b_stop = tk.Button(self.frame2, text="Выход", fg="red", command=self.master.destroy)
        self.b_stop.pack(side='left', padx=10, pady=20)
         
        self.b_rec = tk.Button(self.frame1, text="Подписаться", command=self.cmd)
        self.b_rec.pack(side='left', padx=10, pady=20)

        self.b_exit = tk.Button(self.frame1, text="Отписаться", command=self.cmd)
        self.b_exit.pack(side='left', padx=10, pady=20)

        self.frame_text = ScrolledText()
        self.frame_text.pack(side='bottom')
                
        #self.quit = 
        #self.quit.pack(side="bottom")

    def cmd(self):
        return None


if __name__ == "__main__":
    root = tk.Tk()
    app = MApp(root)
    app.mainloop()


""" 

 
label = Label(text='')
label.pack()

"""

 

