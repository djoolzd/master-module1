# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import json as js

def process_tweet(fichero_sentimiento, fichero_tweet):
    ##Abrir fichero de sentimientos
    sentimientos= open(fichero_sentimiento)
    ##Initialize an dictionary vacio
    valores={}
    ##Iterate en sentimiento fichero para cargar el array
    for line in sentimientos:
        ##separar al fila por el termino \t to have el termino y el score al otro lado
        term,valor= line.split("\t")
        #cargamiento del dictionary con los valores del txt
        valores[term]=int(valor)
        ##Abrir fichero de tweets
    tweets= open(fichero_tweet)
    ##Bucle para leer el fochero de tweets
    for line_tweets in tweets:
        #probamos de leer la fila coomo docuemtno json
        try:json_tweet=js.loads(line_tweets)
        #Si no conseguimos leer el docuemento como json no hacemos nada
        except: json_tweet=None
        #Testeamos si el atributo text existe si no pasamos a la fila siguiente
        if 'text' not in json_tweet:
            continue
        #recuperamos el atributo text
        tweet_text=json_tweet['text']
        #Inicio del contador a 0
        value=0
        #inicializacion de la lista de palabras no encontradas en el dicionario
        palabras_no_encontradas=[]
        #hacemos un split de la frase contenido en el tweet por espacio
        for word in tweet_text.split(" "):
            #para cada palabra miramos si la encotramos en el dicionario
            if word not in valores:
                #si no la encontramos añadimos la palabra en la lista de palabras no encontrados y pasamos a la palabra siguiente
                palabras_no_encontradas.append(word)
                continue
            #si encontramos la palabro incrementeamos el contador con el valor asiociado
            value=valores[word]+value
        #al final de la bucle hacemos un print del valor asociado al tweet
        print('EL SIGUIENTE TWEET: '+tweet_text+' TIENE UN SENTIMIENTO ASOCIADO DE: '+str(value))
        #hacemos un bucle sobre la lista de palabras no encontradas
        if value != 0:
            for palabra in palabras_no_encontradas:
                #hacemos un print de toda las palabras no encontradas con el valor asociado al tweet
                print(palabra+":"+str(value))
    
process_tweet("D:/Master Big data/Module 1/master-module1/Caso_practico/incoming/dictionnary/Sentimientos.txt","D:/Master Big data/Module 1/master-module1/Caso_practico/incoming/tweets/salida_tweets.txt")   