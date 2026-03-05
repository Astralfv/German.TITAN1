import tkinter as tk
from tkinter import ttk
import random
import winsound

# -------- VERBI --------
verbi = {
"essere": ("sein","war","ist gewesen"),
"avere": ("haben","hatte","hat gehabt"),
"diventare": ("werden","wurde","ist geworden"),
"andare": ("gehen","ging","ist gegangen"),
"venire": ("kommen","kam","ist gekommen"),
"fare": ("machen","machte","hat gemacht"),
"dire": ("sagen","sagte","hat gesagt"),
"vedere": ("sehen","sah","hat gesehen"),
"dare": ("geben","gab","hat gegeben"),
"prendere": ("nehmen","nahm","hat genommen"),

"trovare": ("finden","fand","hat gefunden"),
"restare": ("bleiben","blieb","ist geblieben"),
"lasciare": ("lassen","ließ","hat gelassen"),
"iniziare": ("beginnen","begann","hat begonnen"),
"scrivere": ("schreiben","schrieb","hat geschrieben"),
"leggere": ("lesen","las","hat gelesen"),
"mangiare": ("essen","aß","hat gegessen"),
"bere": ("trinken","trank","hat getrunken"),
"parlare": ("sprechen","sprach","hat gesprochen"),
"guidare": ("fahren","fuhr","ist gefahren"),

"dormire": ("schlafen","schlief","hat geschlafen"),
"correre": ("laufen","lief","ist gelaufen"),
"aiutare": ("helfen","half","hat geholfen"),
"chiamare": ("rufen","rief","hat gerufen"),
"portare": ("bringen","brachte","hat gebracht"),
"pensare": ("denken","dachte","hat gedacht"),
"conoscere": ("kennen","kannte","hat gekannt"),
"sapere": ("wissen","wusste","hat gewusst"),
"tenere": ("halten","hielt","hat gehalten"),
"sedersi": ("sitzen","saß","hat gesessen"),

"stare in piedi": ("stehen","stand","hat gestanden"),
"mentire": ("liegen","lag","hat gelegen"),
"arrivare": ("ankommen","kam an","ist angekommen"),
"entrare": ("eintreten","trat ein","ist eingetreten"),
"uscire": ("ausgehen","ging aus","ist ausgegangen"),
"portare via": ("mitnehmen","nahm mit","hat mitgenommen"),
"aprire": ("öffnen","öffnete","hat geöffnet"),
"chiudere": ("schließen","schloss","hat geschlossen"),
"comprare": ("kaufen","kaufte","hat gekauft"),
"vendere": ("verkaufen","verkaufte","hat verkauft"),

"lavorare": ("arbeiten","arbeitete","hat gearbeitet"),
"giocare": ("spielen","spielte","hat gespielt"),
"imparare": ("lernen","lernte","hat gelernt"),
"studiare": ("studieren","studierte","hat studiert"),
"viaggiare": ("reisen","reiste","ist gereist"),
"costruire": ("bauen","baute","hat gebaut"),
"distruggere": ("zerstören","zerstörte","hat zerstört"),
"proteggere": ("schützen","schützte","hat geschützt"),
"creare": ("erschaffen","erschuf","hat erschaffen"),
"mostrare": ("zeigen","zeigte","hat gezeigt")
}
lista = list(verbi.items())
random.shuffle(lista)

indice = 0
punteggio = 0

# -------- FINESTRA --------
root = tk.Tk()
root.title("VerbMaster")
root.geometry("800x600")
root.configure(bg="#111")

# -------- LOGO --------
logo = tk.Label(root,
text="VERB MASTER",
font=("Arial Black",40),
fg="cyan",
bg="#111")

logo.pack(pady=20)

crediti = tk.Label(root,
text="Creato da Astra (Alex)",
font=("Arial",12),
fg="white",
bg="#111")

crediti.pack()

# -------- PROGRESS BAR --------
progress = ttk.Progressbar(root,length=400)
progress.pack(pady=20)

# -------- DOMANDA --------
domanda = tk.Label(root,
text="",
font=("Arial",30),
fg="white",
bg="#111")

domanda.pack(pady=30)

# -------- INPUT --------
entry = tk.Entry(root,
font=("Arial",20),
justify="center")

entry.pack(pady=20)

# -------- FEEDBACK --------
feedback = tk.Label(root,
text="",
font=("Arial",20),
bg="#111")

feedback.pack()

# -------- PUNTEGGIO --------
score_label = tk.Label(root,
text="Punteggio: 0",
font=("Arial",16),
fg="yellow",
bg="#111")

score_label.pack(pady=10)

# -------- FUNZIONI --------
def nuova_domanda():
    global indice

    if indice >= len(lista):
        fine_gioco()
        return

    verbo = lista[indice][0]
    domanda.config(text=verbo)

    progress['value'] = (indice/50)*100

def controlla():
    global indice,punteggio

    risposta = entry.get().lower()
    corretto = lista[indice][1]

    if risposta == corretto:
        feedback.config(text="CORRETTO ✔",fg="lime")
        punteggio +=1
        winsound.Beep(1000,200)
    else:
        feedback.config(text=f"Sbagliato ✖ ( {corretto} )",fg="red")
        winsound.Beep(400,300)

    indice+=1

    score_label.config(text=f"Punteggio: {punteggio}")

    entry.delete(0,tk.END)

    root.after(800,nuova_domanda)

def fine_gioco():

    percentuale = int((punteggio/50)*100)

    domanda.config(text="QUIZ FINITO")
    entry.pack_forget()

    feedback.config(
    text=f"Risposte corrette: {punteggio}/50\nPercentuale: {percentuale}%",
    fg="cyan"
    )

    if percentuale >= 90:
        rank="LEGGENDA"
    elif percentuale >=70:
        rank="PRO"
    elif percentuale >=50:
        rank="STUDENTE"
    else:
        rank="NOVIZIO"

    classifica = tk.Label(root,
    text=f"Classifica: {rank}",
    font=("Arial Black",28),
    fg="gold",
    bg="#111")

    classifica.pack(pady=30)

# -------- BOTTONE --------
btn = tk.Button(root,
text="INVIA",
font=("Arial Black",16),
bg="cyan",
command=controlla)

btn.pack(pady=20)

# -------- START --------
nuova_domanda()

root.mainloop()
