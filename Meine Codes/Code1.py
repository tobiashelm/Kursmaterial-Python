#While Schleife


# x = 0
# while x < 10:
#     print("Hallo Welt")
#     if x == 5:
#         break
#     x+= 1  


import datetime
import random
#login 


#1. Usereingaben in variablen speichern (username,password)
input_try = 0
while input_try < 3:  
    username = input("Gebe den Usernamen ein\n").lower()
    password = input("Gebe das Passwort ein\n").lower()
    input_try += 1
    if input_try == 3:
        print("Drei fehlerhafte Eingaben, beende Programm!")
    if username == "root" and password == "admin":

        print(f"""
            ********Willkommen {username}********
            #1. Zeige Systemwerte
            #2. Zeige Uhrzeit an t
            #3. Lasse eine Zufallszahl generieren
            #4. Exit
            """)
        user_option = input("Wähle eine entsprechende Option aus! [1|2|3|4]")
        if user_option == "1":
            print("""
                ABC: ...
                ABC:...
                
                """)
            break
        elif user_option == "2":
            now = datetime.datetime.now()
            print(str(now.time()))
            break
        elif user_option == "3":
            pseudo_random_number = random.randrange(1,10)
            print(pseudo_random_number)
            break
        else:
            print("CYA!")
            break
    else:
        print("Falsche Eingabe, Bitte Username und/oder Password richtig eingeben!")
    

print("Programm beendet!")


  match auswahl:
    case 1: print("\nSystemwerte") print(f"Benutzer: {user}") case 2: print("\nAktuelle Uhrzeit:") print(datetime.now()) case 3: zufallszahl = random.randint(1, 100) print(f"\nZufallszahl: {zufallszahl}") case 4: print("\nProgramm wird beendet.") case _: print("\nUngültige Eingabe!")else:  