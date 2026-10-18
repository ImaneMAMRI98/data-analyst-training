
import random

def generate_random_array(debug=False, N=21):
    """Renvoie un tableau contenant toutes les valeurs entières de 0 (inclus)
    à N (exclus) rangées dans un ordre aléatoire

    Args:
        debug (boolean): quand debug est vrai, la fonction renvoie toujours le
                         même tableau afin de simplifier le débogage de vos
                         algorithmes de tri
        N (int): la taille du tableau à renvoyer

    Returns:
        list[int]: un tableau d'entiers, de taille N, non ordonné
    """

    if debug:
        return [3, 9, 7, 1, 6, 2, 8, 4, 5, 0]

    array = list(range(0, N))
    random.shuffle(array)

    return array

# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j):
    """Échange la place de deux éléments dans un tableau"""
    tab[i] , tab[j] = tab[j] , tab[i]



# ---------------
# Tris classiques
# ---------------
def bubble_sort(A):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""
    #for i in reversed(range(1,len(A))):
    for i in range(len(A)-1,0,-1):
        for j in range(0,i):
            if A[j+1] < A[j]:
                swap(A,j+1 ,j)
    return (A)


def insertion_sort(A):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    n = len(A)
    for i  in range(1, n):
        x = A[i]
        j = i
        while ( j > 0 and A[j-1]>x):
            A[j] = A[j-1]
            j -=1
        A[j] = x
    return (A)


def selection_sort(A):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    n = len(A)
    for i in range(n-1):
        min  = i
        for j in range(i+1,n):
            if (A[j] < A[min]):
                min = j
        if min != i:
            swap(A, i,min)

    return(A)

# --------------
# Tris récursifs
# --------------



def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""
    n= len(tab)
    if n<=1:
        return tab
    millieu = n//2
    gauche = tab[ :millieu]
    droite = tab[millieu :]
    gauche_triee = merge_sort(gauche)
    droite_triee = merge_sort(droite)
    return fusionner(gauche_triee,droite_triee)


def fusionner(tab1,tab2):
    resultat = []
    while (len(tab1) > 0 and len(tab2) > 0):
        if tab1[0] <= tab2[0]:
            x = tab1.pop(0)
            resultat.append(x)
        else:
            x = tab2.pop(0)
            resultat.append(x)
    while (len(tab1) > 0):
        x = tab1.pop(0)
        resultat.append(x)
    while (len(tab2) > 0):
        x = tab2.pop(0)
        resultat.append(x)
    return resultat


def quick_sort(tab, first, last):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées. L'intelligence se trouve
    dans la division du tableau."""
    if first < last:
        index_pivot = partitionner(tab, first, last)
        quick_sort(tab, first, index_pivot-1)
        quick_sort(tab, index_pivot+1, last)
    return tab
        
def partitionner(tab, first, last):
    pivot = tab[last]
    index_frontiere = first -1
    for j in range(first, last):
        if tab[j]<=pivot:
            index_frontiere +=1
            swap(tab,index_frontiere,j)
    swap(tab,index_frontiere+1,last)
    return(index_frontiere+1)
    
