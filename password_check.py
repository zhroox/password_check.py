def check_password(password: str) -> bool:


    if len(password) < 8:
        #prüft die Mindestlänge

        print("Passwort ist zu kurz")
        return False

    has_number = any(char.isdigit() for char in password)
        #prüft, ob Zahlen enthalten sind
    has_letter = any(char.isalpha() for char in password)
        #prüft, ob Buchstaben enthalten sind

    if has_number and has_letter:
        print("Passwort ist ausreichend sicher")
        return True
    
    else:
        print("Passwort sollte Buchstaben und Zahlen enthalten")
        return False


max_attempts = 3
    #maximale Anzahl der Versuche
attempt = 0

while attempt < max_attempts:
    user_input = input("Bitte Passwort eingeben: ")
    if check_password(user_input):
        break

    attempt += 1
    print(f"Versuch {attempt}/{max_attempts} fehlgeschlagen.\n")
        #zeigt dem Benutzer wie viele Versuche schon verbraucht wurden

if attempt == max_attempts:
        #prüft ob der Benutzer alle erlaubten Versuche aufgebraucht hat
    print("Maximale Versuche erreicht. Bitte starten Sie das Programm neu.")