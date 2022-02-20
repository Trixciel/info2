#Q10
import binarise as bn #Vous n'êtes pas obligé de le faire, si par exemple, vous avez copié-collé la fonction dans votre programme, mais je ne l'ai pas fait.
from Q1 import decoupage
from Q2 import recollage
from Q5 import genere_cle
from Q7 import chiffre_message
from Q9 import dechiffre_message #Même chose que pour tous les autres imports de questions, ne mettez pas ca dans votre rendu final.


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