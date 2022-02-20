#Q7

from Q6 import chiffre_mot #On utilise la fonction de la Q6, tout sera dans le même fichier python, donc ne mettez pas ça.

def chiffre_message(cle:list,message:list):
    """Renvoie le message chiffré à l'aide de la clé fournie:
    Arguments :
    - cle (liste)
    - message (liste)
    """
    message_chiffre=[chiffre_mot(cle,mot) for mot in message]
    return message_chiffre