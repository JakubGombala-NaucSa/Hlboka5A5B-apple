import tkinter as tk

root = tk.Tk()
root.title("Preteky lopticiek")

platno = tk.Canvas(width=400, height=600, bg="lightblue")
platno.pack()

lopticky = []

a = tk.PhotoImage(file="Apple.png")
def vytvor_lopticky():
    global a
    x = -10
    for i in range(10):
        x += 20
        lopticka = platno.create_image(x, 20, image=a)
        lopticky.append(lopticka)

vytvor_lopticky()
