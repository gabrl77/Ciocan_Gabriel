import tkinter as tk
import random
import time


class SortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sortare Vizuala")

        self.width = 1680
        self.height = 880
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack(side="left")

        self.num_elements = 10
        self.data = [random.randint(10, self.height - 10) for _ in range(self.num_elements)]

        self.speed_var = tk.DoubleVar(value=0.1)
        self.algorithm_var = tk.StringVar(value="Bubble Sort")

        self.create_controls()

        self.is_paused = False
        self.is_sorted = False

    def create_controls(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(side="right", padx=20, pady=20)

        algorithm_label = tk.Label(control_frame, text="Selecteaza algoritmul")
        algorithm_label.pack()

        algorithm_menu = tk.OptionMenu(control_frame, self.algorithm_var, "Bubble Sort", "Insertion Sort",
                                       "Selection Sort", "Bogo Sort")
        algorithm_menu.pack()

        speed_label = tk.Label(control_frame, text="Viteza")
        speed_label.pack()

        speed_slider = tk.Scale(control_frame, from_=0.01, to_=1, resolution=0.01, orient="horizontal",
                                variable=self.speed_var)
        speed_slider.pack()

        random_button = tk.Button(control_frame, text="Randomizeaza", command=self.randomize)
        random_button.pack()

        start_button = tk.Button(control_frame, text="Start", command=self.start_sorting)
        start_button.pack()

        pause_button = tk.Button(control_frame, text="Pauza", command=self.pause_sorting)
        pause_button.pack()

        reset_button = tk.Button(control_frame, text="Reset", command=self.reset)
        reset_button.pack()

        exit_button = tk.Button(control_frame, text="Iesire", command=self.root.quit)
        exit_button.pack()

    def randomize(self):
        self.data = [random.randint(10, self.height - 10) for _ in range(self.num_elements)]
        self.is_sorted = False
        self.update_canvas()

    def start_sorting(self):
        algorithm = self.algorithm_var.get()
        if algorithm == "Bubble Sort":
            self.bubble_sort()
        elif algorithm == "Insertion Sort":
            self.insertion_sort()
        elif algorithm == "Selection Sort":
            self.selection_sort()
        elif algorithm == "Bogo Sort":
            self.bogo_sort()

    def pause_sorting(self):
        self.is_paused = not self.is_paused

    def reset(self):
        self.data = [random.randint(10, self.height - 10) for _ in range(self.num_elements)]
        self.is_sorted = False
        self.is_paused = False
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        bar_width = self.width // len(self.data)
        for i, value in enumerate(self.data):
            color = "green"
            if self.is_sorted and i == len(self.data) - 1:
                color = "red"
            self.canvas.create_rectangle(i * bar_width, self.height - value, (i + 1) * bar_width, self.height,
                                         fill=color)
        self.root.update()

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            if self.is_paused: break
            for j in range(0, n - i - 1):
                if self.is_paused: break
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.update_canvas()
                    time.sleep(self.speed_var.get())

        self.is_sorted = True

    def insertion_sort(self):
        n = len(self.data)
        for i in range(1, n):
            if self.is_paused: break
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
            self.update_canvas()
            time.sleep(self.speed_var.get())

        self.is_sorted = True

    def selection_sort(self):
        n = len(self.data)
        for i in range(n):
            if self.is_paused: break
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.update_canvas()
            time.sleep(self.speed_var.get())

        self.is_sorted = True

    def bogo_sort(self):
        while not self.is_sorted:
            if self.is_paused: break
            random.shuffle(self.data)
            self.update_canvas()
            time.sleep(self.speed_var.get())
            if self.is_sorted():
                self.is_sorted = True

    def is_sorted(self):
        return all(self.data[i] <= self.data[i + 1] for i in range(len(self.data) - 1))


if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizer(root)
    root.mainloop()
