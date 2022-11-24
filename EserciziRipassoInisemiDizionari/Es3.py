#Lo scambio di messaggi veloci e la possibilità di farlo usando dispositivi portatili ha prodotto
#insieme di abbreviazioni molto comuni, che si rivelano utili nella composizione dei messaggi brevi,
#anche se alcune persone non li comprendono.
# Scrivere un programma che legga un messaggio di testo lungo una sola riga,
# contenente alcune di tali abbreviazioni comuni,
# e lo traduca usando un insieme di traduzioni pre-impostate.

trad = { "qls": "qualcosa","x": "per","ke": "che", "pk": "perché", "msg": "messaggio","qlc": "qualcuno", "tvb": "ti voglio bene",
         "bf": "best friend", "tvtb": "ti voglio tanto bene" }

while True:
    parola = input("Inserisci frase da traduerre\n"
                   "(scegli tra qlc-qls-pk-msg-x-tvb-ke-nn-tvtb-bf):\n")

    for key in trad.keys():
        if parola == key:  # controllo che l'input corrisponda ad una abbreviaziane
            print("Traduzione:", trad[key])
        else:
            print("Non e stata trovata l'abbreviazione.")


