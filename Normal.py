# importation des modules
import turtle as t
from tkinter import *


class App:
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
        Label(self.frame, text="Figure :", fg="black", background=self.bg).grid(row=2, column=0)
        Label(self.frame, text="Couleur :", fg="black", background=self.bg).grid(row=3, column=0)
        Label(self.frame, text="Epaisseur :", fg="black", background=self.bg).grid(row=4, column=0)

        self.cote = StringVar(value="3")
        self.longueur = StringVar(value="1")
        self.figure = StringVar(value="triangle")
        self.couleur = StringVar(value="black")
        self.epaisseur = StringVar(value="1")

        OptionMenu(self.frame, self.cote, "4", "5", "6", "7", "8", "9", "10", "15", "20", "30", "40", "50", "100",
                   "200", "300", "400", "500", "600", "700", "800", "900", "1000").grid(row=0, column=1)
        OptionMenu(self.frame, self.longueur, "5", "10", "50", "100", "200", "300", "500", "1000").grid(row=1, column=1)
        OptionMenu(self.frame, self.figure, "carré", "pentagone", "hexagone", "heptagone", "octogone", "ennéagone",
                   "décagone", "pentadécagone", "icosagone", "triacontagone", "tétracontagone", "pentacontagone",
                   "hectogone", "dihectogone", "trihectogone", "tétrahectogone", "pentahectogone", "hexahectogone",
                   "heptahectogone", "octahectogone", "ennéahectogone", "Chiliogone").grid(row=2, column=1)
        OptionMenu(self.frame, self.couleur, "red", "yellow", "pink", "purple", "green", "grey", "orange", "blue").grid(
            row=3, column=1)
        OptionMenu(self.frame, self.epaisseur, "2", "3", "4", "5", "6", "7", "8", "9", "10").grid(row=4, column=1)

        self.cote.trace_add("write", self.tracePolygons)
        self.figure.trace_add("write", self.traceNumber)

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
        self.draw.penup()
        self.draw.goto(0, 150)
        self.draw.pendown()
        self.draw.clear()
        self.draw.speed(10)
        self.draw.width(self.epaisseur.get())
        self.draw.color(self.couleur.get())
        self.polygone(int(self.longueur.get()), 360 / int(self.cote.get()), int(self.cote.get()))
        self.text_label = Label(self.window,
                                text="le " + self.figure.get() + " possède " + self.cote.get() + " cotées " + self.couleur.get() + ", \n un angle de " + str(
                                    int(360 / int(
                                        self.cote.get()))) + " degrès et une epaisseur de " + self.epaisseur.get(),
                                fg="red", bg=self.bg)
        self.text_label.grid(row=1, column=1)

    """Fonction qui permet de relier un menu a un dictionnaire, les attributs a,b et c sont
     indispensables mais ne sont pas utilisé dans notre cas"""
    def tracePolygons(self, a, b, c):
        name = {"3": "triangle", "4": "carré", "5": "pentagone", "6": "hexagone", "7": "heptagone", "8": "octogone",
                "9": "ennéagone", "10": "décagone", "15": "pentadécagone", "20": "icosagone", "30": "triacontagone",
                "40": "tétracontagone", "50": "pentacontagone", "100": "hectogone", "200": "dihectogone",
                "300": "trihectogone", "400": "tétrahectogone", "500": "pentahectogone", "600": "hexahectogone",
                "700": "heptahectogone", "800": "octahectogone", "900": "ennéahectogone", "1000": "Chiliogone"}
        self.figure.set(name[self.cote.get()])

    """Fonction qui permet de relier un menu a un dictionnaire, les attributs a,b et c sont
     indispensables mais ne sont pas utilisé dans notre cas"""
    def traceNumber(self, a, b, c):
        names = {"triangle": "3", "carré": "4", "pentagone": "5", "hexagone": "6", "heptagone": "7", "octogone": "8",
                 "ennéagone": "9", "décagone": "10", "pentadécagone": "15", "icosagone": "20", "triacontagone": "30",
                 "tétracontagone": "40", "pentacontagone": "50", "hectogone": "100", "dihectogone": "200",
                 "trihectogone": "300", "tétrahectogone": "400", "pentahectogone": "500", "hexahectogone": "600",
                 "heptahectogone": "700", "octahectogone": "800", "ennéahectogone": "900", "Chiliogone": "1000"}
        self.cote.set(names[self.figure.get()])
