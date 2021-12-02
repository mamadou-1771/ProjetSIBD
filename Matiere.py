from tkinter import *
from tkinter.messagebox import showerror, showinfo

from matiere2 import listeMatiere


class Matiere():
    def __init__(self,code_matiere,libelle_matiere,coef_matiere):
        self.code_matiere = code_matiere
        self.libelle_matiere = libelle_matiere
        self.coef_matiere = coef_matiere


def appartient(Liste,val):
    for i in range(len(Liste)):
        if Liste[i].__eq__(val):
            return 1
    return 0

def valider():
    global listeMat
    if code_matiereEntre.get() and libelle_matiereEntre.get() and coef_matiereEntre.get():
        pn = Matiere(code_matiereEntre.get(),libelle_matiereEntre.get(),coef_matiereEntre.get())
        if appartient(listeMat,pn):
            showerror(title="Formulaire invalide",message="Cette matiere existe deja!")
        else:
            listeMat.append(pn)
            showinfo(title="Validation reussie",message="{} a bien ete ajouter".format(libelle_matiereEntre.get()))

    else:
        showerror(title="Formulaire invalide",message="Toutes les champs doivent etre renseigner")

def reinitialiser():

    code_matiereEntre.delete(0,END)
    libelle_matiereEntre.delete(0,END)
    coef_matiereEntre.delete(0,END)


listeMat = []


fen = Tk()
fen.geometry("300x320+300+150")
fen.title("Page d'inscription")

contenu = Canvas(fen,bg="#FF7801")
fontLabel = 'arial 13 bold'
fontEntre = 'arial 11 bold'

code_matiere = Label(contenu, text="Code matiere :",font = fontLabel, fg='white', bg="#FF7801")
libelle_matiere = Label(contenu, text="Libelle matiere :",font = fontLabel, fg='white', bg="#FF7801")
coef_matiere = Label(contenu, text="Coef  matiere :",font = fontLabel, fg='white', bg="#FF7801")

validation = Label(contenu, text="Veuillez entrez vos informations ici :",font = fontLabel, fg="#FF7801", bg='white')

code_matiereEntre = Entry(contenu, font=fontEntre)
libelle_matiereEntre = Entry(contenu, font=fontEntre)
coef_matiereEntre = Entry(contenu, font=fontEntre)


validation.grid(row=0,column=0,columnspan=2)
code_matiere.grid(row=1,column=0,sticky=E,padx=5,pady=5)
libelle_matiere.grid(row=2,column=0,sticky=E,padx=5,pady=5)
coef_matiere.grid(row=3,column=0,sticky=E,padx=5,pady=5)


code_matiereEntre.grid(row=1,column=1,padx=5,pady=5)
libelle_matiereEntre.grid(row=2,column=1,padx=5,pady=5)
coef_matiereEntre.grid(row=3,column=1,padx=5,pady=5)


b1 = Button(fen,text="Valider",command=valider,width=10,fg='white',bg="#FF7801")
b2 = Button(fen,text="Reinitialiser",command=reinitialiser,width=10,fg='white',bg="#FF7801")
b3 = Button(fen,text="Voir la liste",command=lambda:listeMatiere(fen,listeMat),width=10,fg='white',bg="#FF7801")

b1.grid(row=4,column=0,pady=5)
b2.grid(row=5,column=0,pady=5)
b3.grid(row=6,column=0,pady=5)

contenu.grid(row=0,column=0,padx=5,pady=5)


def listeMatiere(fenetre,Liste):
    newFen = Toplevel(fenetre)
    newFen.geometry("350x400+350+150")
    newFen.title("Liste des Matieres")

    listeCan = Canvas(newFen,bg="#FF7801")
    fontLabel = 'arial 11 bold'

    resultat = Label(listeCan,text="Liste des matiere",font=fontLabel,fg="#FF7801",bg='white')
    code_matiere = Label(listeCan,text="CODE",width=30,font=fontLabel,fg='white',bg="#FF7801")
    libelle_matiere = Label(listeCan, text="LIBELLE",width=25, font=fontLabel, fg='white',bg="#FF7801")
    coef_matiere = Label(listeCan, text="COEFFICIENT",width=20, font=fontLabel, fg='white',bg="#FF7801")
    status = Label(listeCan, text="Aucun inscrit pour le moment", font='arial  ',fg='white',bg="#FF7801")

    listeCan.grid(row=0,column=0)
    resultat.grid(row=0, column=0,columnspan=4)
    code_matiere.grid(row=1, column=1,padx=5,pady=5)
    libelle_matiere.grid(row=1, column=2,padx=5,pady=5)
    coef_matiere.grid(row=1, column=3,padx=5,pady=5)
    status.grid(row=2, column=0,columnspan=4)

    if Liste:
        r=2
        for p in Liste:
            code_matiere = Label(listeCan, text=p.code_matiere, font=fontLabel, fg='white', bg="#FF7801")
            libelle_matiere = Label(listeCan, text=p.libelle_matiere, font=fontLabel, fg='white', bg="#FF7801")
            coef_matiere = Label(listeCan, text=p.coef_matiere, font=fontLabel, fg='white', bg="#FF7801")

            code_matiere.grid(row = r, column = 1)
            libelle_matiere.grid(row = r, column = 2)
            coef_matiere.grid(row = r, column = 3)
            listeCan.create_line(10,50,350,50,width=1,fill='white')

            r=r+1

            status.configure(text="{} Matiere ajoute pour le moment".format(len(Liste)))
            status.grid(row=r,column =0,columnspan=4,pady=2)

    newFen.mainloop()


fen.mainloop()