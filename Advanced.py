# importation des modules
from tkinter import *
import turtle as t


class Advanced:
    """
    Initialisation de la fonction, cette initialisation contient l'appel des fonctions et
    l'initialisation des elements de base dans une fenetre tkinter, comme le nom ou le logo
    """
    def __init__(self):
        self.window = Tk()
        self.window.title("Application")
        self.window.iconbitmap("images/logo.ico")
        self.window.resizable(False, False)
        self.bg = "#50E3C2"

        self.manager()
        self.appearance()

        self.window.mainloop()

    """Fonction manager qui permet une meilleur organisation du programme a travers des frames"""
    def manager(self):
        self.global_frame = Frame(self.window, background=self.bg)
        self.window.config(background=self.bg)
        canvas = Canvas(self.global_frame, width=375, height=370)
        self.draw = t.RawTurtle(canvas)
        canvas.grid(row=0, column=1)

    """Fonction appearance qui stock tout les Label les entry et les menus, ameliorant l'IHM"""
    def appearance(self):
        self.frame = Frame(self.global_frame, bg=self.bg)

        Label(self.frame, text="Cotées :", fg="black", background=self.bg).grid(row=0, column=0)
        Label(self.frame, text="Longueur :", fg="black", background=self.bg).grid(row=1, column=0)
        Label(self.frame, text="Couleur :", fg="black", background=self.bg).grid(row=2, column=0)
        Label(self.frame, text="Epaisseur :", fg="black", background=self.bg).grid(row=3, column=0)

        self.cote = Entry(self.frame)
        self.longueur = Entry(self.frame)
        self.couleur = Entry(self.frame)
        self.epaisseur = Entry(self.frame)

        self.cote.grid(row=0, column=1)
        self.longueur.grid(row=1, column=1)
        self.couleur.grid(row=2, column=1)
        self.epaisseur.grid(row=3, column=1)

        Button(self.frame, text="Valider", command=self.config).grid(row=5, column=0, columnspan=2)
        self.frame.grid(row=0, column=0)
        self.global_frame.grid(row=0, column=1)

    """Fonction polygon recursive qui permet de tracer n'importe quel polygone régulier"""
    def polygone(self, longueur, angle, cote):
        if cote > 0:
            self.draw.forward(longueur)
            self.draw.right(angle)
            self.polygone(longueur, angle, cote - 1)
        self.draw.ht()

    """Fonction config qui permet un meilleur affichage de la tortue, regle la position,
    la vitesse, puis trace le polygone"""
    def config(self):
        color = [self.couleur.get(), "black"][self.couleur.get() == ""]
        self.draw.penup()
        self.draw.goto(0, 150)
        self.draw.pendown()
        self.draw.clear()
        self.draw.speed(10)
        self.draw.width(self.epaisseur.get())
        self.draw.color(color)
        self.polygone(int(self.longueur.get()), 360 / int(self.cote.get()), int(self.cote.get()))
        text = Label(self.window, text='La figure possede '+ self.cote.get() + " cotées "+ self.couleur.get() +" et un angle de "+ str(360 / int(self.cote.get())) + " degres", bg=self.bg)
        text.grid(row=1, column=1)
