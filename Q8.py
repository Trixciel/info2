#Q8

def dechiffre_mot(cle:list,C:int):
    """Retrouve le mot chiffré dans C avec la clé cle.
    Arguments :
    - cle (liste)
    - C (entier)
    """
    revcle,revmot=cle[::-1],[]
    for item in revcle:
        if C >= item:
            C-=item
            revmot.append(1)
        else: revmot.append(0)
    mot=revmot[::-1]
    return mot