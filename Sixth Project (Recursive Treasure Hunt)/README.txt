Il file program01.py è il file da me ideato e creato, gli altri sono file di testing forniti dall'richiedente del progetto

Queste erano le richieste progettuali:

Nikita è un'abile spia che deve trovare e seguire una serie di
indizi (una sequenza di parole) che la porteranno a scoprire una o più
informazioni segrete, sotto forma di sequenze di parole.  Per ottenere
il/i segreto/i Nikita deve visitare diverse città ed in ciascuna città
troverà un indizio che le rivelerà quale sia la prossima città in cui
dovrà spostarsi.  Per ogni città visitata, Nikita otterrà una nuova
parola del segreto.

Come in una caccia al tesoro, Nikita dovrà esplorare una rete di
città, raccogliendo informazioni in ognuna di esse.

NOTA: un indizio di una città può portare in più città alternative.
    Quindi i percorsi da esplorare potrebbero essere multipli ed i
    segreti più di uno.

NOTA: se in una certa città NON C'È l'istruzione corrispondente al
    prossimo indizio vuol dire che la rete di spie nemica ha scoperto
    e distrutto l'informazione, ed il segreto che Nikita stava
    costruendo con quella sequenza non può essere più completato.
    Nikita, quindi, abbandona quella pista e prova a completare gli
    altri segreti che ha già raccolto.

Vogliamo scoprire tutti i segreti che Nikita può ricostruire dati gli
indizi a disposizione e le istruzioni disseminate nelle diverse città.

Le indicazioni su come muoversi tra le città sono contenute nel file
file_istruzioni secondo il seguente formato:
    - ogni riga che inizia con il carattere cancelletto '#' va ignorata
    - le città sono sempre scritte in MAIUSCOLO
    - gli indizi e le parole del/i segreto/i da scoprire sono sempre
    scritte in minuscolo
Il file contiene, separate da almeno uno spazio/tab/accapo, zero o più
istruzioni da seguire.  Ogni istruzione è scritta come la
concatenazione di quattro parole:
    - città         (parola MAIUSCOLA)
    - indizio       (parola minuscola)
    - destinazione  (parola MAIUSCOLA)
    - segreto       (parola minuscola)

Esempio:
    l'istruzione      ROMAcarciofoPARIGIchampagne     indica che
        - quando la spia è a                    'ROMA'
        - se l'indizio seguente è               'carciofo'
        - la spia deve andare a                 'PARIGI'
        - ed aggiungere al segreto la parola    'champagne'

NOTA: potete assumere che il file non contenga mai istruzioni uguali.
NOTA: possono essere presenti istruzioni diverse che, partendo dalla stessa città,
    per lo stesso indizio portano in città diverse e/o producono segreti diversi
    Esempio:
    ROMAcarciofoPARIGIchampagne
    ROMAcarciofoCANCUNchampagne
    ROMAcarciofoPARIGImitraglietta
    ROMAcarciofoCATANZAROcommissario

Progettate ed implementate la funzione ex1(istructions_file, initial_city, clues) 
ricorsiva o che usa funzioni o metodi ricorsivi, che riceve come argomenti:

    - istructions_file: il nome di un file di testo che contiene le
                        istruzioni da seguire in ogni città
    - initial_city:     il nome della città da cui parte Nikita (una parola MAIUSCOLA)
    - clues:            una lista di indizi (stringa formata da parole minuscole separate
                        da spazio)

che ricostruisce tutti i possibili segreti e che torna come risultato
l'insieme di TUTTE le possibili coppie (segreto, CITTÀ), dove:
    - segreto è uno dei possibili segreti scoperti da Nikita, ovvero una
            stringa ottenuta dalla concatenazione delle parole scoperte
            separate da spazio
    - CITTÀ   è la città in cui la spia è arrivata quando ha completato il segreto

Esempio:
Se il file è 'esempio.txt', la città di partenza è 'ROMA' e gli indizi sono 
"" 
tutte le possibili coppie segreto/città finale saranno:
     ('vendita diamanti rubati stanotte ad anversa', 'CANCUN')
     ('vendita cannoni mercato nero del cairo',      'CANCUN')
     ('furto di diamanti a buckingham palace',       'MILANO')
     ('mata hari ha sedotto ambasciatore zambia',    'MILANO')

NOTA: è vietato importare/usare altre librerie o aprire file tranne quello indicato

NOTA: il sistema di test riconosce la presenza di ricorsione SOLO se 
    la funzione/metodo ricorsivo è definita a livello esterno. 
    NON definite la funzione ricorsiva all'interno di un'altra funzione/metodo 
    altrimente fallirete tutti i test.

#############################################################################################################
The program01.py file is the file I designed and created, the others are testing files provided by the project applicant

These were the design requests:

Nikita, a clever spy, needs to follow a series of clues (namely a
sequence of words) that will lead her to discover one or more secret
information (sequences of words).  To find the secret(s) Nikita has to
visit different cities: in each city Nikita will find which is the
next city she has to move to and will also get a new word of the
secret.  The next city you have to move to depends on the next clue.

It is a bit like a treasure hunt, in which Nikita explores a network
of cities, collecting information.

NOTE: From the same city, the same clue can lead to multiple
    alternative cities.  So the paths to explore could be multiple and
    the secrets more than one.

NOTE: if in a certain city the instruction corresponding to the next
    clue is missing, this means that the enemy spy network has
    captured and destroyed the information. This also means the secret
    that Nikita was following with that sequence cannot be completed
    anymore.  Thus, our spy quits that sequence and she tries to
    complete all the other secrets she has already collected.

We want to reconstruct all the secrets that Nikita could reconstruct,
given the available clues and the pieces of instructions scattered
throughout the different cities.

The instructions about how to move between the cities are contained in
a text file, according to the following format:
    - every line starting with the '#' character should be ignored
    - cities are always written in UPPERCASE
    - the clues and words of the secret(s) to be discovered are always
    written in lowercase letters

The file contains, separated by at least one space/tab/return, zero or
more instructions to follow.  Each instruction is written as the
concatenation of four words:
    - city 	  (UPPERCASE word)
    - clue 	  (lowercase word)
    - destination (UPPERCASE word)
    - secret 	  (lowercase word)

Example:
    the instruction ROMAcarciofoPARIGIchampagne indicates that
        - when the spy is in                         'ROME'
        - if the following clue is                   'carciofo'
        - the spy must go to                         'PARIGI'.
        - and add to the secret the word             'champagne'

NOTE: You can assume that the each line of instruction is unique.
NOTE: There may be different instructions that even starting from the
      same city AND having the same clue, lead to different cities and/or
      produce different secrets.
    Example:
    ROMAcarciofoPARIGIchampagne
    ROMAcarciofoCANCANCANCUNchampagne
    ROMAcarciofoPARIGImitraglietta
    ROMAcarciofoCATANZAROcommissario

Design and implement the function ex1(instructions_file, initial_city, clues)
recursive or using recursive functions or methods, which receives as
arguments:
    - instructions_file: the name of a text file that contains
                        instructions to follow in each city
    - initial_city:      the name of the initial city from which Nikita
                        starts her journey (UPPERCASE word)

    - clues:             a list of clues (string of lowercase words separated
                        by spaces) 

that reconstructs all the possible secrets Nikita can discover and that
returns the set of ALL possible pairs (secret, CITY), where:
    - secret is one of the possible secrets Nikita can discover, namely a
            string obtained by the concatenation of the words collected,
            separated by space
    - CITY   is the city reached by Nikita when she completed that secret.

Example:

If the file is 'example.txt', the starting city is 'ROMA' and the
clues are "la bocca sollevò dal fiero pasto", then all the possible
secret/city pairs will be:
    ('vendita diamanti rubati stanotte ad anversa', 'CANCUN')
    ('vendita cannoni mercato nero del cairo',      'CANCUN')
    ('furto di diamanti a buckingham palace',       'MILANO')
    ('mata hari ha sedotto ambasciatore zambia',    'MILANO')


NOTE: it is forbidden to import/use other libraries or open files
      except the one indicated

NOTE: The test system recognizes recursion ONLY if the recursive
      function/method is defined in the outermost level.  DO NOT
      define the recursive function within another function/method
      otherwise you will fail all the tests.