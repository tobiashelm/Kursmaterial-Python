import random
from datetime import datetime

# 1. Erstelle 3 feste Benutzerkonten mit einzelnen Variablen
user1_name = "admin"
user1_pw = "1234"
user1_role = "admin"

user2_name = "worker"
user2_pw = "5678"
user2_role = "user"

user3_name = "reader"
user3_pw = "9012"
user3_role = "user"

# Variablen für den Login-Status
login_erfolgreich = False
aktuelle_rolle = ""

# 2. Login-Abfrage
print("--- LOGIN SYSTEM ---")
eingabe_name = input("Benutzername: ")

# Prüfe nacheinander, welcher Benutzer sich einloggt
if eingabe_name == user1_name:
    eingabe_pw = input("Passwort: ")
    if eingabe_pw == user1_pw:
        login_erfolgreich = True
        aktuelle_rolle = user1_role
    else:
        print("Falsches Passwort! Programm wird beendet.")

elif eingabe_name == user2_name:
    eingabe_pw = input("Passwort: ")
    if eingabe_pw == user2_pw:
        login_erfolgreich = True
        aktuelle_rolle = user2_role
    else:
        print("Falsches Passwort! Programm wird beendet.")

elif eingabe_name == user3_name:
    eingabe_pw = input("Passwort: ")
    if eingabe_pw == user3_pw:
        login_erfolgreich = True
        aktuelle_rolle = user3_role
    else:
        print("Falsches Passwort! Programm wird beendet.")

else:
    print("Benutzer nicht gefunden! Programm wird beendet.")

# 3. & 5. Begrüßung nach erfolgreichem Login und Hauptmenü-Schleife
if login_erfolgreich:
    print("\n----------------------------------------")
    if aktuelle_rolle == "admin":
        print("Willkommen Admin! Du hast alle Rechte.")
    else:
        print("Willkommen User! Grundfunktionen verfügbar.")
    print("----------------------------------------")

    # ERSATZ: for-Schleife statt while-Schleife
    # range(3) erlaubt dem Benutzer, das Menü bis zu 3 Mal zu nutzen
    for _ in range(3):
        # Menü anzeigen
        print("\n=== HAUPTMENÜ ===")
        print("[1] Taschenrechner (Addition)")
        print("[2] Taschenrechner (Subtraktion)")
        print("[3] Taschenrechner (Multiplikation)")
        print("[4] Taschenrechner (Division)")
        print("[5] Uhrzeit anzeigen")
        print("[6] Zufallszahl generieren")
        print("[7] Programm beenden")
        
        auswahl = input("Bitte Option wählen (1-7): ")

        # 4. Taschenrechner-Funktionen (Optionen 1-4)
        if auswahl in ["1", "2", "3", "4"]:
            try:
                zahl1 = float(input("Erste Zahl eingeben: "))
                zahl2 = float(input("Zweite Zahl eingeben: "))
                
                if auswahl == "1":
                    ergebnis = zahl1 + zahl2
                    print(f"Ergebnis: {zahl1} + {zahl2} = {ergebnis}")
                elif auswahl == "2":
                    ergebnis = zahl1 - zahl2
                    print(f"Ergebnis: {zahl1} - {zahl2} = {ergebnis}")
                elif auswahl == "3":
                    ergebnis = zahl1 * zahl2
                    print(f"Ergebnis: {zahl1} * {zahl2} = {ergebnis}")
                elif auswahl == "4":
                    # Prüfung auf Division durch 0
                    if zahl2 == 0:
                        print("Division durch 0 nicht erlaubt!")
                    else:
                        ergebnis = zahl1 / zahl2
                        print(f"Ergebnis: {zahl1} / {zahl2} = {ergebnis}")
            except ValueError:
                print("Ungültige Eingabe! Bitte nur Zahlen eingeben.")

        # 7. Uhrzeit anzeigen
        elif auswahl == "5":
            jetzt = datetime.now()
            uhrzeit_string = jetzt.strftime("%H:%M:%S")
            print(f"Aktuelle Uhrzeit: {uhrzeit_string}")

        # 6. Zufallszahl generieren
        elif auswahl == "6":
            zufallszahl = random.randint(1, 100)
            print(f"Deine Zufallszahl ist: {zufallszahl}")

        # Programm beenden
        elif auswahl == "7":
            print("Programm wird beendet. Auf Wiedersehen!")
            break  # bricht die for-Schleife sofort ab
            
        else:
            print("Ungültige Option! Bitte wähle eine Zahl von 1 bis 7.")
    else:
        print("Anzahl Versuche erreicht")
    
