#Q1

def decoupage(message:list,taille:int):
    """Decoupe la liste message en sous-parties de contenant taille éléments
    Arguments :
    - message (liste)
    - taille (entier) 
    """
    final,temp=[],[]
    for item in message:
        temp.append(item)
        if len(temp)==taille:
            final.append(temp)
            temp=[]
    if temp != []: final.append(temp) #On oublie pas d'ajouter la liste temporaire à final, sauf si elle est vide.
    return final
