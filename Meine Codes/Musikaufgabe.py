import random
from datetime import datetime
# AUFGABE: Erweitere das Login-System mit einem einfachen Taschenrechner-Menü
# 
# 1. Erstelle 3 feste Benutzerkonten mit einzelnen Variablen:
#    - user1_name = "admin", user1_pw = "1234", user1_role = "admin"
#    - user2_name = "worker", user2_pw = "5678", user2_role = "user"  
#    - user3_name = "reader", user3_pw = "9012", user3_role = "user"
#
# 2. Login-Abfrage mit folgenden Bedingungen:
#    - Prüfe nacheinander: Ist der Username user1, user2 oder user3?
#    - Wenn ja, prüfe das dazugehörige Passwort
#    - Bei falschem Passwort: "Falsches Passwort! Programm wird beendet"
#    - Wenn Username nicht gefunden: "Benutzer nicht gefunden! Programm wird beendet"
#
# 3. Nach erfolgreichem Login zeige ein Menü mit:
#    [1] Taschenrechner (Addition)
#    [2] Taschenrechner (Subtraktion)
#    [3] Taschenrechner (Multiplikation)
#    [4] Taschenrechner (Division)
#    [5] Uhrzeit anzeigen
#    [6] Zufallszahl generieren
#    [7] Programm beenden
#
# 4. Taschenrechner-Funktionen:
#    - Fordere den User auf, zwei Zahlen einzugeben
#    - Führe die entsprechende Rechenoperation aus
#    - Zeige das Ergebnis an
#    - Bei Division: Prüfe ob der Divisor 0 ist -> "Division durch 0 nicht erlaubt!"
#
# 5. Zusätzliche Bedingungen:
#    - Bei Admin (admin): Zeige "Willkommen Admin! Du hast alle Rechte"
#    - Bei User (worker und reader): Zeige "Willkommen User! Grundfunktionen verfügbar"
#    - Das Programm beendet sich erst bei Option [7]
#
# 6. Zufallszahl:
#    - Generiere eine Zahl zwischen 1 und 100
#    - Zeige: "Deine Zufallszahl ist: [zahl]"
#
# 7. Uhrzeit:
#    - Zeige die aktuelle Uhrzeit im Format: "Aktuelle Uhrzeit: 14:30:25"
#Zusatz:
# Überlege wie man nach jeder Option wieder das Hauptmenü angezeigt bekommt (auch while schleife)
#
# Tipp: Verwende while-Schleifen für das Menü und if-elif-else für die
# Benutzerprüfung und Menüauswahl.
#
# Beispiel für die Benutzerprüfung:
# if username == user1_name:
#     if password == user1_pw:
#         # Login erfolgreich
#     else:
#         # Passwort falsch
# elif username == user2_name:
#     # ...
#
# """
# AUFGABENSTELLUNG: MUSIKLISTE-VERWALTUNG
# Erweitere das vorhandene Login- und Hauptmenü-Programm um zwei neue Funktionen:
# 1. Musikliste anlegen (Option 8): Der Benutzer kann Songs zur Liste hinzufügen.
# 2. Songs aus der Musikliste löschen (Option 9): Der Benutzer kann einen Song 
#    anhand des Namens suchen und löschen.
# -------------------------------------------------------------------------------
# ANFORDERUNGEN FÜR DIE MUSIKLISTE
# -------------------------------------------------------------------------------
# - Erstelle eine LEERE LISTE namens 'music_list' zu Beginn des Programms 
#   (z.B. nach dem Login).
# - Die Liste soll die hinzugefügten Songs speichern.
# -------------------------------------------------------------------------------
# ANFORDERUNGEN FÜR OPTION 8: MUSIKLISTE ANLEGEN (SONGS HINZUFÜGEN)
# -------------------------------------------------------------------------------
# - Implementiere eine SCHLEIFE, die es erlaubt, mehrere Songs hintereinander 
#   einzugeben.
# - Der Benutzer soll zur Eingabe eines Songtitels aufgefordert werden.
# - Wenn der Benutzer "quit" (Groß-/Kleinschreibung egal) eingibt, wird die 
#   Schleife beendet.
#   TIPP: Verwende .lower() für die Eingabe.
# - Nach der Beendigung der Schleife wird die gesamte Musikliste mit allen Songs 
#   ausgegeben.
# - OPTIONAL: Falls die Liste bereits 10 Einträge enthält, wird die Schleife 
#   automatisch beendet und die Liste ausgegeben.
# - Füge den eingegebenen Song (außer "quit") zur Liste hinzu.
#   TIPP: Verwende die append()-Methode.
# -------------------------------------------------------------------------------
# ANFORDERUNGEN FÜR OPTION 9: SONGS AUS DER MUSIKLISTE LÖSCHEN
# -------------------------------------------------------------------------------
# - Der Benutzer wird aufgefordert, den NAMEN EINES SONGS einzugeben, den er 
#   löschen möchte.
# - Das Programm sucht nach diesem Song in der 'music_list'.
#   TIPP: Verwende eine Schleife (for oder while), um die Liste zu durchsuchen.
#   TIPP: Verwende die in- oder remove()-Methode aus den Python Listen-Methoden
#   (z.B. list.remove() oder list.pop()).
# - Wenn der Song gefunden wird, wird er aus der Liste gelöscht und eine 
#   Bestätigung ausgegeben.
# - Wenn der Song NICHT gefunden wird, erscheint eine entsprechende Meldung.
# -------------------------------------------------------------------------------
# HINWEISE ZUR EINBINDUNG
# -------------------------------------------------------------------------------
# - Füge die neuen Optionen [8] Musikliste anlegen und [9] Songs aus Musikliste 
#   löschen in das Hauptmenü ein.
# - Passe die Bereichsüberprüfung (if choice == "1" bis elif choice == "9") und 
#   die else-Meldung entsprechend an.
# - Die music_list muss AUSSERHALB der Hauptschleife definiert werden, damit sie 
#   beim Hinzufügen und Löschen erhalten bleibt.
# -------------------------------------------------------------------------------
# TIPS FÜR DIE UMSETZUNG
# -------------------------------------------------------------------------------
# - Nutze die Dokumentation zu Python Listen und insbesondere die Methoden unter 
#   "List Methods" auf W3Schools.
# - Teste die Funktionen gründlich, besonders das Löschen 
#   (Fallunterscheidungen) und das Beenden der Hinzufüge-Schleife.
# - Verwende für die Song-Eingabe input() und für die Ausgabe print().
# - Die Logik für die neuen Optionen wird in den vorhandenen else-Zweig 
#   (nach choice == "7") eingefügt.
# - Denk daran, die neuen Menüpunkte im Hauptmenü-Text zu ergänzen.
# """
###START
# Variablen für Aufgabe 1
user1_name = "admin"
user1_pw = "1234"
user1_role = "admin"
user2_name = "worker"
user2_pw = "5678"
user2_role = "user"
user3_name = "reader"
user3_pw = "9012"
user3_role = "user"
# login_erfolgreich merkt sich, ob wir das Menü starten dürfen
login_erfolgreich = False
aktuelle_rolle = ""
# Login-Abfrage (Aufgabe 2)
username = input("Bitte Benutzernamen eingeben: ")
music_list = []
if username == user1_name:
    password = input("Bitte Passwort eingeben: ")
    if password == user1_pw:
        login_erfolgreich = True
        aktuelle_rolle = user1_role
    else:
        print("Falsches Passwort! Programm wird beendet")
        
elif username == user2_name:
    password = input("Bitte Passwort eingeben: ")
    if password == user2_pw:
        login_erfolgreich = True
        aktuelle_rolle = user2_role
    else:
        print("Falsches Passwort! Programm wird beendet")
        
elif username == user3_name:
    password = input("Bitte Passwort eingeben: ")
    if password == user3_pw:
        login_erfolgreich = True
        aktuelle_rolle = user3_role
    else:
        print("Falsches Passwort! Programm wird beendet")
        
else:
    print("Benutzer nicht gefunden! Programm wird beendet")
# Aufgabe 5: Willkommensnachricht nach Rolle
if login_erfolgreich == True:
    if aktuelle_rolle == "admin":
        print("Willkommen Admin! Du hast alle Rechte")
    elif aktuelle_rolle == "user":
        print("Willkommen User! Grundfunktionen verfügbar")
    # Zusatz & Aufgabe 3: Das Menü in einer while-Schleife
    while True:
        print("\n--- MENÜ ---")
        print("[1] Taschenrechner (Addition)")
        print("[2] Taschenrechner (Subtraktion)")
        print("[3] Taschenrechner (Multiplikation)")
        print("[4] Taschenrechner (Division)")
        print("[5] Uhrzeit anzeigen")
        print("[6] Zufallszahl generieren")
        print("[7] Programm beenden")
        print("[8] Musikliste anlegen")
        print("[9] Musikliste löschen")
        
        option = input("Wähle eine Option: ")
        
        # Aufgabe 7: Programm beenden
        if option == "7":
            print("Programm beendet.")
            break
            
        # Aufgabe 4: Taschenrechner (Optionen 1-4)
        elif option == "1":
            zahl1 = float(input("Erste Zahl: "))
            zahl2 = float(input("Zweite Zahl: "))
            ergebnis = zahl1 + zahl2
            print("Ergebnis:", ergebnis)
            
        elif option == "2":
            zahl1 = float(input("Erste Zahl: "))
            zahl2 = float(input("Zweite Zahl: "))
            ergebnis = zahl1 - zahl2
            print("Ergebnis:", ergebnis)
            
        elif option == "3":
            zahl1 = float(input("Erste Zahl: "))
            zahl2 = float(input("Zweite Zahl: "))
            ergebnis = zahl1 * zahl2
            print("Ergebnis:", ergebnis)
            
        elif option == "4":
            zahl1 = float(input("Erste Zahl: "))
            zahl2 = float(input("Zweite Zahl: "))
            # Division durch 0 prüfen
            if zahl2 == 0:
                print("Division durch 0 nicht erlaubt!")
            else:
                ergebnis = zahl1 / zahl2
                print("Ergebnis:", ergebnis)
                
        # Aufgabe 7: Uhrzeit anzeigen
        elif option == "5":
            jetzt = datetime.now()
            # Formatiert die Uhrzeit genau wie gefordert: 14:30:25
            print("Aktuelle Uhrzeit:", jetzt.strftime("%H:%M:%S"))
            
        # Aufgabe 6: Zufallszahl generieren
        elif option == "6":
            zahl = random.randint(1, 100)
            print("Deine Zufallszahl ist:", zahl)
        # Aufgabe 8: Musikliste anlegen
        elif option == "8":
            for i in range(10):
                music_title = input("Gib einen Musiktitel ein (mit der Endung .mp3) oder quit zum beenden\n").lower()
                if ".mp3" not in music_title:
                    print("Du hast nicht das korrekte Format ausgewählt!")
                
                elif music_title == "quit":
                    print("Beende Programm")
                    break
        
                else:
                    music_list.append(music_title)
                    print("✅")
                    print(f"{music_list}")
        # Aufgabe 9: Musikliste löschen
        elif option == "9":
            for i in range(10):
                music_title = input("Gib einen Musiktitel ein, den du löschen möchtest oder quit zum beenden\n").lower()
                if music_title == "quit":
                    print("Beende Programm")
                    break
                elif music_title not in music_list: 
                    print("Nicht Teil der Liste")
                    
                else:
                    music_list.remove(music_title)
                    print("❌")
                    print(f"{music_list}")         
        else:
            print("Ungültige Option, bitte neu wählen.")