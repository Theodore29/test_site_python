import customtkinter
import fonction



customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()
app.title("my app")
app.geometry("400x200")
app.resizable(width=False, height=False)
app.columnconfigure(0, weight=3) 
app.rowconfigure(0, weight=3) 


label_resultat = customtkinter.CTkLabel(app, text="",  wraplength=300)
label_resultat.grid(row=3, column = 0, padx=20, pady = 20)




label = customtkinter.CTkLabel(app, text="Rechercher un nom de ville : ")
label.grid(row=0, column=0)

entry = customtkinter.CTkEntry(app, placeholder_text="Entrez un nom de ville")
entry.grid(row=1, column=0)


def afficher_resultat():
    user_entry=entry.get()
    entry.delete(0,'end')
    resultat = fonction.recherche(user_entry)
    label_resultat.configure(text=resultat)


button = customtkinter.CTkButton(app, text="Rechercher", command=afficher_resultat)
button.grid(row=2, column = 0, padx=20, pady = 20)



app.mainloop()