#Q6

def chiffre_mot(cle:list,W:list):
    """Chiffre le mot W à l'aide de la clé cle et renvoie le résultat.
    Arguments : 
    - cle (liste)
    - W (liste)
    """
    somme=0
    for i in range(len(W)):
        somme+=cle[i]*W[i]
    return somme