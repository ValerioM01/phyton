# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

def ex1(int_seq, subtotal):
    lista = list(map(int, int_seq.split(',')))          #creo una lista d'interi dalla stringa data
    lunghezza = len(lista)                              #creo una variabile con valore pari alla lunghezza della lista
    count = 0                                           #counter che contera quante combinazioni sono possibili
    
    if all(v == lista[1] for v in lista):               #nel caso siano tutti 1 
        count = max(0, lunghezza - subtotal + 1)        #applico la formula matematica valida impedendo di restiutuire un valore negativo
        
    else:
        for v in range(lunghezza):                      #ciclo che ricorda a che cifra sono
            somma = 0                                   #inizializzo la somma a 0 
        
            while v < lunghezza and somma <= subtotal:  #controllo se ho superato l'ultima cifra della lista e se la somma sfora il valore richiesto
                somma += lista[v]                       #aggiungo alla somma ogni volta il valore successivo
                v += 1                                  #agggiungo 1 all'indice per passare alla cifra successiva
                                                    
                if somma == subtotal:                   #e nel caso in cui la somma sia gia uguale al subtotale
                    count += 1                          #aggiungo uno al mio counter
           
    return count                                        #ritorna la variabile count


#Parte usata per debuggare il codice senza dover eseguire lo script di test
if __name__ == '__main__':
    subtotal = 9
    int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
    def ex(int_seq, subtotal):
        lista = list(map(int, int_seq.split(',')))
        lunghezza = len(lista)
        count = 0 
        lista_prov=[]
        
        for n in range(lunghezza):
            lista_prov.append(lista[n])
            
            if sum(lista_prov) == subtotal:
                count += 1
            elif sum(lista_prov) > subtotal:
                ex(','.join(lista[n:]),subtotal)
                
        return count      
    print(ex(int_seq,subtotal))