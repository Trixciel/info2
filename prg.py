import random,binarise as bn

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

#Q3

def inverse_modulo(A:int,N:int):
    """Renvoie l'inverse de A modulo N
    Arguments :
    - A (entier)
    - N (entier)
    """
    for B in range(N):
        if (A*B)%N==1: 
            return B

#Q4

#J'ai réussi à la faire marcher, mais ca m'a couté 1h par jour pendant une semaine, donc vous l'aurez pas :P
#De tte façon elle est facultative...

#Q5

def genere_cle(n:int):
    """Génère une liste contenant une séquence super-croissante de taille n
    Arguments :
    - n (entier)
    """
    liste,somme=[],0
    for i in range(n):
        if not len(liste): newitem=random.randrange(0,10) #Les rk sont des nombres pseudo-random de 1 à 9
        else: newitem=somme+random.randrange(0,10) #J'aurais idéalement préféré utiliser secrets, mais random est bien plus populaire.
        somme+=newitem
        liste.append(newitem)
    return liste
    
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

#Q7

def chiffre_message(cle:list,message:list):
    """Renvoie le message chiffré à l'aide de la clé fournie:
    Arguments :
    - cle (liste)
    - message (liste)
    """
    message_chiffre=[chiffre_mot(cle,mot) for mot in message]
    return message_chiffre

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

#Q9

def dechiffre_message(cle:list,message_chiffre:list):
    """Renvoie le message déchiffré avec la clé cle.
    Arguments :
    - cle (liste)
    - message_chiffre (liste)
    """
    message_dechiffre=[dechiffre_mot(cle,mot) for mot in message_chiffre]
    return message_dechiffre

#Q10

def transmission_sac_a_dos():
    cle=genere_cle(16) #La clé est aléatoire, donc le chiffrement n'est jamais le même
    #Envoi (Chiffrement)
    message_envoye="J'aime le chiffrement symétrique"
    message_envoye_bin=bn.binarise(message_envoye)
    message_envoye_16=decoupage(message_envoye_bin,16)
    message_chiffre=chiffre_message(cle,message_envoye_16)
    #Récéption (Déchiffrement)
    message_dechiffre_16=dechiffre_message(cle,message_chiffre)
    message_dechiffre_bin=recollage(message_dechiffre_16)
    message_recu=bn.debinarise(message_dechiffre_bin)
    return f"Clé : {cle}\n(Note : La clé est choisie aléatoirement à chaque fois, donc le message chiffré n'est jamais le même)\nMessage envoyé : {message_envoye}\nMessage chiffré : {message_chiffre}\nMessage reçu : {message_recu}"
    #Franchement, le return, mettez ce que vous voulez dedans, j'ai mit ça, mais bon, d'autres choses conviennent...

#Q11

#a
P=genere_cle(8)

#b
#Mettez les valeurs que vous voulez ici, du moment qu'ils respectent la condition.
N = ...
A = ...

#c
N_auto=0
for pi in P:
    N_auto+=pi
#Ici, N_auto est égal à la somme des pi

N_auto+=random.randrange(1,6904)
#N_auto est donc > à la somme des pi, on peut remplacer le nombre aléatoire par 1, ca marche aussi

def premier_avec_N(N):
    for i in range(2,N):
        premier_bool=True
        for j in range(2,N):
            if (i*j)%N==0:
                premier_bool=False
        if premier_bool:
            return i
    return None

A_auto=premier_avec_N(N_auto)
#On trouve un entier A_auto premier avec N_auto

#Remarque : à partir de maintenant, les opérations seront effectuées 2 fois:
#1 fois avec A/N choisis au hasard, et 1 fois avec les valeurs prédéfinies

#d

#Nombres choisis manuellement
cle_publique=[]
for pi in P:
    bpi=(A*pi)%N
    cle_publique.append(bpi)
    
#Nombres choisis algorithmiquement
cle_publique_auto=[]
for pi in P:
    bpi_auto=(A_auto*pi)%N
    cle_publique_auto.append(bpi_auto) #Valeur aléatoire


#e
message="Le chiffrement asymétrique me rend fou"
message_bin=bn.binarise(message)
message_8=decoupage(message_bin,8)
message_chiffre_publique=chiffre_message(cle_publique,message_8) #Valeur manuelle

message_chiffre_publique_auto=chiffre_message(cle_publique_auto,message_8) #Valeur algorithmique

#f
def decode_Merkle_Hellman(cle_privee:tuple,message_chiffre:list):
    """Renvoie le message déchiffré avec la clé privée.
    Arguments :
    - cle_privee (tuple)
    - message_chiffre (liste)
    """
    (A,N,P)=cle_privee
    B=inverse_modulo(A,N)
    liste,texte=[],""
    for C in message_chiffre:
        p=(B*C)%N
        x=dechiffre_mot(P,p)
        clair=bn.debinarise(x)
        liste+=clair
    for lettre in liste:
        texte+=lettre
    return texte
