from tkinter import *


def check_entry_value():
    try:

        int(entry_zahl1.get())
        int(entry_zahl2.get())

    except ValueError:
        label_result.config(text='Bitte eine Zahl eingeben')
        return False

    return True


def addieren():
    # Übernahme der Daten aus den Eingabefeldern mit der Funktion get()
    if check_entry_value():
        zahl1 = int(entry_zahl1.get())
        zahl2 = int(entry_zahl2.get())
        # Addiere beide Zahlen
        erg = zahl1 + zahl2
        # erg in label schreiben
        label_result.config(text=str(erg))


def subtrahieren():
    if check_entry_value():
        zahl1 = int(entry_zahl1.get())
        zahl2 = int(entry_zahl2.get())
        erg = zahl1 - zahl2
        label_result.config(text=str(erg))


def multiplizieren():
    if check_entry_value():
        zahl1 = int(entry_zahl1.get())
        zahl2 = int(entry_zahl2.get())
        erg = zahl1 * zahl2
        label_result.config(text=str(erg))


def dividieren():
    if check_entry_value():
        zahl1 = int(entry_zahl1.get())
        zahl2 = int(entry_zahl2.get())
        if zahl2 == 0:
            label_result.config(text='Division durch Null ist nicht erlaubt')
        else:
            erg = zahl1 / zahl2
            label_result.config(text=str(erg))


def clear():
    label_result.config(text='')
    entry_zahl1.delete(0, END)
    entry_zahl2.delete(0, END)


# Erstelle das Hauptfenster
fenster = Tk()
# Titel festlegen
fenster.title("Rechner")
# Größe des Fensters
fenster.geometry("600x400")
label_zahl1 = Label(fenster, text="Zahl1")
label_zahl1.place(x=10, y=10)
# Eingabefelder
entry_zahl1 = Entry(fenster, bg="white")
entry_zahl1.place(x=80, y=10)

label_zahl2 = Label(fenster, text="Zahl2")
label_zahl2.place(x=10, y=40)
entry_zahl2 = Entry(fenster, bg="white")
entry_zahl2.place(x=80, y=40)

label_ergebnis = Label(fenster, text="Ergebnis")
label_ergebnis.place(x=10, y=80)

label_result = Label(fenster, text="")
label_result.place(x=80, y=80)

# Aktionen, Buttons, um Aktionen auslösen zu können
button_plus = Button(fenster, font='20', text="+", command=addieren)
button_plus.place(x=230, y=10, width=20, height=20)

button_minus = Button(fenster, font='20', text='-', command=subtrahieren)
button_minus.place(x=230, y=40, width=20, height=20)

button_multi = Button(fenster, font='20', text='x',  command=multiplizieren)
button_multi.place(x=260, y=10, width=20, height=20)

button_division = Button(fenster, font='20', text='/', command=dividieren)
button_division.place(x=260, y=40, width=20, height=20)

button_clear = Button(fenster, font='20', text='C', command=clear)
button_clear.place(x=290, y=10, width=20, height=20)

fenster.mainloop()
