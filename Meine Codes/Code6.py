# 0. eine leere liste
user_liste = []

for i in range(10):
    user_entry = input("Bitte einen Usernamen eingeben (oder 'quit' zum Beenden): ").lower()
    if user_entry == "quit":
        break
    user_liste.append(user_entry)

print("Maximale Anzahl von 10 Usern erreicht!")

# 1. loop damit für die eingabemöglichkeit
# while True:
#     # tip: user_entry = input("...").lower()
#     user_entry = input("Bitte einen Usernamen eingeben (oder 'quit' zum Beenden): ").lower()

#     # 1.a bei eingabe von "quit" oder "quit" oder "quit" wird der loop unterbrochen und danach die bestehende liste mit den usern ausgegeben
#     if user_entry == "quit":
#         break

#     # 2. nach dem eingeben wird der liste der eingegebene user hinzugefügt
#     user_liste.append(user_entry)

#     # optional: falls die liste 10 einträge groß ist (die länge bekommt mit len()) wird das programm beendet und die liste mit den bestehenden usern ausgegeben
#     if len(user_liste) == 10:
#         print("Maximale Anzahl von 10 Usern erreicht!")
#         break

# Ausgabe der Liste nach dem Ende des Loops

print("Hier ist die Liste mit allen hinzugefügten usern:")
print(user_liste)
