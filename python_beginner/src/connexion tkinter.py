import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, parent, on_login):
        super().__init__(parent)
        self.on_login = on_login # fonction qui sera appelée lors d'une connexion réussie

        # Création des widgets de la page de connexion
        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)

        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")

        self.login_button = tk.Button(self, text="Login", command=self.login)

        # Placement des widgets dans la page de connexion
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get() # Récupération du nom d'utilisateur saisi
        password = self.password_entry.get() # Récupération du mot de passe saisi

        if username == "admin" and password == "password":
            self.on_login(username) # Appel de la fonction de connexion réussie avec le nom d'utilisateur en paramètre
        else:
            tk.messagebox.showerror("Error", "Invalid username or password") # Affichage d'une boîte de dialogue d'erreur

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page") # Titre de la fenêtre
        self.geometry("300x200") # Taille de la fenêtre

        self.login_page = LoginPage(self, self.handle_login) # Création de la page de connexion
        self.login_page.pack() # Placement de la page de connexion dans la fenêtre

    def handle_login(self, username):
        tk.messagebox.showinfo("Success", f"Welcome {username}!") # Affichage d'une boîte de dialogue de succès avec le nom d'utilisateur

if __name__ == '__main__':
    app = App()
    app.mainloop() # Lancement de l'application Tkinter
