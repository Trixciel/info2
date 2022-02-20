#Q11
import random, binarise as bn
from Q1 import decoupage
from Q3 import inverse_modulo
from Q5 import genere_cle
from Q7 import chiffre_message
from Q8 import dechiffre_mot #Idem, ne mettez pas ça dans le programme final

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

for A_auto in range(2,N_auto):
    if N_auto%A_auto!=0: break
#On trouve le plus petit entier qui n'est pas un diviseur de N_auto, il est donc premier avec N_auto
#(Leur PGCD vaut forcément 1, d'ou la relation du dessus)

#Remarque : à partir de maintenant, les opérations seront effectuées 2 fois:
#1 fois avec A/N choisis au hasard, et 1 fois avec les valeurs prédéfinies

#d
cle_publique,cle_publique_auto=[],[]
for pi in P:
    bpi=(A*pi)%N
    cle_publique.append(bpi) #Valeur définie
    bpi_auto=(A_auto*pi)%N
    cle_publique_auto.append(bpi_auto) #Valeur aléatoire

#e
message="Le chiffrement asymétrique me rend fou"
message_bin=bn.binarise(message)
message_8=decoupage(message_bin,8)
message_chiffre_publique=chiffre_message(cle_publique,message_8) #Valeur définie
message_chiffre_publique_auto=chiffre_message(cle_publique_auto,message_8) #Valeur aléatoire

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