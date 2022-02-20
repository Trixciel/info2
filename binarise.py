def binarise(texte : str)-> list :
    """
    renvoie une liste de 0 et de 1, représentation binaire de la chaîne texte
    La liste de sortie a pour longueur 8*len(texte)
    Exemple :
    >>> binarise("A")
    [0, 1, 0, 0, 0, 0, 0, 1]
    >>> binarise("ab")
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]
    """
    
    sequence_binaire = []
    for lettre in texte :
        ascci = ord(lettre)       #code ascii du caractère

        # l'expression format(a,"08b") renvoie une chaine de caractère
        # écriture de a en binaire sur 8 bits        
        sequence_binaire += [ int(digit) for digit in format(ascci,"08b")]
    return sequence_binaire

def debinarise(sequence_binaire : list)-> str :
    """
    réalise l'opération inverse de binarise
    >>> debinarise([0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0])
    'ab'
    """
    # conversion de la liste en une chaîne de caractère de 0 et de 1
    seq_texte = ''.join([str(bit) for bit in sequence_binaire])

    # On va maintenant lire cette chaîne par blocs de taille 8
    n  = len(seq_texte)//8
    texte = ''
    for i in range(n) :
        mot = seq_texte[8*i: 8*i+8]
        ascci = int(mot, base=2)     # conversion en entier 
        car = chr(ascci)             # la fonction chr renvoie le caractère correspondant
        texte += car 
    return texte   
