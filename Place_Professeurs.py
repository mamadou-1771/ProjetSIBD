from tkinter import *
from tkinter.messagebox import showerror, showinfo

from prof2 import listeInscrit


class Personnage():
    def __init__(self, prenom, nom, id, grade):
        self.prenom = prenom
        self.nom = nom
        self.id = id
        self.grade = grade

    def __eq__(self, other):
        return (self.id == other.id)


def appartient(Liste, val):
    for i in range(len(Liste)):
        if Liste[i].__eq__(val):
            return 1
    return 0


def valider():
    global listePersonne
    if prenomEntre.get() and nomEntre.get() and idEntre.get() and gradeEntre.get():
        pn = Personnage(prenomEntre.get(), nomEntre.get(), idEntre.get(), gradeEntre.get())
        if appartient(listePersonne, pn):
            showerror(title="Formulaire invalide", message="Cette utilisateur existe deja!")
        else:
            listePersonne.append(pn)
            showinfo(title="Validation reussie", message="{} a bien ete ajouter".format(prenomEntre.get()))

    else:
        showerror(title="Formulaire invalide", message="Toutes les champs doivent etre renseigner")


def reinitialiser():
    prenomEntre.delete(0, END)
    nomEntre.delete(0, END)
    idEntre.delete(0, END)
    gradeEntre.delete(0, END)


listePersonne = []

fen = Tk()
fen.geometry("300x320+300+150")
fen.title("Page d'inscription")

contenu = Canvas(fen, bg="#FF7801")
fontLabel = 'arial 13 bold'
fontEntre = 'arial 11 bold'

prenom = Label(contenu, text="Prenom :", font=fontLabel, fg='white', bg="#FF7801")
nom = Label(contenu, text="Nom :", font=fontLabel, fg='white', bg="#FF7801")
id = Label(contenu, text="ID :", font=fontLabel, fg='white', bg="#FF7801")
grade = Label(contenu, text="Grade :", font=fontLabel, fg='white', bg="#FF7801")
validation = Label(contenu, text="Veuillez entrez vos informations ici :", font=fontLabel, fg="#FF7801", bg='white')

prenomEntre = Entry(contenu, font=fontEntre)
nomEntre = Entry(contenu, font=fontEntre)
idEntre = Entry(contenu, font=fontEntre)
gradeEntre = Entry(contenu, font=fontEntre)

validation.grid(row=0, column=0, columnspan=2)
prenom.grid(row=1, column=0, sticky=E, padx=5, pady=5)
nom.grid(row=2, column=0, sticky=E, padx=5, pady=5)
id.grid(row=3, column=0, sticky=E, padx=5, pady=5)
grade.grid(row=4, column=0, sticky=E, padx=5, pady=5)

prenomEntre.grid(row=1, column=1, padx=5, pady=5)
nomEntre.grid(row=2, column=1, padx=5, pady=5)
idEntre.grid(row=3, column=1, padx=5, pady=5)
gradeEntre.grid(row=4, column=1, padx=5, pady=5)

b1 = Button(fen, text="Valider", command=valider, width=10, fg='white', bg="#FF7801")
b2 = Button(fen, text="Reinitialiser", command=reinitialiser, width=10, fg='white', bg="#FF7801")
b3 = Button(fen, text="Voir la liste", command=lambda: listeInscrit(fen, listePersonne), width=10, fg='white',bg="#FF7801")

b1.grid(row=5, column=0, pady=5)
b2.grid(row=6, column=0, pady=5)
b3.grid(row=7, column=0, pady=5)

contenu.grid(row=0, column=0, padx=5, pady=5)


def listeInscrit(fenetre,Liste):
    newFen = Toplevel(fenetre)
    newFen.geometry("350x400+350+150")
    newFen.title("Liste des Professseurs inscrits")

    listeCan = Canvas(newFen,bg="#FF7801")
    fontLabel = 'arial 11 bold'

    resultat = Label(listeCan,text="Liste des gens inscrits",font=fontLabel,fg="#FF7801",bg='white')
    prenom = Label(listeCan,text="Prenom",width=30,font=fontLabel,fg='white',bg="#FF7801")
    nom = Label(listeCan, text="Nom",width=25, font=fontLabel, fg='white',bg="#FF7801")
    id = Label(listeCan, text="ID",width=20, font=fontLabel, fg='white',bg="#FF7801")
    grade = Label(listeCan, text="Grade",width=15, font=fontLabel,fg='white',bg="#FF7801")
    status = Label(listeCan, text="Aucun inscrit pour le moment", font='arial  ',fg='white',bg="#FF7801")

    listeCan.grid(row=0,column=0)
    resultat.grid(row=0, column=0,columnspan=4)
    prenom.grid(row=1, column=1,padx=5,pady=5)
    nom.grid(row=1, column=2,padx=5,pady=5)
    id.grid(row=1, column=3,padx=5,pady=5)
    grade.grid(row=1, column=4,padx=5,pady=5)
    status.grid(row=2, column=0,columnspan=4)

    if Liste:
        r=2
        for p in Liste:
            prenom = Label(listeCan, text=p.prenom, font=fontLabel, fg='white', bg="#FF7801")
            nom = Label(listeCan, text=p.nom, font=fontLabel, fg='white', bg="#FF7801")
            id = Label(listeCan, text=p.id, font=fontLabel, fg='white', bg="#FF7801")
            grade = Label(listeCan, text=p.grade, font=fontLabel, fg='white', bg="#FF7801")

            prenom.grid(row = r, column = 1)
            nom.grid(row = r, column = 2)
            id.grid(row = r, column = 3)
            grade.grid(row = r, column = 4)
            listeCan.create_line(10,50,350,50,width=1,fill='white')

            r=r+1

            status.configure(text="{} Professeurs(s) inscrit pour le moment".format(len(Liste)))
            status.grid(row=r,column =0,columnspan=4,pady=2)

    newFen.mainloop()


fen.mainloop()

