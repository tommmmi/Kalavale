# Kalavale

```
Tuonne Tuonelan joesta,
halki haukkua hipua,
poika pursi puut purohon,
kaikki kansan kauneutta,

Lemminkäisen leikkeänsä,
katsahtani kaikerosta,
sinisukka äijön lapsi,
katselevi, kääntelevi,

kun ei tyttö pyyettäne,
vastan vaskisen varavan,
kun venynnä kyntämätä,
rauta rautaisen haravan.

   --Kalavale-generaattori
```

28. helmikuuta on Kalevalan päivä, suomalaisen kulttuurin päivä.

Kalevalan päivän kunniaksi pieni neuroverkkojumppa, jossa luodaan uusi kalevalahenkinen runo käyttäen lähdeaineistona alkuperäistä Elias Lönnrotin Kalevalaa. Kalevala on kokonaisuudessaan verkossa saatavilla mm. Project Gutenbergin (www.gutenberg.org) alla osoitteessa: https://www.gutenberg.org/ebooks/7000

### Tekniikasta

Tähän kevytmieliseen harjoitukseen utilisoidaan Pythonin kirjastoja, joista `textgenrnn` näyttelee keskeistä osaa. Se tarjoaa takaisinkytketyt neuroverkot (recurrent neural networks; RNN) sekä niiden alta spesifimmät pitkäkestoinen lyhytkestomuisti -arkkitehtuurin (long short-term memory; LSTM) algoritmit.

Muita vaadittuja Python-kirjastoja ovat `urllib` ja `re`, joista käytetään vain muutamia funktioita.

Käytettävissä olevista CPU:ista ja GPU:ista riippuen Kalevalalla treenaus ('training') kestää tovin:

```bash
Training new model w/ 2-layer, 128-cell LSTMs
Training on 381,489 character sequences.
Epoch 1/20
2980/2980 [==============================] - 547s 183ms/step - loss: 1.9666 - val_loss: 1.6535 - lr: 0.0040
Epoch 2/20
2980/2980 [==============================] - 558s 187ms/step - loss: 1.5752 - val_loss: 1.5002 - lr: 0.0038
Epoch 3/20
2980/2980 [==============================] - 570s 191ms/step - loss: 1.4625 - val_loss: 1.4422 - lr: 0.0036
Epoch 4/20
2980/2980 [==============================] - 578s 194ms/step - loss: 1.3969 - val_loss: 1.4070 - lr: 0.0034

####################
Temperature: 0.2
####################
kuun kulki kullan kulken,

tuli tuonne tultuansa,

Mi on seppo Ilmarinen,

####################
Temperature: 0.5
####################
katsahan kalentamahan.

jos mulla meren metsälle,

itse tuon sisarutahan,

Epoch 5/20
1141/2980 [==========>...................] - ETA 4:42 - loss: 1.3520
```

Tälle projektille voidaan pystyttää Dockerilla kehitysympäristökontti ja ladata siihen kaikki tarvittavat työkalut valmiiksi. ~~Tätä varten katso Dockerfile.~~

Docker Desktopista löytyy valmis työkalu Dev Environments, jolla voi pystyttää kehityskontin hyvin helposti.

Repoon on sisällytetty myös treenauksesta saadut painot, mallin asetukset ja käytetty sanasto.

### Lopputulos

Malli on ajettu oletusasetuksilla ja sitä on treenattu vain 20 generaatiota. Mallia voisi tarkentaa ja kokeilla myös erilaisia neuroverkkoja tähän. Nyt monet mallin generoimat lauseet ovat sanasta sanaan suoraan Kalevalasta tai sitten kaksi kolmesta lauseen sanasta sellaisenaan suoraan. Sinänsä kuitenkin mielenkiintoista, että säkeet kuitenkin ovat ymmärrettäviä sanoja ja runomuoto anteeksiantaa sen verran, että myös tarina välittyy säkeistä.

Sen verran fuskasin, että järjestin säkeet uudelleen, mutta säkeet itsessään ovat suoraan mallin generoimia.
