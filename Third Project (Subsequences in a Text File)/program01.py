# -*- coding: utf-8 -*-

def ex1(ftesto,a,b,n):
    def count_sequenza(stringa, sequenza):                                                                          #Definisco una funzione che conta la sequenza cercata in una stringa
        ripetizioni = 0
        segnalino = stringa.find(sequenza)                                                                          #Metto un segnalino nell'indice dove si trova la sequenza cercata
        while segnalino >= 0:
            ripetizioni += 1                                                                                        #Aggiorno il counter
            segnalino = stringa.find(sequenza, segnalino+1)                                                         #Richiamo ricorsivamente la funzione nella sottostringa successiva al segnalino messo
        return ripetizioni

    fin = open(ftesto)                                                                                              #Dichiarazioni variabili
    sequenza =' '
    mega_listone = {}
    
    for riga in fin:                                                                                                #Creo la sequenza dalla riga del file in input
        parola = riga.strip()
        sequenza += parola
    lunghezza=len(sequenza)
    
    while a <= b:                                                                                                   #Nell'intervallo delle stringhe cercato
        j = a
        i = 0
        while j < lunghezza:                                                                                        #Per ogni sottostringa lancio la funzione count_sequenza
            sottostringa = sequenza[i:j]
            if sottostringa not in str(mega_listone.values()):                                                      
                val = count_sequenza(sequenza, sottostringa)
                if val not in mega_listone:                                                                         #Aggiungo al listone il valore restituito dalla funzione associato alla sottostringa cercata
                    mega_listone[val] = list([sottostringa])
                else:
                    mega_listone[val].append(sottostringa)
            i += 1
            j += 1
        a += 1
    mega_listone = sorted(list((key, sorted(list(value))) for key, value in mega_listone.items()), reverse=True)    #Ordino la lista in modo da restituire i valori ordinati come richiesto
    del mega_listone[n:]
    return sorted(mega_listone)

#Parte usata per debuggare il codice senza dover eseguire lo script di test
if __name__ == '__main__':
    fin = open('ft1.txt')
    a = 2
    b = 4
    n = 10
    
    def count_sequenza(stringa, sequenza):
        ripetizioni=0
        segnalino=stringa.find(sequenza)
        
        while segnalino>=0:
            ripetizioni+=1
            segnalino=stringa.find(sequenza, segnalino+1)
            
        return ripetizioni
    
    sequenza=''
    mega_listone={}
    
    for riga in fin:
        parola = riga.strip()
        sequenza += parola
    lunghezza=len(sequenza)
    
    while a<=b:
        j=a
        i=0
        while j < lunghezza:
            sottostringa = sequenza[i:j]
            if sottostringa not in str(mega_listone.values()):
                val = count_sequenza(sequenza, sottostringa)
                if val not in mega_listone:
                    mega_listone[val] = list([sottostringa])
                else:
                    mega_listone[val].append(sottostringa)
            i+=1
            j+=1
        a+=1
    mega_listone = sorted(list((key, sorted(list(value))) for key, value in mega_listone.items()), reverse=True)
    del mega_listone[n:]
    print(sorted(mega_listone))