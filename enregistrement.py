import hashlib
import maskpass
import string

def Introduire_pwd():
    while True:
        p = maskpass.getpass()
        if len(p) == 8:
            if any(c in string.digits for c in p):
                if any(c in string.ascii_uppercase for c in p):
                    if any(c in string.ascii_lowercase for c in p):
                        if any(c in string.punctuation for c in p):
                            p = hashlib.sha256(p.encode()).hexdigest()
                            return p
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
print(colorama.Fore.RED)
print(art.text2art("Cyber"))
print(colorama.Fore.MAGENTA)
print("Enregistrement")

print("\t Email")
print("\t Pwd")

y = Introduire_pwd()

with open('enregistrement.txt', 'w') as f1:
    f1.write(f"Le password haché est : {y}")

with open('enregistrement.txt', 'r') as f1:
    stored_password = f1.readline().strip()
    print(stored_password)

    if stored_password == y:
        print("\nBienvenue : ......")
    else:
        print("Merci de vous enregistrer avant l'authentification")

import re  # Importez le module de correspondance d'expressions régulières

def Introduire_gmail():
    while True:
        email = input("Entrez votre adresse Gmail : ").strip()  # Demandez à l'utilisateur d'entrer son adresse Gmail
        if re.match(r"[a-zA-Z0-9._%+-]+@gmail\.com", email):
            return email  # Si l'adresse correspond au format Gmail, retournez-la
        else:
            print("Adresse Gmail invalide. Veuillez entrer une adresse Gmail valide.")

