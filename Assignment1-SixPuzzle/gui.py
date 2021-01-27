from tkinter import *
import algorithms
from state import START_STATE

root = Tk()
root.title("Assignment1 (COMP-424) - Six Puzzle")
root.geometry("800x400")

ALGORITHMS = ["Breadth First Search", "Uniform Cost Search", "Depth First Search", "Iterative Deepening"]


class GUI:
    def __init__(self):
        # Initialize
        self.states = []
        self.index = 0
        self.notification = StringVar()
        self.notification_extra = StringVar()
        self.state_number = StringVar()
        self.b1 = StringVar()
        self.b2 = StringVar()
        self.b3 = StringVar()
        self.b4 = StringVar()
        self.b5 = StringVar()
        self.b6 = StringVar()
        self.algorithm = StringVar()
        self.algorithm.set(ALGORITHMS[0])
        self.notification.set("No algorithm has been run.")
        self.notification_extra.set("")
        self.state_number.set("")

    def clear_state(self):
        self.b1.set("")
        self.b2.set("")
        self.b3.set("")
        self.b4.set("")
        self.b5.set("")
        self.b6.set("")

    def next_state(self):
        self.b1.set(self.states[self.index][0][0])
        self.b2.set(self.states[self.index][0][1])
        self.b3.set(self.states[self.index][0][2])
        self.b4.set(self.states[self.index][1][0])
        self.b5.set(self.states[self.index][1][1])
        self.b6.set(self.states[self.index][1][2])
        self.state_number.set("State number: " + str(self.index + 1))
        if self.index == len(self.states) - 1:
            if not (self.index == 0):
                self.notification.set("REACHED END STATE (you review them)")
            self.index = -1
        self.index += 1

    def reset(self):
        self.states = []
        self.index = 0
        self.clear_state()
        self.notification.set("No algorithm has been run.")
        self.notification_extra.set("")
        self.state_number.set("")

    def run(self):
        if self.algorithm.get() == ALGORITHMS[0]:
            self.run_bfs()
        elif self.algorithm.get() == ALGORITHMS[1]:
            self.run_uniform_cost_search()
        elif self.algorithm.get() == ALGORITHMS[2]:
            self.run_dfs()
        else:
            self.run_iterative_deepening()

    def run_bfs(self):
        self.notification.set("Running Breadth First Search")
        answer = algorithms.breadth_first_search(START_STATE)
        self.states = answer[0]
        self.notification_extra.set(str(answer[1]) + " total states visited.\n" +
                                    str(len(answer[0])) + " states in solution path")
        self.notification.set("Loaded Breadth First Search states")

    def run_dfs(self):
        self.notification.set("Running Depth First Search")
        answer = algorithms.depth_first_search(START_STATE)
        self.states = answer[0]
        self.notification_extra.set(str(answer[1]) + " total states visited.\n" +
                                    str(len(answer[0])) + " states in solution path")
        self.notification.set("Loaded Depth First Search states")

    def run_uniform_cost_search(self):
        self.notification.set("Running Uniform Cost Search")
        answer = algorithms.uniform_cost_search(START_STATE)
        self.states = answer[0]
        self.notification_extra.set(str(answer[1]) + " total states visited.\n" +
                                    str(len(answer[0])) + " states in solution path")
        self.notification.set("Loaded Uniform Cost Search states")

    def run_iterative_deepening(self):
        self.notification.set("Running Iterative Deepening Search")
        answer = algorithms.iterative_deepening(START_STATE)
        self.states = answer[0]
        self.notification_extra.set(str(answer[1]) + " total states visited.\n" +
                                    str(len(answer[0])) + " states in solution path\n" +
                                    str(answer[2]) + " was depth level of the solution (counting 0 as root)")
        self.notification.set("Loaded Iterative Deepening Search states")


my_gui = GUI()

label_1 = Label(root, text="Algorithm: ")
label_algorithm = Label(root, textvariable=my_gui.algorithm)
label_notification = Label(root, fg="red", textvariable=my_gui.notification)
label_notification_extra = Label(root, fg="green", textvariable=my_gui.notification_extra)
label_state_number = Label(root, fg="blue", textvariable=my_gui.state_number)
reset_button = Button(root, fg='blue', text="RESET", command=my_gui.reset, padx=10, pady=10)
run_button = Button(root, fg='green', text="RUN", command=my_gui.run, padx=10, pady=10)
next_state = Button(root, fg='green', text="Next State", command=my_gui.next_state, padx=10, pady=10)

# Create blocks
block1 = Label(root, textvariable=my_gui.b1, height=5, width=10, bg="grey")
block2 = Label(root, textvariable=my_gui.b2, height=5, width=10, bg="grey")
block3 = Label(root, textvariable=my_gui.b3, height=5, width=10, bg="grey")
block4 = Label(root, textvariable=my_gui.b4, height=5, width=10, bg="grey")
block5 = Label(root, textvariable=my_gui.b5, height=5, width=10, bg="grey")
block6 = Label(root, textvariable=my_gui.b6, height=5, width=10, bg="grey")

# Create radio button
for al in (range(len(ALGORITHMS))):
    Radiobutton(root, text=ALGORITHMS[al], variable=my_gui.algorithm,
                value=ALGORITHMS[al]).place(x=al * 200, y=50)

# Place widgets on screen
label_1.place(x=220, y=10)
label_algorithm.place(x=300, y=10)
label_notification.place(x=500, y=150)
label_notification_extra.place(x=200, y=340)
label_state_number.place(x=170, y=100)
reset_button.place(x=1, y=1)
run_button.place(x=700, y=1)
next_state.place(x=700, y=350)
block1.place(x=150, y=150)
block2.place(x=250, y=150)
block3.place(x=350, y=150)
block4.place(x=150, y=250)
block5.place(x=250, y=250)
block6.place(x=350, y=250)

root.mainloop()

# NOTES
# label.pack() # -- for packing it anywhere on the screen
