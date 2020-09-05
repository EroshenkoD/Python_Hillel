import tkinter as tk


class Calculator(tk.Frame):
    CANVAS_WIDTH = 300
    CANVAS_HEIGHT = 400

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.tuple_button = ('1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '0', '.', '=/DEL', '/')
        self.enter_data = ''
        self._create_main_canvas()

    def _create_main_canvas(self):
        self.main_canvas = tk.Canvas(self, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.main_canvas.pack()

        self.top_frame = tk.Frame(self.main_canvas, bg='#80c1ff', bd=10)
        self.top_frame.place(relx=0.5, rely=0, relwidth=1, relheight=0.2, anchor='n')

        if not self.enter_data:
            text = '0'
        else:
            text = self.enter_data

        self.enter_wind = tk.Label(self.top_frame, bd=10, text=text, font=("Times New Roman", 40))
        self.enter_wind.place(relwidth=1, relheight=1)

        self.bot_frame = tk.Frame(self.main_canvas, bg='#00CED1')
        self.bot_frame.place(relx=0.5, rely=0.2, relwidth=1, relheight=0.8, anchor='n')

        x = 0.04
        y = 0.04

        for but in self.tuple_button:
            if x == 1:
                x = 0.04
                y += 0.24

            if but == '=/DEL':
                bg = '#008000'
            else:
                bg = '#80c1ff'

            button = tk.Button(self.bot_frame, text=but, bg=bg, font=15, command=lambda i=but: self._work(i))
            button.place(relx=x, rely=y, relwidth=0.2, relheight=0.2)
            x += 0.24

    def _work(self, text):
        if text == '=/DEL':
            if self.enter_data.replace('.', '').isdigit():
                self.enter_data = ''
                self._update()
            else:
                try:
                    self.enter_data = str(eval(self.enter_data))
                    self._update()
                except:
                    self.enter_data = 'Error'
                    self._update()
        else:
            self.enter_data += text
            self._update()

    def _update(self):
        if self.enter_data == '':
            self.enter_wind.config(text='0')
        elif self.enter_data == 'Error':
            self.enter_wind.config(text='Error')
            self.enter_data = ''
        else:
            self.enter_wind.config(text=self.enter_data)


if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(master=root)
    app.mainloop()
