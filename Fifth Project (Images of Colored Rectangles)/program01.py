# -*- coding: utf-8 -*-

import images

def ex1(image_filename, encoded_filename):

    def convertitore(valore):                                                                                                   #Funzione che prende un numero in base 10 che appende in una tupla del tipo (0,0,0) il resto delle divisioni per 256 e se la tupla è minore di tre elementi appende uno 0 cosi da ottenere i valori RGB.
        if valore == 0:
            return (0,0,0)
        cifre = []
        while valore:
            cifre.append(int(valore % 256))
            valore //= 256
        while len(cifre) < 3:
            cifre.append(0)
        return tuple(cifre[::-1])
    
    def ordine(diz_ordine):                                                                                                     #Funzione che prende in input un dizionario dove sono presenti le intersezioni di ciascun rettangolo es {giallo(sta sotto a): rosso verde ecc.}
        for chiave in diz_ordine:
            if len(diz_ordine[chiave]) == 0:                                                                                    #controlla quale rettangolo non ha intersezioni e lo appende in una lista nuova ordinata
                lista_ordinata.append(chiave)
                del diz_ordine[chiave]
                for a in diz_ordine.values():
                    a.discard(chiave)
                if len(diz_ordine) != 0:
                    ordine(diz_ordine)                                                                                          #richiama la funzione stessa rimuovendo però la chiave stessa ed il valore della chiave dalle altre intersezioni per poi cosi trovare il prossimo rettangolo senza intersezioni
                return lista_ordinata                                                                                           #restituire, quando il dizionario sarà vuoto, la lista ordinata.
                
    def immagine_ordinata(lista_ordinata):
        for colori in lista_ordinata:
            [nuova_immagine.append(liste) for liste in rettangoli if liste[-1] == colori]  
        return nuova_immagine.reverse()
    
    def vai_a_destra(riga, x1):                                                                                                 #Funzione che scorre una riga per trovare corrispondenze di altri colori
        while x1 <= m:
            if riga[x1] != colore: 
                diz_ordine[colore].add(riga[x1])
            x1+=1
                        
    def vai_giu(y1, x):                                                                                                         #Funzione che scorre una colonna per trovare corrispondenze di altri colori
        while y1 <= n:
            if immagine[y1][x] != colore:
                diz_ordine[colore].add(immagine[y1][x])
            y1 += 1
    
    def ultima_apparizione(riga, colore):                                                                                       #Funzione che trova l'ultima apparizione di un colore in una riga
        return len(riga) - 1 - riga[::-1].index(colore)
    
    def prendi_colonna_da_matrice(x, matrice):
        return [y[x]for y in matrice]
    
    immagine = images.load(image_filename)                                                                                      #apro l'immagine
                                                                                                                                #Definisco le variabili
    nero = (0,0,0)                                                                                                              #il colore che mi servirà per i controlli
    diz_ordine = {nero:1}                                                                                                       #il dizionario che mi servirà per l'ordinamento
    lista_ordinata = []                                                                                                         #lista dove inserira i colori in ordine
    ymax = 0                                                                                                                    #le lunghezze delle righe dell'immagine data
    xmax = 0
    xmin = 10000000
    ymin = 10000000
    rettangoli = []
    nuova_immagine = []                                                                                                         #la matrice per la nuova immagine da restituire.
    
    for y, riga in enumerate(immagine):                                                                                         #Inizio il ciclo che scorre tutte le righe dell'immagine con enumerate
        controllo = set(riga) - diz_ordine.keys()
        for colore in controllo:                                                                                                #Ciclo che scorre i diversi colori in una riga tranne quelli gia incontrati
            x = riga.index(colore)
            diz_ordine[colore] = set()
            if ymin > y:
                ymin = y
            if xmin > x:
                xmin = x
            m = ultima_apparizione(riga, colore)                                                                                #Prendo grazie alle funzioni le coordinate di ultima apparizione in una riga e in una colonna di quel colore
            n = ultima_apparizione(prendi_colonna_da_matrice(x, immagine), colore)
            vai_a_destra(riga, x+1)                                                                                             #Cosi definisco il perimetro dell'rettangolo cercato
            vai_giu(y, x)                                                                                                       #Seguo quindi il contorno del rettangolo
            vai_giu(y, m)
            vai_a_destra(immagine[n], x+1)
            if ymax < n:
                ymax = n
            if xmax < m:
                xmax = m
            rettangoli.append([convertitore(x), convertitore(y), convertitore(m - x + 1), convertitore(n - y + 1), colore])     #Inserisco il rettangolo trovato nella lista, convertendo le coordinate
    
    del diz_ordine[nero]
    immagine_ordinata(ordine(diz_ordine))                                                                                       #Infine si passa il dizionario completo alla funzione che ordina
    images.save(nuova_immagine, encoded_filename)                                                                               #Avremo la nostra immagine compressa a dovere e la tupla (xmin,ymin,xmax,ymax).
    return (xmin, ymin, xmax, ymax)

#Parte usata per debuggare il codice senza dover eseguire lo script di test
if __name__ == '__main__':    
    
    def convertitore(valore):
        if valore == 0:
            return (0,0,0)
        cifre = []
        while valore:
            cifre.append(int(valore % 256))
            valore //= 256
        while len(cifre) < 3:
            cifre.append(0)
        return tuple(cifre[::-1])
    
    def ordine(diz_ordine):
        for chiave in diz_ordine:
            if len(diz_ordine[chiave]) == 0:
                lista_ordinata.append(chiave)
                del diz_ordine[chiave]
                for a in diz_ordine.values():
                    a.discard(chiave)
                if len(diz_ordine) != 0:
                    ordine(diz_ordine)
                return lista_ordinata
                
    def immagine_ordinata(lista_ordinata):
        for colori in lista_ordinata:
            [nuova_immagine.append(liste) for liste in rettangoli if liste[-1] == colori]
        return nuova_immagine.reverse()
    
    def vai_a_destra(riga, x1):
        while x1 <= m:
            if riga[x1] != colore: 
                diz_ordine[colore].add(riga[x1])
            x1+=1
                        
    def vai_giu(y1, x):
        while y1 <= n:
            if immagine[y1][x] != colore:
                diz_ordine[colore].add(immagine[y1][x])
            y1 += 1
    
    def ultima_apparizione(riga, colore):
        return len(riga) - 1 - riga[::-1].index(colore)
    
    def prendi_colonna_da_matrice(x, matrice):
        return [y[x]for y in matrice]
    
    immagine = images.load('random-40-2399-1913.png')
    nero = (0,0,0)
    diz_ordine = {nero:1}
    lista_ordinata = []
    ymax = 0
    xmax = 0
    xmin = 10000000
    ymin = 10000000
    rettangoli = []
    nuova_immagine = []
    
    for y, riga in enumerate(immagine):
        controllo = set(riga) - diz_ordine.keys()
        for colore in controllo:
            x = riga.index(colore)
            diz_ordine[colore] = set()
            if ymin > y:
                ymin = y
            if xmin > x:
                xmin = x
            m = ultima_apparizione(riga, colore)
            n = ultima_apparizione(prendi_colonna_da_matrice(x, immagine), colore)
            vai_a_destra(riga, x+1)
            vai_giu(y, x)
            vai_giu(y, m)
            vai_a_destra(immagine[n], x+1)
            if ymax < n:
                ymax = n
            if xmax < m:
                xmax = m
            rettangoli.append([convertitore(x), convertitore(y), convertitore(m - x + 1), convertitore(n - y + 1), colore])
    
    del diz_ordine[nero]
    immagine_ordinata(ordine(diz_ordine))    
    images.png.from_array(nuova_immagine, 'RGB').save('foo.png')
    print((xmin, ymin, xmax, ymax))