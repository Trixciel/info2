#Q5
import random

def genere_cle(n:int):
    """Génère une liste contenant une séquence super-croissante de taille n
    Arguments :
    - n (entier)
    """
    liste,somme=[],0
    for i in range(n):
        if not len(liste): newitem=random.randrange(1,10) #Les rk sont des nombres pseudo-random de 1 à 9
        else: newitem=somme+random.randrange(1,10) #J'aurais idéalement préféré utiliser secrets, mais random est bien plus populaire.
        somme+=newitem
        liste.append(newitem)
    return liste
