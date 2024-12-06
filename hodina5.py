import tkinter as tk

root = tk.Tk()
root.title("Preteky lopticiek")

platno = tk.Canvas(width=400, height=600, bg="lightblue")
platno.pack()

lopticky = []

def vytvor_lopticky():
    x = -10
    for i in range(10):
        x += 20
        lopticka = platno.create_oval(x, 10, x+20, 30)
        lopticky.append(lopticka)

vytvor_lopticky()
