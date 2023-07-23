Il file program01.py è il file da me ideato e creato, gli altri sono file di testing forniti dall'richiedente del progetto

Queste erano le richieste progettuali:

Abbiamo quattro giocatori che si sfidano a Scarabeo+. In ogni mano
di Scarabeo+, i giocatori, a turno, devono inserire una parola nel
tabellone ed ottengono un punteggio, calcolato in base al valore
delle lettere che compongono la parola inserita.

Ogni giocatore crea la propria parola scegliendola a partire da una
mano di 8 lettere, che vengono rimpiazzate una volta che la parola
è stata giocata, finché non sono esaurite. Il numero totale di
lettere è 130.  Il gioco finisce quando un giocatore riesce a
finire tutte le lettere nella sua mano e non ci sono più lettere a
disposizione per rimpiazzare quelle che ha appena giocato (ovvero,
le 130 lettere sono esaurite, perché giocate oppure perché in mano
agli altri giocatori).

Alla fine delle giocate, vince il giocatore che ha accumulato più
punti, considerando che per ogni lettera che rimane non giocata
(ovvero rimane in mano ad un giocatore quando il gioco finisce)
vengono sottratti 3 punti. 
I punteggi sono così calcolati:
1 punto:  E, A, I, O, N, R, T, L, S, U
2 punti: D, G
3 punti: B, C, M, P
4 punti: F, H, V, W, Y
5 punti: K
8 punti: J, X
10 punti: Q, Z

Progettare una funzione ex1(g1, g2, g3, g4, dim_hand, num_letters) che calcola i
punteggi di una partita di Scarabeo+ svolta fra i 4 giocatori, con
la variante che il numero di lettere iniziali è num_letters, piuttosto che
130 e il numero di lettere a disposizione di ogni giocatore è dim_hand.
g1, g2, g3 e g4 sono liste di stringhe che rappresentano le
giocate dei giocatori g1, g2, g3 e g4, rispettivamente, 
in ciascun turno.

ES: dim_hand=5, num_letters=40
g1 = ['seta','peeks','deter']
g2 = ['reo','pumas']
g3 = ['xx','xx']
g4 = ['frs','bern']

Notare che all’inizio della partita 5 lettere vengono date ad ognuno dei
giocatori, dunque il contatore num_letters decresce conseguentemente.

dim_hand - num_letters - parola - punti
5 5 5 5    20            seta      4  0  0  0
5 5 5 5    16            reo       4  3  0  0
5 5 5 5    13            xx        4  3 16  0
5 5 5 5    11            frs       4  3 16  6
5 5 5 5     8            peeks    15  3 16  6
5 5 5 5     3            pumas    15 12 16  6
5 3 5 5     0            xx       15 12 32  6
5 3 3 5     0            bern     15 12 32 12
5 3 3 1     0            deter    21 12 32 12
0 3 3 1     0                       GAME OVER
---------------------------------------------
Finale                            21  3 23  9

Il TIMEOUT per ciascun test è di 0.5 secondi

ATTENZIONE: è proibito:
  - importare altre librerie
  - usare variabili globali
  - aprire file

#############################################################################################################
The program01.py file is the file I designed and created, the others are testing files provided by the project applicant

We have four players competing in Scrabble+. In each hand
of Scrabble+, players take turns entering a word into the
scoreboard and get a score, calculated on the basis of the value
of the letters that make up the entered word.

Each player creates his own word by choosing it starting from one
hand of 8 letters, which are replaced once the word
has been played, until they are exhausted. The total number of
letters is 130. The game ends when one player manages to
finish all the letters in his hand and there are no more letters a
arrangement to replace the ones he just played (i.e.,
the 130 letters are exhausted, either because you have played or because you have one in your hand
to other players).

At the end of the rounds, the player who has accumulated the most wins
points, considering that for each letter that remains unplayed
(i.e. remains in a player's hand when the game ends)
3 points are deducted.
The scores are calculated as follows:
1 point: E, A, I, O, N, R, T, L, S, U
2 points: D, G
3 points: B, C, M, P
4 points: F, H, V, W, Y
5 points: K
8 points: J, X
10 points: Q, Z

Design a function ex1(g1, g2, g3, g4, dim_hand, num_letters) that calculates the
scores of a game of Scrabble+ between 4 players, with
the variant that the number of initial letters is num_letters, rather than
130 and the number of letters available to each player is dim_hand.
g1, g2, g3 and g4 are lists of strings representing the
play of players g1, g2, g3 and g4, respectively,
in each round.

EX: dim_hand=5, num_letters=40
g1 = ['silk','peeks','deter']
g2 = ['offender','pumas']
g3 = ['xx','xx']
g4 = ['frs','bern']

Note that at the start of the game 5 letters are given to each of the
players, so the num_letters counter decreases accordingly.

dim_hand - num_letters - word  -  points
5 5 5 5    20            silk     4 0 0 0
5 5 5 5    16            offender 4 3 0 0
5 5 5 5    13            xx       4 3 16 0
5 5 5 5    11            frs      4 3 16 6
5 5 5 5    8             peeks    15 3 16 6
5 5 5 5    3             cougars  15 12 16 6
5 3 5 5    0             xx       15 12 32 6
5 3 3 5    0             bern     15 12 32 12
5 3 3 1    0             deter    21 12 32 12
0 3 3 1    0                      GAME OVER
---------------------------------------------
Final                             21 3 23 9

The TIMEOUT for each test is 0.5 seconds

ATTENTION: it is forbidden:
  - import other libraries
  - use global variables
  - open files