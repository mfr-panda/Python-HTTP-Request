#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
exemple de requete http avec loop
et gestion des erreurs.

Si le serveur ne repond pas avec
un code 2xx (codes ok), on recommence

auteur : panda - FabLac

'''

import requests

# url du serveur
url = 'http://192.168.1.1/test'

# variable pour controler la boucle en fonction du code retour de la requete
status_req = 0

# tant que la réponse de la requete est différente de 2xx, on envoie la requete
while not status_req // 100 == 2 :
    try :
        reponse = requests.get(url)
        status_req = reponse.status_code
        print(status_req)

    except requests.exceptions.RequestException as e:
        # si erreur de serveur, connexion ou reseau, on catche l'exception et on recommence la boucle
        print(str(e))
        status_req = 0
    

