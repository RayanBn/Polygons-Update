from Normal import App
from Advanced import Advanced
from tkinter import *
from PIL import ImageTk, Image


class Menu:
    """
    Initialisation de la fonction, cette initialisation contient l'appel des fonctions et
    l'initialisation des elements de base dans une fenetre tkinter, comme le nom ou le logo
    Cette initialisation va aussi permettre d'afficher le logo en gros sur la fentre pour un meilleur rendu
    """
    def __init__(self):
        self.window = Tk()
        self.window.iconbitmap("images/logo.ico")
        self.window.geometry("380x130")
        self.window.title("(Menu) Application")
        self.window.resizable(False, False)
        self.bg = "#50E3C2"
        self.window.config(background=self.bg)

        self.global_frame = Frame(self.window, bg=self.bg)
        image = ImageTk.PhotoImage(Image.open("images/poligons.jpg"))
        self.canvas = Canvas(self.global_frame, width=200, height=100, bd=0, highlightthickness=0)
        self.canvas.create_image(100, 50, image=image)
        self.canvas.grid(row=0, column=0)

        self.option()
        self.window.mainloop()

    """Fonction Option qui affiche 2 bouton permettant de choir soit le mode avancé, soit normal"""
    def option(self):
        frame = Frame(self.global_frame, bg=self.bg)
        Label(frame, text="Menu", bg=self.bg, font=("", 20), fg="#3C3C3C").pack()
        Button(frame, text="Normal", bg="#93D1C3", width=10, bd=1, command=self.normal).pack()
        Button(frame, text="Avancé", width=10, bd=1, bg="#93D1C3", command=self.advanced).pack()
        frame.grid(row=0, column=1)
        self.global_frame.pack()

    """Fonction qui va lancer le mode normal"""
    def normal(self):
        self.window.destroy()
        App()

    """Fonction qui va lancer le mode avancé"""
    def advanced(self):
        self.window.destroy()
        Advanced()

#Programe Principal
Menu()