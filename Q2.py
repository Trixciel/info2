#Q2

def recollage(mots:list):
    """Regroupe les objets des mots en une seule liste
    Arguments :
    - mots (liste de listes)
    """
    message=[]
    for mot in mots:
        for item in mot:
            message.append(item)
    return message