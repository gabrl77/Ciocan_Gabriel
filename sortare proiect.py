import tkinter as tk
import random
import time

width = 800
height = 400
bar_width = 50
num_bars = width // bar_width

arr = [random.randint(10, height) for _ in range(num_bars)]

root = tk.Tk()
root.title("Vizualizare Sortare prin Metoda Bulelor")

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()


def draw_bars():
    canvas.delete("all")
    for i in range(num_bars):
        x1 = i * bar_width
        y1 = height - arr[i]
        x2 = (i + 1) * bar_width
        y2 = height
        canvas.create_rectangle(x1, y1, x2, y2, fill="red")


def bubble_sort():
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                draw_bars()
                root.update()
                time.sleep(0.01)


start_button = tk.Button(root, text="Începe Sortarea", command=bubble_sort)
start_button.pack()

draw_bars()

root.mainloop()