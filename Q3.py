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