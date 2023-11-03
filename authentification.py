import hashlib
import string
import getpass

def Introduire_pwd():
    while True:
        p = getpass.getpass("Entrez votre mot de passe : ")
        if len(p) == 8:
            if any(c in string.digits for c in p):
                if any(c in string.ascii_uppercase for c in p):
                    if any(c in string.ascii_lowercase for c in p):
                        if any(c in string.punctuation for c in p):
                            p_hashed = hashlib.sha256(p.encode()).hexdigest()
                            return p_hashed
                        else:
                            print("SVP, au moins un caractère spécial")
                    else:
                        print("SVP, au moins une lettre minuscule")
                else:
                    print("SVP, au moins une lettre majuscule")
            else:
                print("SVP, au moins un chiffre")
        else:
            print("SVP, le mot de passe doit contenir 8 caractères")
import art
import colorama
import re
print(colorama.Fore.RED)
print(art.text2art("Cyber"))
print(colorama.Fore.MAGENTA)
print("Authentification")

# Demander l'adresse Gmail
def Introduire_gmail():
    while True:
        user_email = input("Entrez votre adresse Gmail : ").strip()
        if re.match(r"[a-zA-Z0-9._%+-]+@gmail\.com", user_email):
            return user_email
        else:
            print("Adresse Gmail invalide. Veuillez entrer une adresse Gmail valide.")

def verifier_authentification(email, mot_de_passe_hache):
    with open('enregistrement.txt', 'r') as f1:
        stored_email = None
        stored_password = None
        for line in f1:
            if line.startswith("Email"):
                stored_email = line.split(':')[1].strip()
            elif line.startswith("Le password haché"):
                stored_password = line.split(':')[1].strip()

        if stored_email and stored_password:
            if email == stored_email and mot_de_passe_hache == stored_password:
                print("Bienvenue : ......")
            else:
                print("Mot de passe incorrect")
        else:
            print("Aucun enregistrement trouvé. Merci de vous enregistrer avant l'authentification.")

email = Introduire_gmail()
mot_de_passe_hache = Introduire_pwd()
verifier_authentification(email, mot_de_passe_hache)
