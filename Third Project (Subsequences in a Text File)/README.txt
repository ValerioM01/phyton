Il file program01.py è il file da me ideato e creato, gli altri sono file di testing forniti dall'richiedente del progetto

Queste erano le richieste progettuali:

In un file di testo e' riportata una sequenza binaria S. Siamo interessati
alla  frequenza delle sottosequenze di S(la frequenza di una sottosequenza
di S e'  il numero di volte che la sottosequenza occorre in S). Si consideri
ad esempio il file di testo f1.txt contenente la sequenza

01010010010001000111101100001010011001111000010010011110010000000

la sottosequenza '00' ha frequenza 23 mentre la sottosequenza '1000' ha
frequenza 5. Notare che la sottosequenza e' separata su tre righe nel file.

Dati gli interi a e b, con a<=b, siamo interessati a contare le frequenze delle
sottosequenze si S che presentano una lunghezza tra a e b. Dato l'intero
n vogliamo listare le al piu' n frequenze massime ciascuna con le
corrispondenti sottosequenze. Nel caso ci siano meno di n distinte
frequenze con lunghezza tra a e b, l'output avra' meno di n elementi.

Progettare la funzione ex1(ftesto, a, b, n) che prende come parametri:
    - ftesto: l'indirizzo del file di testo in cui e' registrata la sequenza
      binaria in una o piu' righe consecutive;
    - a,b: i due interi a e b con a<=b che indicano l'intervallo delle
      lunghezze delle sottosequenze  di cui contare le frequenze;
    - n: l'intero che indica il numero di frequenze massime cui siamo
      interessati;
e restituisce una lista di tuple.

Ciascuna tupla della lista ha come prima coordinata una frequenza e come
seconda coordinata la lista delle sottosequenze che hanno quella frequenza.
La lista deve contenere solo le tuple con le prime n frequenze massime e, in
caso ci siano meno di n frequenze distinte, conterra' tutte le tuple con
frequenze distinte. La lista e' ordinata in ordine lessicografico rispetto
alla prima coordinata delle tuple e in ciascuna tupla la lista presente
nella seconda coordinata e' ordinata lessicograficamente.

Ad esempio, ex1('ft1.txt', 2, 4, 10) restituisce la lista:
    [ (4, ['0001', '0011', '1100' ]),
    (5, ['011', 1000', '110' ]),
    (6, ['0000', '111']),
    (7, ['0010','1001' ]),
    (8, ['0100']),
    (10,['010']),
    (11,['000', '001', '11']),
    (12,['100']),
    (15,['01','10']),
    (23,['00'])
    ]

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

#############################################################################################################
The program01.py file is the file I designed and created, the others are testing files provided by the project applicant

A binary sequence S is reported in a text file. We are interested
to the frequency of subsequences of S(the frequency of a subsequence
of S is the number of times the subsequence occurs in S). Consider
for example the text file f1.txt containing the sequence

01010010010001000111101100001010011001111000010010011110010000000

the subsequence '00' has frequency 23 while the subsequence '1000' has
frequency 5. Notice that the subsequence is separated on three lines in the file.

Given the integers a and b, with a<=b, we are interested in counting the frequencies of
subsequences si S that have a length between a and b. Given the whole
n we want to list at most n maximum frequencies each with le
corresponding subsequences. In case there are less than n distinct
frequencies with lengths between a and b, the output will have fewer than n elements.

Design the function ex1(ftext, a, b, n) which takes as parameters:
     - ftext: the address of the text file where the sequence is recorded
       binary in one or more consecutive lines;
     - a,b: the two integers a and b with a<=b which indicate the range of
       lengths of subsequences to count frequencies;
     - n: the integer that indicates the number of maximum frequencies we are at
       interested;
and returns a list of tuples.

Each tuple in the list has as its first coordinate a frequency and how
second coordinate the list of subsequences that have that frequency.
The list must contain only the tuples with the first n maximum frequencies and, in
if there are fewer than n distinct frequencies, it will contain all tuples with
distinct frequencies. The list is sorted in lexicographic order with respect
to the first coordinate of the tuples and in each tuple the present list
in the second coordinate it is lexicographically ordered.

For example, ex1('ft1.txt', 2, 4, 10) returns the list:
     [ (4, ['0001', '0011', '1100' ]),
     (5, ['011', 1000', '110' ]),
     (6, ['0000', '111']),
     (7, ['0010','1001' ]),
     (8, ['0100']),
     (10,['010']),
     (11,['000', '001', '11']),
     (12,['100']),
     (15,['01','10']),
     (23,['00'])
     ]

NOTE: The timeout for this exercise is 1 second for each test.