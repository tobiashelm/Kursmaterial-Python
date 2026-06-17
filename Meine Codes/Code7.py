# 0. eine leere liste
user_liste = []

# 1. loop damit für die eingabemöglichkeit
while True:
    # tip: user_entry = input("...").lower()
    user_entry = input(
        "Bitte einen Usernamen eingeben (oder 'quit' zum Beenden): "
    ).lower()

    # 1.a bei eingabe von "quit" oder "quit" oder "quit" wird der loop unterbrochen und danach die bestehende liste mit den usern ausgegeben
    if user_entry == "quit":
        break

    # NEU: Prüfen, ob der Name schon in der Liste existiert (Doppelte verhindern)
    if user_entry in user_liste:
        print("Dieser User existiert bereits! Bitte einen anderen Namen wählen.")
        continue  # Springt sofort an den Anfang der Schleife für eine neue Eingabe

    # 2. nach dem eingeben wird der liste der eingegebene user hinzugefügt
    user_liste.append(user_entry)


# Ausgabe der Liste nach dem Ende des Loops
print("\nHier ist die Liste mit allen hinzugefügten usern:\n")

# NEU: Die Namen schön untereinander anzeigen mit einer for-Schleife
for user in user_liste:
    print(f"- {user}")
