import urllib
from re import search
from re import sub
from textgenrnn import textgenrnn



### DATA

# annetaan polku Kalevalan verkkolähteeseen
polku = "https://www.gutenberg.org/cache/epub/7000/pg7000.txt"

# haetaan verkkosisältö
file = urllib.request.urlopen(polku)

# alustetaan tyhjä lista
kalevala = []

# tehdään enkoodauskonversio
for line in file:
    kalevala.append(line.decode("utf-8"))

# metodi, jolla voidaan etsiä listasta string-tyyppisiä olioita tiettyä fraasia
def paikka_jossa(data, hakulause):
    for indeksi, alkio in enumerate(data):
        if search(hakulause, alkio):
            return indeksi
    return None

# mistä alkavat varsinaiset runot
ensimRuno = paikka_jossa(kalevala, "(?i)ensimmäinen runo")

# jos haettua fraasia ei löydykään, palauttaa metodi arvon 'None', joten otetaan kaikki listan alusta (alkiosta 0)
ensimRuno = ensimRuno if ensimRuno != None else 0

# mihin varsinaiset runot loppuvat, "End of the Project Gutenberg e-Book"
kirjaLoppuu = paikka_jossa(kalevala, "(?i)end of the") - 1

# jos haettua fraasia ei löydykään, palauttaa metodi arvon 'None', joten mennään listan loppuun asti
kirjaLoppuu = kirjaLoppuu if kirjaLoppuu != None else len(kalevala)

# metodi, korvaamaan tietyt merkkijonot ja poistamaan sen jälkeen tyhjät alkiot
def etsi_korvaa(data, lauseke):
    for indeksi, alkio in enumerate(data):
        data[indeksi] = sub(lauseke, '', alkio).strip()
    data = list(filter(None, data))
    return(data)

# varsinainen runo-osuus verkkosisällöstä
runot = etsi_korvaa(kalevala[ensimRuno:kirjaLoppuu], '\r\n')



### NEUROVERKOT

# työkalujen alustus
textgen = textgenrnn()
textgen.reset()

## neuroverkon treenaus:
# treenataan 20 generaatiota, joista
# neljän välein testigeneraatio,
# käytetään treenaukseen 70% datasta, ja
# pudotetaan tällä generaatiolla pois 20% neuroverkon edellisellä generaatiolla saamista tokeneista
textgen.train_on_texts(runot, new_model=True, num_epochs=20, gen_epochs=4, train_size=0.7, dropout=0.2)



# generoidaan uusia säkeitä
i = 0
while i < 10:
    textgen.generate()
    i = i+1
