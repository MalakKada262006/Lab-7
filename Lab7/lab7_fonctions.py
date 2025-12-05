
def saluer():
    print("Bonjour depuis une fonction !")
    print("Ravi de te voir")

saluer()
saluer() 
def bonjour(prenom):
    print(f"Salut {prenom} !")

bonjour("Alice")
bonjour("Mohamed")
def presentation(nom, age):
  print(f"Je m'appelle {nom} et j'ai {age} ans")

presentation("Alice", 20)
presentation("Mohamed", 26)
presentation("Sofia", 19)
def additionner(a, b):
    total = a + b
    return total

resultat = additionner(3, 5)
print("Résultat :", resultat)
print("Type :", type(resultat))
def afficher_message(message, prefix="[INFO]"):
    print(f"{prefix} {message}")
afficher_message("message")
afficher_message("Erreur", prefix="[ERREUR]")
def produit(*args):
    total = 1
    for valeur in args:
        total *= valeur
    return total
print(produit())           
print(produit(1, 2))       
print(produit(1, 2, 3, 4))  
def test_locale():
    message = "Je suis locale"
    print(message)

test_locale()
compteur = 0

def incrementer():
    global compteur
    compteur += 1

incrementer()
incrementer()
print(compteur)
compteur = 0

def incrementer(valeur):
    return valeur + 1

compteur = incrementer(compteur)
print(compteur) 
def moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)
def appliquer_bonus(notes, bonus=1):
    return [min(note + bonus, 20) for note in notes]
def filtrer_notes(notes, seuil):
    return [note for note in notes if note >= seuil]
def rapport(notes, bonus=1, seuil=12, titre="Rapport des notes"):
    notes_bonus = appliquer_bonus(notes, bonus)
    notes_valides = filtrer_notes(notes, seuil)

    lignes = [
        f"=== {titre} ===",
        f"Notes originales : {notes}",
        f"Notes bonus (+{bonus}) : {notes_bonus}",
        f"Moyenne initiale : {moyenne(notes):.2f}",
        f"Moyenne bonus : {moyenne(notes_bonus):.2f}",
        f"Notes ≥ {seuil} : {notes_valides} (total {len(notes_valides)})"
    ]
    return "\n".join(lignes)
if __name__ == "__main__":
    notes = [12, 9, 15, 8, 17, 13, 19, 10]
    print(rapport(notes))
    print(rapport(notes, bonus=2, seuil=14, titre="Rapport avancé"))

def moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)

def appliquer_bonus(notes, bonus=1):
    return [min(note + bonus, 20) for note in notes]

def filtrer_notes(notes, seuil):
    return [note for note in notes if note >= seuil]

def rapport(notes, bonus=1, seuil=12, titre="Rapport des notes"):
    notes_bonus = appliquer_bonus(notes, bonus)
    notes_valides = filtrer_notes(notes, seuil)

    lignes = [
        f"=== {titre} ===",
        f"Notes originales : {notes}",
        f"Notes bonus (+{bonus}) : {notes_bonus}",
        f"Moyenne initiale : {moyenne(notes):.2f}",
        f"Moyenne bonus : {moyenne(notes_bonus):.2f}",
        f"Notes ≥ {seuil} : {notes_valides} (total {len(notes_valides)})"
    ]
    return "\n".join(lignes)

if __name__ == "__main__":
    notes = [12, 9, 15, 8, 17, 13, 19, 10]
    print(rapport(notes))
    print()
    print(rapport(notes, bonus=2, seuil=14, titre="Rapport avancé"))
