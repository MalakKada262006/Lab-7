def moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)

def appliquer_bonus(notes, bonus=1):
    return [min(note + bonus, 20) for note in notes]

def filtrer_notes(notes, seuil):
    return [note for note in notes if note >= seuil]

def min_max(notes):
    if not notes:
        return (0, 0)
    return (min(notes), max(notes))

def normaliser(notes, sur=20):
    if not notes:
        return []
    maximum = max(notes)
    return [note * sur / maximum for note in notes]

def rapport(notes, bonus=1, seuil=12, titre="Rapport des notes"):
    notes_bonus = appliquer_bonus(notes, bonus)
    notes_valides = filtrer_notes(notes, seuil)
    min_note, max_note = min_max(notes)
    notes_norm = normaliser(notes, sur=20)

    lignes = [
        f"=== {titre} ===",
        f"Notes originales : {notes}",
        f"Notes normalisées sur 20 : {notes_norm}",
        f"Notes bonus (+{bonus}) : {notes_bonus}",
        f"Moyenne initiale : {moyenne(notes):.2f}",
        f"Moyenne bonus : {moyenne(notes_bonus):.2f}",
        f"Notes ≥ {seuil} : {notes_valides} (total {len(notes_valides)})",
        f"Min : {min_note}, Max : {max_note}"
    ]
    return "\n".join(lignes)

if __name__ == "__main__":
    notes = [12, 9, 15, 8, 17, 13, 19, 10, 100] 
    rapport_txt = rapport(notes, bonus=2, seuil=14, titre="Rapport enrichi")
    print(rapport_txt)
    with open("rapport_notes.txt", "w", encoding="utf-8") as f:
        f.write(rapport_txt)