#Q9
from Q8 import dechiffre_mot #On utilise la fonction de la Q8, ne pas mettre dans le rendu final.

def dechiffre_message(cle:list,message_chiffre:list):
    """Renvoie le message déchiffré avec la clé cle.
    Arguments :
    - cle (liste)
    - message_chiffre (liste)
    """
    message_dechiffre=[dechiffre_mot(cle,mot) for mot in message_chiffre]
    return message_dechiffre