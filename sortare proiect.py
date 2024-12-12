import tkinter as tk
import random
import time

width = 800
height = 400
bar_width = 40
num_bars = width // bar_width

arr = [random.randint(10, height) for _ in range(num_bars)]

root = tk.Tk()
root.title("Vizualizare Sortare Selection Sort")

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()


def draw_bars(highlight=None):
    canvas.delete("all")
    for i in range(num_bars):
        x1 = i * bar_width
        y1 = height - arr[i]
        x2 = (i + 1) * bar_width
        y2 = height
        color = "black" if highlight and i in highlight else "green"
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)


def selection_sort():
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_bars(highlight=[min_idx, j])
            root.update()
            time.sleep(0.1)
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_bars()
        root.update()


start_button = tk.Button(root, text="Începe Sortarea", command=selection_sort)
start_button.pack()

draw_bars()

root.mainloop()
