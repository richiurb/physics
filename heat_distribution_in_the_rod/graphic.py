import tkinter
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from config import Config
from matrix import Matrix


class Graphic:
    TITLE = "Heat distribution in the rod(t = "

    def __init__(self, a, u):
        self.root = tkinter.Tk()
        self.root.title(self.TITLE + str(0) + ")")
        self.a = a
        self.u = u
        self.click = 0
        self.button = tkinter.Button(
            text="Next",
            background="#555",
            foreground="#ccc",
            padx="20",
            pady="8",
            font="16",
            command=self.button
        )

    def get(self):
        self.button.pack()

        self.root.mainloop()

    def button(self):
        if self.click != 0:
            self.root.title(self.TITLE + str(self.click * Config.DELTA_T) + ")")

        fig, ax = plt.subplots()
        print("t = " + str(self.click * Config.DELTA_T))
        print(self.u)
        print("--------")
        for i in range(len(self.u)):
            current_x = i * Config.DELTA_X
            ax.scatter(current_x, self.u[i])

        ax.set_xlim([0, Config.LENGTH])
        ax.set_ylim([-1, 1])
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
        ax.grid()
        plt.show()

        self.click += 1

        self.u = Matrix(self.u, self.a).solve()
