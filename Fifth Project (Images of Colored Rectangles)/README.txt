Il file program01.py è il file da me ideato e creato, gli altri sono file di testing forniti dall'richiedente del progetto

Queste erano le richieste progettuali:

Abbiamo una immagine formata da N rettangoli colorati (vuoti, è disegnato solo il bordo) su sfondo nero che vogliamo comprimere.
Per comprimerla bisogna trovare nell'immagine tutti gli N rettangoli presenti, anche se intersecati.
Dobbiamo ordinare i rettangoli in modo che la sequenza di operazioni di disegno riproduca fedelmente l'immagine originale.
Potete assumere che:
    - tutti i rettangoli hanno colori diversi
    - ciascun rettangolo ne interseca almeno un altro
    - i lati di rettangoli diversi non si sovrappongono per lungo ma si incrociano solamente
    - gli angoli di rettangoli diversi non si sovrappongono
    - la sequenza è unica (esiste una sola sovrapposizione tra rettangoli che li ordina)

Per ciascuno degli N rettangoli individuati abbiamo 5 informazioni da codificare sotto forma di una immagine:
    - x, y: coordinate dell'angolo superiore sinistro (x=colonna, y=riga)
    - w, h: larghezza ed altezza in pixel
    - C:    colore del rettangolo

Lo schema di compressione costruisce una seconda immagine di dimensioni 5xN.
La nuova immagine contiene, nello stesso ordine della sequenza di disegno, 
su righe successive dall'alto in basso i dati di ciascun rettangolo 
codificati come 5 pixel consecutivi in orizzontale come segue:
    x, y, w, h: sono codificati ciascuno con un pixel: i tre canali RGB del pixel rappresentano il valore in base 256.
        Esempio: (1,2,3) = 1 * 256^2 + 2*256 + 3
    C: è il colore del 5° pixel

Infine vogliamo conoscere il bounding-box del gruppo di rettangoli, ovvero il rettangolo minimo,
con angolo superiore sinistro in (xmin, ymin) ed angolo inferiore destro (xmax, ymax)
che racchiude tutti i rettangoli.

Progettate ed implementate la funzione ex1(image_filename, encoded_filename) che:
    - legge il file indicato dal parametro 'image_filename' usando la libreria 'images' allegata
    - individua gli N rettangoli e li ordina
    - costruisce l'immagine 5xN che codifica le informazioni dei rettangoli
    - salva l'immagine codificata nel file indicato dal parametro 'encoded_filename'
    - ritorna la tupla con le 4 coordinate (xmin, ymin, xmax, ymax) del bounding box

ATTENZIONE: non importate altre librerie e non aprite file diversi da quelli passati per argomento.

#############################################################################################################
The program01.py file is the file I designed and created, the others are testing files provided by the project applicant

These were the design requests:

We have an image that we want to compress. The image has a black
background and contains N empty rectangles, for which only the four
sides are drawn.

To compress the image, we need to find all the N rectangles, even if
they have their sides intersecting.  We need to find the order in
which the rectangles were drawn so that we can encode the sequence of
the drawing operations and perfectly reproduce the original image.

You can assume that:
    - all the rectangles have different colors
    - each rectangle intersects at least another one
    - the sides of different rectangles do not overlap but just cross
    - the vertices of different rectangles do not overlap
    - the sequence of the drawing operations is unique (there is only
      one overlap between rectangles that orders them)

To compress the image, we need to encode 5 pieces of information for
each of the N rectangles:
    - x, y: coordinates of the upper left vertex (x=column, y=row)
    - w, h: width and height of the rectangle in pixels
    - C: color of the sides of the rectangle.

The compression scheme builds a second image with size 5xN pixels.
The new image contains one row for each rectangle, in the same order
of the sequence of drawing. Each row encodes the corresponding
rectangle considering the values of x, y, w, h and C as a pixel: while
C is a pixel with color C, the three RGB channels of the other pixels
represent a digit of the corresponding value, on base 256. For
example: a pixel with color (1,2,3) represents the value 130815, since
(1,2,3) = 1*255*(2*255+3)=130815.

Finally, we want to know the bounding-box of the group of rectangles,
namely the minimum rectangle, with upper left vertex in (xmin, ymin)
and lower right vertex (xmax, ymax) which encloses all the rectangles.

Design and implement the function ex1(image_filename, encoded_filename)
which:
    - reads the file indicated by the parameter 'image_filename' using
      the 'images' library
    - locates and find the drawing order of the N rectangles 
    - builds the 5xN image that encodes rectangle information
    - saves the encoded image in the file indicated by the
      'encoded_filename' parameter
    - returns the tuple with the 4 coordinates (xmin, ymin, xmax,
      ymax) of the bounding box

WARNING: do not import other libraries and do not open files other
than the ones in the argument list.