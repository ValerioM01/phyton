Il file program01.py è il file da me ideato e creato, gli altri sono file di testing forniti dall'richiedente del progetto

Queste erano le richieste progettuali:

Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che riceve come argomenti la stringa int_seq e l'intero subtotal e restituisce il numero di sottostringhe di int_seq la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9, la funzione deve restituire 7.

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

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

#############################################################################################################
The program01.py file is the file I designed and created, the others are testing files provided by the project applicant

These were the design requests:

We have a string int_seq containing a sequence of comma-separated non-negative integers and a positive integer subtotal.

Design a function ex1(int_seq, subtotal) that takes the string int_seq and the integer subtotal as arguments and returns the number of substrings of int_seq whose sum of values is subtotal.

For example, for int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' and subtotal=9, the function should return 7.

Indeed:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
  _'0,4,0,3,1,0,1,0'_____________
  _'0,4,0,3,1,0,1'_______________
  ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
  _______________________'5,0,4'_

NOTE: it is FORBIDDEN to use/import any other library apart from the ones already present

NOTE: The timeout for this exercise is 1 second for each test
