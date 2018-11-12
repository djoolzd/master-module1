# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import json as js

##Abrir fichero de sentimientos
sentimientos= open("D:/Master Big data/Module 1/master-module1/Caso_practico/incoming/dictionnary/Sentimientos.txt")
##Initialize an dictionary vacio
valores={}
##Iterate en sentimiento fichero para cargar el array
for line in sentimientos:
##separar al fila por el termino \t to have el termino y el score al otro lado
    term,valor= line.split("\t")
#cargamiento del dictionary con los valores del txt
    valores[term]=int(valor)
    
###(valores.items())
    
##Abrir fichero de tweets
tweets= open("D:/Master Big data/Module 1/master-module1/Caso_practico/incoming/tweets/salida_tweets.txt")
##Initialize an dictionary vacio
tweets_array={}
for line_tweets in tweets:
    try:json_tweet=js.loads(line_tweets)
    except: json_tweet=None
    if 'text' not in json_tweet:
        continue
    tweet_text=json_tweet['text']
    print(tweet_text)
    