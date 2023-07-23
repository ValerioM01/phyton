# -*- coding: utf-8 -*-

def ex1(g1, g2, g3, g4, dim_hand, num_letters):
    punteggi = [0,0,0,0]                                                                        #Creo una variabile punteggio una lista che contiene 4 elementi che corrispondono ai 4 punteggi dei giocatori all'inizio della partita
    mano = [dim_hand, dim_hand, dim_hand, dim_hand]                                             #Distribuisco le carte ai 4 creando una lista "mano" che avra come valore "dim_hand"
    num_letters -= dim_hand*4
    valori = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,   #Creo un dizionario che assegna a ogni lettera il proprio punteggio nel gioco
              'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 
              'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 
              'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10}
    lista_di_liste = [g1,g2,g3,g4]
    
    for i in range(4):                                                                          #Faccio partire il conteggio dei punti
        lettere = list(''.join(map(str, lista_di_liste[i])))
        for lettera in lettere:                                                                 #Cosi andranno lette tutte le parole di ogni giocatore che si scomporranno in lettere singole e assegnando punti al giocatore corrispondente.
            punteggi[i] += valori[lettera]
    
    for turno in range(len(g1)):                                                                #Infine eseguo il controllo delle carte nel mazzo e quante carte ha usato il giocatore in quel determinato turno
        
        for giocatore, parole in enumerate(lista_di_liste):
            parola = len(parole[turno])
            mano[giocatore] -= parola
            
            if parola <= num_letters:                                                           #Vengono aggiunte alla mano del giocatore tante carte quanti ne ha usate o quante ne ha a disposizione il mazzo
                mano[giocatore] += parola
                num_letters -= parola
            
            else:
                mano[giocatore]+=num_letters
                num_letters-=num_letters
                if mano[giocatore] == 0:                                                        #In questo caso controllo se in mano del giocatore di turno sono rimaste 0 carte, assegno ad ognuno i punti di penalità e restituisco i valori dei punteggi.
                    for i in range(4):
                        punteggi[i] -= mano[i]*3
                    return punteggi

#Parte usata per debuggare il codice senza dover eseguire lo script di test       
if __name__ == "__main__":
    pass
    dim_hand = 5
    num_letters = 40
    g1 = ['seta','peeks','deter']
    g2 = ['reo','pumas']
    g3 = ['xx','xx']
    g4 = ['frs','bern']
    v = 0
    punteggi_finali= []
    
    def penalita(punteggi, mano, v, punteggi_finali):
        if v < 4:
           punteggi[v] -= mano[v]*3
           v += 1
           punteggi_finali.append(punteggi[v])
           penalita(punteggi[v:], mano[v:], v, punteggi_finali)
        else:
            print(punteggi_finali)
            
    punteggi = [0,0,0,0]
    mano = [dim_hand, dim_hand, dim_hand, dim_hand]
    num_letters -= dim_hand*4
    valori = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1, 
              'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 
              'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 
              'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10}
    lista_di_liste = [g1,g2,g3,g4]
    
    for i in range(4):
        lettere = list(''.join(map(str, lista_di_liste[i])))
        for lettera in lettere:
            punteggi[i] += valori[lettera]
    
    for turno in range(len(g1)):
        
        for giocatore, parole in enumerate(lista_di_liste):
            parola = len(parole[turno])
            mano[giocatore] -= parola
            
            if parola <= num_letters:
                mano[giocatore] += parola
                num_letters -= parola
            
            else:
                mano[giocatore]+=num_letters
                num_letters=0
                if mano[giocatore] == 0:
                    penalita(punteggi, mano, v, punteggi_finali)
