# -*- coding: utf-8 -*-

def ricorsione(clues, diz, citta, segreto = '', segreti = set()):                                                 #Funzione ricorsiva che trova i segreti
    if clues == []:                                                                                               #Caso base: gli indizi sono finiti
        return segreti.add((segreto.rstrip(), citta))
    if (citta,clues[0]) in diz:                                                                                   #Caso ricorsivo
        for indizi in diz[(citta,clues[0])]:                                                                      
            ricorsione(clues[1:], diz, indizi[0], segreto + indizi[1] + ' ')
    return segreti

def dividi_istruzioni(string):                                                                                    #Funzione che prende una stringa di istruzioni del tipo CITTAindizioDESTINAZIONEsegreto
    start = 0
    parti = []
    for i in range(len(string)-1):                                                                                #Parte il ciclo sulla stringa
        if (string[i].isupper() and string[i+1].islower()) or (string[i].islower() and string[i+1].isupper()):    #Appena trova il cambio da MAIUSCOLO (isupper()) a minuscolo (islower()) splitta l'istruzione in [CITTA,indizio,DESTINAZIONE,segreto] e la trasforma in due tuple (CITTA,indizio) e (DESTINAZIONE,segreto)
            parti.append(string[start: i+1])
            start = i+1
    parti.append(string[start:])
    return tuple(parti[:2]), tuple(parti[2:])                                                                     #Ritorna le tuple da inserire nel dizionario della funzione pulisci_file.

def pulisci_file(istructions_file):                                                                               #Funzione che analizza il file in ingresso
    f_in = open(istructions_file, encoding="utf8")
    diz = dict()
    for riga in (l.strip().split() for l in f_in if not l.startswith('#')):                                       #Un ciclo che se la riga non è vuota o inizia con il # (line.startswith('#')) appende le istruzioni trovate in un dizionario
        for istruzioni in riga:
            citta_indizio, destinazione_segreto = dividi_istruzioni(istruzioni)                                   #Chiamata alla funzione: dividi istruzioni(stringa)
            diz[citta_indizio] = diz.get((citta_indizio),[]) + [destinazione_segreto]
    return diz                                                                                                    #Restituisce il dizionario del tipo {(CITTA, indizio):(destinazione1,segreto1),(destinazione2,segreto2), (CITTA2,INDIZIO2):(...,...) ecc.}

def ex1(istructions_file, initial_city, clues):                                                                   #Funzione chiamata dal richiedente
    clues = clues.split()
    return ricorsione(clues, pulisci_file(istructions_file), initial_city) if clues != [] else set()

#Parte usata per debuggare il codice senza dover eseguire lo script di test
if __name__ == '__main__':
    print(ex1('esempio.txt', 'ROMA', 'la    bocca                sollevò dal fiero               pasto'))