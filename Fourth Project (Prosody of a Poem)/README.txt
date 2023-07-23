Il file program01.py è il file da me ideato e creato, gli altri sono file di testing forniti dall'richiedente del progetto

Queste erano le richieste progettuali:

Sia dato un testo che contiene un poema, ovvero una successione di versi in rima.
Il poema è contenuto in un file, un verso per riga.

Vogliamo analizzarlo per estrarne la struttura prosodica, ovvero lo schema poetico in esso usato.
Per far questo sono utili le seguenti definizioni:
    - un 'elemento sonoro' (ES) è una successione massimale di 1 o più consonanti seguite da 1 o più vocali
        - prima tutte le consonanti
        - poi tutte le vocali (aeiouyj)
        - ignorando eventuali caratteri non alfabetici come spazi, numeri e segni di interpunzione 
        - togliendo gli accenti dalle lettere accentate
        - e ignorando la differenza tra maiuscole e minuscole
        NOTA:   fanno eccezione il primo ES di un verso, che può essere composto da sole vocali
                e l'ultimo ES, che può essere composto di sole consonanti
    - un verso è composto da una successione di elementi sonori, l'ultimo dei quali è chiamato 'finale'
        Esempio:      
        Se il verso è "Paperino andò al mare a pescare" 
            - gli elementi sonori sono     ["pa", "pe", "ri", "noa", "ndoa", "lma", "rea", "pe", "sca", "re"]
            - la finale è                   "re"
            - il verso è lungo              10 ES
        notate che le lettere accentate hanno perso l'accento e non ci interessa la distinzione tra maiuscole e minuscole
    - la struttura prosodica di una poesia è una lista di interi, uno per ciascun verso
    - per ciascun verso si considerano sia il numero di ES (#ES) che la sua finale
    - al primo verso va associato il numero 0
    - a ciascuno dei versi successivi va associato:
        - l'intero che è stato già associato ad un verso precedente che ha stesso #ES e finale
        - altrimenti un nuovo intero (che segue l'ultimo già usato)
Esempio:
    se la poesia è quella qui sotto                     gli elementi sonori sono                                    #ES finale   prosodia
    '''
    Dì pestaggio tessessi allarmai, Partenopea!         di pe sta ggio te sse ssia lla rmai pa rte no pea           13  pea         0
    Sembrò svieremo imbarcate, aumentarono usurpai?     se mbro svie re moi mba rca teau me nta ro nou su rpai      14  rpai        1
    Flash privé spirereste? Pentecoste deturpai         fla shpri ve spi re re ste pe nte co ste de tu rpai         14  rpai        1
    scrost, direttamante arrischiai,                    scro stdi re tta ma ntea rri schiai                          8  schiai      2
    odi attuazione vernicera Partenopea.                o dia ttua zio ne ve rni ce ra pa rte no pea                13  pea         0
    Psion trentacinque preesistiti calzascarpe          psio ntre nta ci nque pree si sti ti ca lza sca rpe         13  rpe         3
    nobilt fiacchi vedesti avvertirsi spermatozoi?      no bi ltfia cchi ve de stia vve rti rsi spe rma to zoi      14  zoi         4
    Igloo rubi incassando giurati spermatozoi!          i gloo ru bii nca ssa ndo giu ra ti spe rma to zoi          14  zoi         4
    Saprai reputasse inebriai                           sa prai re pu ta ssei ne briai                               8  briai       5
    man l'ballaste segnaleremo soprascarpe.             ma nlba lla ste se gna le re mo so pra sca rpe              13  rpe         3
    '''
    l'elenco dei numeri di ES è     [13,    14,     14,     8,        13,    13,    14,    14,    8,       13   ]
    l'elenco delle finali è         ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe']
    quindi la struttura prosodica è [0,     1,      1,      2,        0,     3,     4,     4,     5,       3    ]

    Dalla struttura prosodica dovete determinare il periodo, ovvero la lunghezza minima di un gruppo di versi che si ripete
    con lo stesso schema.
    In questo esempio il modulo = 5, infatti la prosodia è formata da due sequenze uguali di 5 elementi 
    che seguono lo schema [0, 1, 1, 2, 0], infatti [0, 1, 1, 2, 0] è equivalente a [3, 4, 4, 5, 3]

    La funzione deve tornare la tupla che contiene nell'ordine i 4 valori: 
        - prosodia: ovvero la lista di interi che avete calcolato da #ES e lunghezza dei versi
        - periodo:  ovvero la lunghezza minima dello schema prosodico che si ripete
        - lunghezze: ovvero la lista delle lunghezze (#ES) dei versi
        - finali:   ovvero la lista degli ES finali di ciascun verso

    Quindi per questo esempio la funzione deve tornare la tupla:
        ( [0, 1, 1, 2, 0, 3, 4, 4, 5, 3], 5, [13, 14, 14, 8, 13, 13, 14, 14, 8, 13 ], 
        ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe'])

ATTENZIONE: non potete usare altre librerie o aprire altri file.
TIMEOUT: Il timeout per questo esercizio è di 100ms (0.1 secondi)

#############################################################################################################
The program01.py file is the file I designed and created, the others are testing files provided by the project applicant

These were the design requests:

We have a text containing a poem, that is a sequence of verses with rhymes.
The poem is stored in a text file, one verse per line.

We want to analyze the poem to extract its prosodic structure, i.e. the repetition scheme of the poem.

To this aim we need the following definitions:
    - a 'sound element' (SE) is a maximal sequence of 1 or more consonants followed by 1 or more vowels: 
        - first all the consonants
        - then all the vowels (aeioujy)
        - all non-alphabetic chars like spaces, numbers, colon, comma etc. must be ignored
        - all accents from accented letters (e.g. è->e) must be removed
        - differences between uppercase and lowercase letters are disregarded
        NOTICE: the only exceptions are the first and the last SE of a verse, that could contain only vowels
                and only consonants, respectively.
    - a verse is made of a sequence of sound elements, the last of which is called 'final'
        Example:      
        If the verse is "Donàld Duck! wènt, to tHe seas'ìde to swim" 
            - the SEs are           [ 'do', 'na', 'lddu', 'ckwe', 'ntto', 'the', 'sea', 'si', 'de', 'to', 'swi', 'm' ]
            - the final SE is       'm'
            - the verse length is   12
        notice that accents have been removed, letters are lowercase and non-alphabetic chars are ignored.
    - the prosodic structure of the poem is a list of numbers, one for each verse
    - the prosodic structure is obtained considering both the number of SE (#SE) and the final SE of the verses 
    - the first verse is associated with the number 0
    - each one of the following verses are associated:
        - with the same number associated to an earlier verse having the same #SE and final SE
        - or with a new number, obtained adding 1 to the greatest number, already used
    - the period of the verses is the minimum number of verses that repeats with the same schema.

Example:
    If the poem is the text here below                  its sound elements are                                      #SE final   prosody
    '''
    Dì pestaggio tessessi allarmai, Partenopea!         di pe sta ggio te sse ssia lla rmai pa rte no pea           13  pea         0
    Sembrò svieremo imbarcate, aumentarono usurpai?     se mbro svie re moi mba rca teau me nta ro nou su rpai      14  rpai        1
    Flash privé spirereste? Pentecoste deturpai         fla shpri ve spi re re ste pe nte co ste de tu rpai         14  rpai        1
    scrost, direttamante arrischiai,                    scro stdi re tta ma ntea rri schiai                          8  schiai      2
    odi attuazione vernicera Partenopea.                o dia ttua zio ne ve rni ce ra pa rte no pea                13  pea         0
    Psion trentacinque preesistiti calzascarpe          psio ntre nta ci nque pree si sti ti ca lza sca rpe         13  rpe         3
    nobilt fiacchi vedesti avvertirsi spermatozoi?      no bi ltfia cchi ve de stia vve rti rsi spe rma to zoi      14  zoi         4
    Igloo rubi incassando giurati spermatozoi!          i gloo ru bii nca ssa ndo giu ra ti spe rma to zoi          14  zoi         4
    Saprai reputasse inebriai                           sa prai re pu ta ssei ne briai                               8  briai       5
    man l'ballaste segnaleremo soprascarpe.             ma nlba lla ste se gna le re mo so pra sca rpe              13  rpe         3
    '''
    the list of #SE is              [13,    14,     14,     8,        13,    13,    14,    14,    8,       13   ]
    the list of final SE is         ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe']
    thus the prosodic structure is  [0,     1,      1,      2,        0,     3,     4,     4,     5,       3    ]

    From the prosodic structure you should find the period, i.e. the minimum length of verses that repeats with the same schema.
    In this example the period is 5, in facts the prosody is obtained by repeating twice the [0, 1, 1, 2, 0] schema,
    since the sequence [0, 1, 1, 2, 0] has the same schema of [3, 4, 4, 5, 3]

You have to define a function that analyzes the prosody of a poem stored in a file and returns a tuple with four elements, namely:
    - a list with the prosodic structure of the poem
    - an integer representing the period of the verses
    - a list with the number of Sound Elements (#SE) of each verse
    - a list with the final SE of each verses

    From the above example, the function should return the tuple
          ( [0, 1, 1, 2, 0, 3, 4, 4, 5, 3], 5, [13, 14, 14, 8, 13, 13, 14, 14, 8, 13 ], 
            ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe'])

NOTICE: you cannot use other libraries or open other files.
TIMEOUT: The timeout for each test is 100ms (0.1 seconds)