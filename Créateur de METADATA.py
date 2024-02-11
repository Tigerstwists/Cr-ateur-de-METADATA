import os
import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, messagebox


class Enterbackground(simpledialog.Dialog):
    def body(self, master):
        self.title("Entrez le nombre de background")
        self.iconbitmap('C:\\Users\\johssua\\Desktop\\testjava\\python\\logo.ico')
        self.label = ttk.Label(master, text="Nombre de background :")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(master)
        self.entry.pack()

        return self.entry  # initial focus

    def apply(self):
        self.result = self.entry.get()
        if self.result == '':  # L'utilisateur a entré une valeur nulle
            self.parent.quit()  # Fermer la boîte de dialogue

class background(simpledialog.Dialog):
    def body(self, master):
        self.title("Entrez background")
        self.iconbitmap('C:\\Users\\johssua\\Desktop\\testjava\\python\\logo.ico')
        self.label = ttk.Label(master, text="Entrez background :")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(master)
        self.entry.pack()

        return self.entry  # initial focus

    def apply(self):
        self.result = self.entry.get()
        if self.result == '':  # L'utilisateur a entré une valeur nulle
            self.parent.quit()  # Fermer la boîte de dialogue


class EnterBPM(simpledialog.Dialog):
    def body(self, master):
        self.title("Entrez nombre de BPM et Offset")
        self.iconbitmap('C:\\Users\\johssua\\Desktop\\testjava\\python\\logo.ico')
        self.label = ttk.Label(master, text="Entrez le nombre de BPM et Offest :")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(master)
        self.entry.pack()

        return self.entry  # initial focus

    def apply(self):
        self.result = self.entry.get()
        if self.result == '':  # L'utilisateur a entré une valeur nulle
            self.parent.quit()  # Fermer la boîte de dialogue


class BPM(simpledialog.Dialog):
    def body(self, master):
        self.title("Entrez BPM")
        self.iconbitmap('C:\\Users\\johssua\\Desktop\\testjava\\python\\logo.ico')
        self.label = ttk.Label(master, text="Entrez BPM :")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(master)
        self.entry.pack()

        return self.entry  # initial focus

    def apply(self):
        self.result = self.entry.get()
        if self.result == '':  # L'utilisateur a entré une valeur nulle
            self.parent.quit()  # Fermer la boîte de dialogue


class Offset(simpledialog.Dialog):
    def body(self, master):
        self.title("Entrez Offset")
        self.iconbitmap('C:\\Users\\johssua\\Desktop\\testjava\\python\\logo.ico')
        self.label = ttk.Label(master, text="Entrez Offset :")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(master)
        self.entry.pack()

        return self.entry  # initial focus

    def apply(self):
        self.result = self.entry.get()
        if self.result == '':  # L'utilisateur a entré une valeur nulle
            self.parent.quit()  # Fermer la boîte de dialogue 


def create_file():
    # Ouvrir une boîte de dialogue pour choisir le fichier à enregistrer
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], initialfile="METADATA.txt")
    if not file_path:
        return  # L'utilisateur a annulé la boîte de dialogue

    # Ouvrir le fichier en mode écriture
    with open(file_path, "w", encoding="utf-8") as fichier:
        fichier.write("[METADATA]\n")
        fichier.write("Artist: " + nom_artiste.get() + "\n")
        fichier.write("Artist romanised: " + nom_artiste_romanise.get() + "\n")
        fichier.write("Title: " + nom_titre.get() + "\n")
        fichier.write("Title romanised: " + nom_titre_romanised.get() + "\n")
        fichier.write("Tags: " + nom_tags.get() + "\n")
        fichier.write("Audio: " + nom_audio.get() + "\n")

        # Demander le nombre de fois à l'utilisateur pour Background
        dialog = Enterbackground(fenetre)
        n = dialog.result
        if n is None:  # L'utilisateur a annulé la boîte de dialogue
            fichier.close()  # Fermer le fichier
            os.remove(file_path)  # Supprimer le fichier
            fenetre.quit()  # Fermer la fenêtre
            return
        for i in range(int(n)):
            fenetre.update()  # Mettre à jour la fenêtre pour fermer la boîte de dialogue précédente
            dialog = background(fenetre)
            Background = dialog.result
            if Background is None:  # L'utilisateur a annulé la boîte de dialogue
                fichier.close()  # Fermer le fichier
                os.remove(file_path)  # Supprimer le fichier
                fenetre.quit()  # Fermer la fenêtre
                return
            fichier.write("Background: " + Background + "\n")

        fichier.write("\n")
        fichier.write("[TIMING]\n")

        # Demander le nombre de fois à l'utilisateur pour BPM et Offset
        dialog = EnterBPM(fenetre)
        s = dialog.result
        if s is None:  # L'utilisateur a annulé la boîte de dialogue
            fichier.close()  # Fermer le fichier
            os.remove(file_path)  # Supprimer le fichier
            fenetre.quit()  # Fermer la fenêtre
            return
        for i in range(int(s)):
            fenetre.update()  # Mettre à jour la fenêtre pour fermer la boîte de dialogue précédente
            dialog = BPM(fenetre)
            bpm = dialog.result
            if bpm is None:  # L'utilisateur a annulé la boîte de dialogue  
                fichier.close()  # Fermer le fichier
                os.remove(file_path)  # Supprimer le fichier
                fenetre.quit()  # Fermer la fenêtre
                return
            dialog = Offset(fenetre)
            offset = dialog.result
            if offset is None:  # L'utilisateur a annulé la boîte de dialogue
                fichier.close()  # Fermer le fichier
                os.remove(file_path)  # Supprimer le fichier
                fenetre.quit()  # Fermer la fenêtre
                return
            fichier.write("BPM: " + bpm + "," + " Offset: " + offset + "\n")

    # Afficher un message de confirmation
    messagebox.showinfo("Succès", "Votre fichier a été créé avec succès")

# Créer une fenêtre tkinter
fenetre = tk.Tk()
fenetre.iconbitmap('C:\\Users\\johssua\\Desktop\\testjava\\python\\logo.ico')
fenetre.title("Créateur de METADATA")
fenetre.geometry("800x600")  # Largeur de 800 pixels et hauteur de 600 pixels

style = ttk.Style()
style.configure("TButton", font=("Arial", 20), background="blue")
style.configure("TEntry", font=("Arial", 15), fieldbackground="lightgray")
style.configure("TLabel", font=("Arial", 15), background="lightgray")

# Créer des champs de texte pour chaque entrée avec des labels correspondants
ttk.Label(fenetre, text="Nom de l'artiste").pack(pady=10)
nom_artiste = ttk.Entry(fenetre)
nom_artiste.pack()

ttk.Label(fenetre, text="Nom de l'artiste romanisé").pack(pady=10)
nom_artiste_romanise = ttk.Entry(fenetre)
nom_artiste_romanise.pack()

ttk.Label(fenetre, text="Titre").pack(pady=10)
nom_titre = ttk.Entry(fenetre)
nom_titre.pack()

ttk.Label(fenetre, text="Titre romanisé").pack(pady=10)
nom_titre_romanised = ttk.Entry(fenetre)
nom_titre_romanised.pack()

ttk.Label(fenetre, text="Tags").pack(pady=10)
nom_tags = ttk.Entry(fenetre)
nom_tags.pack()

ttk.Label(fenetre, text="Audio").pack(pady=10)
nom_audio = ttk.Entry(fenetre)
nom_audio.pack()

# Créer un bouton pour exécuter le script
bouton = ttk.Button(fenetre, text="Créer le fichier", command=create_file)
bouton.pack(pady=20)

fenetre.mainloop()
