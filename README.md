# Kalavale

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
2980/2980 [==============================] - ETA: 0s - loss: 1.3969
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

2980/2980 [==============================] - 578s 194ms/step - loss: 1.3969 - val_loss: 1.4070 - lr: 0.0034
Epoch 5/20
1141/2980 [==========>...................] - ETA 4:42 - loss: 1.3520
```

Tälle projektille voidaan pystyttää Dockerilla kätevä kehitysympäristökontti ja ladata siihen kaikki tarvittavat työkalut valmiiksi. Tätä varten katso Dockerfile.
