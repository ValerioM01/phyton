# -*- coding: utf-8 -*-

def ex1(poem_filename):
    def divisori(lunghezza):                                                                                            #definisco la funzione che trova i divisori della lunghezza della lista prosodica 
        lista = []
        [lista.append(i) for i in range(3, lunghezza//2+1) if (lunghezza % i==0)] 
        return lista
    
    def periodo(lista_prosidica):                                                                                       #Funzione che chiamo alla fine del codice per restituire il periodo, prende la lunghezza della lista e trova i suoi divisori da 3 in poi, dato il periodo minimo, e per questi parte un ciclo for (es per 12 fara [3,4,6]), 
                                                                                                                        #crea una slice della lista prosodica da 0 al divisore a cui siamo arrivati e da li un altro for i in range(divisore, lunghezza, divisore) dove il terzo dato fornito vuol dire che saltera ad intervalli del divisore 
                                                                                                                        #e crea ogni volta una lista da confrontare con l'iniziale cercando la corrispondenza biunivoca confrontandoli in un dizionario (es lista1 = [0,1,2,2] lista2 = [4,5,6,6] 0 = 4, 1 = 5, 2 = 6), 
                                                                                                                        #se c'è una corrispondenza per l'intera lunghezza della stringa allora ritorna il divisore a cui siamo senno continua a ciclare nei divisori. 
        lunghezza = len(lista_prosidica)
        num = divisori(lunghezza)
        for j in num:                                                                                                   #ciclo 1 che parte dal periodo minimo = 3 e nel caso non trovi corrispondenza aumenta la lunghezza del periodo
            lista1 = lista_prosidica[0:j]
            for i in range(j, lunghezza, j):                                                                            #ciclo 2 che parte confronta tutti i periodi successivi della stessa lunghezza di lista1
                lista2 = lista_prosidica[i:i+j]
                if confronto(lista1, lista2) == False:
                    break
                elif i+j == lunghezza:
                    return j
        return 1                                                                                                        #se invece è arrivato alla metà senza trovare corrispondenza restituisce 1
    
    def confronto(lista1, lista2):
        diz_mod =dict()
        for indice, elem in enumerate(lista1):                                                                          #cerca la corrispondenza biunivoca confrontandoli in un dizionario
            if elem not in diz_mod and lista2[indice] not in diz_mod.values() or diz_mod.get(elem) == lista2[indice]:   #in queste situazioni elencate crea una corrispondenza
                diz_mod[elem] =  lista2[indice]
            else:
                return False
        return True
                        
    def num_es(riga):                                                                                                   #Dato un verso della poesia for i nella sua lunghezza se incontra una vocale seguita da una consonante aggiunge 1 al numero di es in quella riga e poi lo ritorna
        vocali = ["a","e","i","o","u","j","y"]
        num_es=1
        lunghezza_riga = len(riga)
        for i in range(lunghezza_riga):
            if riga[i] in vocali and i+1 < lunghezza_riga and riga[i+1] not in vocali:
                num_es+=1
        return num_es
    
    def es_fin(riga):                                                                                                   #Inverte il verso della poesia dato (es. ciao, oaic) e aggiunge una lettera alla volta in una variabile es finche non trova una consonante seguita da una vocale e ritorna la variabile ribaltata [::-1]
        vocali = ["a","e","i","o","u","j","y"]
        riga = riga[::-1]
        es = ''
        lunghezza_riga = len(riga)
        for i in range(lunghezza_riga):
            es += riga[i]
            if riga[i] not in vocali and i+1 < lunghezza_riga and riga[i+1] in vocali:
                return es[::-1]
                
    with open(poem_filename, encoding="utf8") as verso:                                                                 #Da qui apro il file, codificandolo in UFT-8 e inserendolo in una variabile chiamata verso grazie al read(), la rendo minuscola con lower()
        verso = verso.read().lower()

    tran = verso.maketrans('àáâãäåèéêëìíîïòóôõöøùúûüýÿ', 'aaaaaaeeeeiiiioooooouuuuyy',                                  #con il metodo tran che crea il dizionario con i corrispettivi delle lettere accentate e translate che le rimuove rendo leggibile la poesia poi con splitlines() creo una lista con i singoli versi dentro.
                           ' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
    verso = verso.translate(tran).splitlines()
    
    lista_lunghezze = []                                                                                                #Definisco le variabili: lista dell'es in ogni riga, lista dell' es finali, lista dei valori della prosodica e il dizionario che gestisce la prosodica.
    lista_finali = []
    lista_prosidica = []
    prosidica = 0
    diz_pros = dict()
    
    for riga in verso:                                                                                                  #ciclo che scorre tutte le righe della poesia
        lista_lunghezze.append(num_es(riga))                                                                            #appendo alla lista dell'es in ogni riga il risultato della funzione num_es
        lista_finali.append(es_fin(riga))                                                                               #appendo alla lista dell' es finali il risultato della funzione es_finale
                           
        if (lista_lunghezze[-1], lista_finali[-1]) not in diz_pros:                                                     #passo al dizionario una tupla di (ultima es inserita, ultimo numero di es inserito) e se non è presente le da un valore prosodico che parte da 0 e ogni volta che va nel dizionario aggiunge 1
            diz_pros[(lista_lunghezze[-1], lista_finali[-1])] = prosidica
            prosidica += 1
        lista_prosidica.append(diz_pros.get((lista_lunghezze[-1], lista_finali[-1])))                                   #prendo il valore assegnato alla tupla e la listo nella lista dei valori della prosodica 
    return (lista_prosidica, periodo(lista_prosidica), lista_lunghezze, lista_finali)                                   #Infine ritorno i valori in una tupla (lista dei valori della prosodica, periodo che calcolo chiamando la funzione periodo sopra descritta, lista dell'es in ogni riga, lista dell' es finali)

#Parte usata per debuggare il codice senza dover eseguire lo script di test
if __name__ == "__main__":
    def divisori(lunghezza, inizio):
        for i in range(inizio, lunghezza//2+1):
            if lunghezza % i==0:
                return i
    
    def periodo(lista_prosidica):
        lunghezza = len(lista_prosidica)
        #ciclo 1 che parte dal periodo minimo = 3 e nel caso non trovi corrispondenza aumenta la lunghezza del periodo
        inizio = 3
        while True:
            j = divisori(lunghezza, inizio)
            lista1 = lista_prosidica[0:j]
            #ciclo 2 che parte confronta tutti i periodi successivi della stessa lunghezza di lista1
            for i in range(j, lunghezza, j):
                lista2 = lista_prosidica[i:i+j]
                if confronto(lista1, lista2) is False:
                    inizio = j+1
                    break
                if i+j == lunghezza:
                    return j
        #se invece è arrivato alla metà senza trovare corrispondenza restituisce 1
        return 1
    
    def confronto(lista1, lista2):
        diz_mod =dict()
        #cerca la corrispondenza biunivoca confrontandoli in un dizionario
        for indice, elem in enumerate(lista1):
            #in queste situazioni elencate crea una corrispondenza
            if elem not in diz_mod and lista2[indice] not in diz_mod.values() or diz_mod.get(elem) == lista2[indice]:
                diz_mod[elem] =  lista2[indice]
            else:
                return False
        return True
    
    def num_es(riga):
        vocali = ["a","e","i","o","u","j","y"]
        num_es=1
        lunghezza_riga = len(riga)
        for i in range(lunghezza_riga):
            if riga[i] in vocali and i+1 < lunghezza_riga and riga[i+1] not in vocali:
                num_es+=1
        return num_es
    
    def es_fin(riga):
        vocali = ["a","e","i","o","u","j","y"]
        riga = riga[::-1]
        es = ''
        lunghezza_riga = len(riga)
        for i in range(lunghezza_riga):
            es += riga[i]
            if riga[i] not in vocali and i+1 < lunghezza_riga and riga[i+1] in vocali:
                return es[::-1]
                
    #apre il file e lo inserisce nella variabile verso
    with open('random-2048-rnd.txt', encoding="utf8") as verso:
        verso = verso.read().lower()
    
    #passo la poesia intera alla funzione e la rendo interpretabile
    tran = verso.maketrans('àáâãäåèéêëìíîïòóôõöøùúûüýÿ', 'aaaaaaeeeeiiiioooooouuuuyy', ' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
    verso = verso.translate(tran).splitlines()
    
    #definizioni variabili
    lista_lunghezze = []
    lista_finali = []
    lista_prosidica = []
    prosidica = 0
    diz_pros = dict()
    
    #ciclo che scorre tutte le righe della poesia
    for riga in verso:
        lista_lunghezze.append(num_es(riga))
        lista_finali.append(es_fin(riga))
                            
        #passo al dizionario una tupla di (es, lunghezza) e se non è presente le da un valore
        if (lista_lunghezze[-1], lista_finali[-1]) not in diz_pros:
            diz_pros[(lista_lunghezze[-1], lista_finali[-1])] = prosidica
            prosidica += 1
                                
        #prendo il valore assegnato alla tupla e la listo
        lista_prosidica.append(diz_pros.get((lista_lunghezze[-1], lista_finali[-1])))
        
    #ritorno i valori in una tupla
    print((lista_prosidica, periodo(lista_prosidica), lista_lunghezze, lista_finali))