
import sys
from math import sqrt

def empty(iterable):
    try:
        next(iterable)
    except StopIteration:
        return True
    return False

def clique_number1(G):
    #Version backtracking simulando fuerza bruta.
    def is_clique(parcial):
        for v in range(0, len(parcial)): 
            for w in range(v+1, len(parcial)):
                if G[parcial[v]][parcial[w]] == 0: 
                    return False
        return True
    
    def backtracking(parcial, v):
        if v == len(G): return len(parcial) if is_clique(parcial) else -len(G)
        
        left = backtracking(parcial, v+1)
        right = backtracking(parcial + [v], v+1)
        
        return max(left, right)
    
    return backtracking(list(), 0)

def clique_number2(G):
    #poda por factibilidad
    def is_clique(parcial):
        for v in range(0, len(parcial)): 
            for w in range(v+1, len(parcial)):
                if G[parcial[v]][parcial[w]] == 0: 
                    return False
        return True
    
    def backtracking(parcial, v):
        if not is_clique(parcial): return -len(G)
        if v == len(G): return len(parcial)
        
        left = backtracking(parcial, v+1)
        right = backtracking(parcial + [v], v+1)
        
        return max(left, right)
    
    return backtracking(list(), 0)

def clique_number3(G):
    #Idem clique_number2, pero con una implementacion mejor pensada.
    #Reemplazamos el test de is_clique de O(parcial^2) en cada nodo del arbol, porque es muy caro.
    #En su lugar, solo chequeamos que el nuevo nodo sea adyacente a todos los anteriores O(parcial)
    def is_clique(parcial, v):
        for w in parcial:
            if G[v][w] == 0: 
                return False
        return True
    
    def backtracking(parcial, v):
        if v == len(G): return len(parcial)
        
        left = backtracking(parcial, v+1)
        right = 0 if not is_clique(parcial, v) else backtracking(parcial + [v], v+1)
        
        return max(left, right)
    
    return backtracking(list(), 0)

def clique_number4(G):
    #Idem clique_number3, pero en lugar de copiar la solucion parcial en cada paso, vamos
    #a mantener el estado haciendo push y pop
    #Notar que parcial, al igual que G, es una variable "global"
    def is_clique(v):
        for w in parcial:
            if G[v][w] == 0: 
                return False
        return True
    
    def backtracking(v):
        if v == len(G): return len(parcial)
        
        best = backtracking(v+1)
        if(is_clique(v)):
            parcial.append(v)
            best = max(best, backtracking(v+1))
            parcial.pop()
            
        return best
    
    parcial = list()
    return backtracking(0)

def clique_number5(G):
    #En este caso, ademas de la factibilidad, vamos a poner una poda boba que chequee que tenemos
    #una cantidad de vertices suficientes para superar a la mejor clique vista hasta el momento
    def is_clique(v):
        for w in parcial:
            if G[v][w] == 0: 
                return False
        return True
    
    def backtracking(v, best):
        if len(parcial) + len(G) - v <= best: return best
        if v == len(G): return len(parcial)
        
        best = max(best, backtracking(v+1, best))
        if(is_clique(v)):
            parcial.append(v)
            best = max(best, backtracking(v+1, best))
            parcial.pop()
            
        return best
    
    parcial = list()
    return backtracking(0, 0)
    
def clique_number6(G):
    #Idem clique_number5 pero vamos guardando los vertices que son factibles de ser agregados
    #(lo hacemos por copia para simplificar).  Notar que ya no necesitamos saber si es clique
    
    def backtracking(V, best):
        if len(parcial) + len(V) <= best: return -len(G)
        if len(V) == 0: return len(parcial)
        
        v = V[0]
        best = max(best, backtracking(V[1:], best))
        parcial.append(v)
        best = max(best, backtracking([w for w in V if v != w and G[v][w] == 1], best))
        parcial.pop()
            
        return best
    
    parcial = list()
    vertices = range(0, n)
    return backtracking(vertices, 0)
    
def clique_number7(G):
    #Idem clique_number6, pero ordenamos los vertices de acuerdo a su grado, de menor a mayor
    
    def backtracking(V, best):
        if len(parcial) + len(V) <= best: return -len(G)
        if len(V) == 0: return len(parcial)
        
        v = V[0]
        best = max(best, backtracking(V[1:], best))
        parcial.append(v)
        best = max(best, backtracking([w for w in V if v != w and G[v][w] == 1], best))
        parcial.pop()
            
        return best
    
    parcial = list()
    vertices = list(range(0, n))
    vertices.sort(key=lambda v: sum(G[v]))
    return backtracking(vertices, 0)

def clique_number8(G):
    #clique_number7 pero con heuristica inicial de quedarse siempre con el de mayor grado que genere una clique
    #(vendria a ser como la rama mas a la derecha del arbol de backtracking)
    def heuristic(V):
        #requiere que los vertices esten ordenados de menor a mayor grado
        #no me voy a esforzar mucho, voy a hacer recursion
        return 0 if len(V) == 0 else 1 + heuristic([w for w in V if w != V[-1] and G[V[-1]][w] == 1])
        
    def backtracking(V, best):
        if len(parcial) + len(V) <= best: return best
        if len(V) == 0: return len(parcial)
        
        v = V[0]
        best = max(best, backtracking(V[1:], best))
        #if(is_clique(v)):
        if(True):
            parcial.append(v)
            best = max(best, backtracking([w for w in V if v != w and G[v][w] == 1], best))
            parcial.pop()
            
        return best
    
    parcial = list()
    vertices = list(range(0, n))
    vertices.sort(key=lambda v: sum(G[v]))
    #print(heuristic(vertices), end=' ')
    return backtracking(vertices, heuristic(vertices))


def clique_number9(G):
    #Mejoramos la cota para la poda.  En lugar de considerar que todos los vertices de V pueden agregarse
    #vamos a buscar una cota superior para la clique maxima
    #Para eso, vamos a partir V en conjuntos indeptes V1, ..., Vk.  
    #Claramente, la maxima clique es a lo sumo k, porque puede tener a lo sumo
    #1 vertice de cada conjunto.  
    def heuristic(V):
        return 0 if len(V) == 0 else 1 + heuristic([w for w in V if w != V[-1] and G[V[-1]][w] == 1])
    
    def upper_bound(V):
        ind = [list() for i in range(0, len(V))]
        for v in reversed(V):
            next(I for I in ind if empty(w for w in I if G[v][w] == 1)).append(v)
        return sum(1 for I in ind if len(I) > 0)
    
    def backtracking(V, best):
        if len(parcial) + upper_bound(V) <= best: return best
        if len(V) == 0: return len(parcial)
        
        v = V[0]

        best = max(best, backtracking(V[1:], best))
        parcial.append(v)
        best = max(best, backtracking([w for w in V if v != w and G[v][w] == 1], best))
        parcial.pop()
            
        return best
    
    parcial = list()
    vertices = list(range(0, n))
    vertices.sort(key=lambda v: sum(G[v]))
    return backtracking(vertices, heuristic(vertices))

def clique_number10(G):
    #Esta es la implementacion de clique_number9, siguiendo un esquema mas parecido al que se usa para backtrackings
    #de permutaciones.  La idea es reducir la cantidad de nodos, comprimiendo las aristas que se usan para bajar por
    #el no agreado.
    def heuristic(V):
        return 0 if len(V) == 0 else 1 + heuristic([w for w in V if w != V[-1] and G[V[-1]][w] == 1])
    
    def upper_bound(V):
        ind = [list() for i in range(0, len(V))]
        for v in reversed(V):
            next(I for I in ind if empty(w for w in I if G[v][w] == 1)).append(v)
        return sum(1 for I in ind if len(I) > 0)
    
    def backtracking(V, best):
        if len(V) == 0: return len(parcial)

        for i in range(0, len(V)):
            #por qué va aca la cota?
            if len(parcial) + upper_bound(V[i:]) <= best: return best
            parcial.append(V[i])
            best = max(best, backtracking([w for w in V[i+1:] if G[V[i]][w] == 1], best))
            parcial.pop()
            
        return best
    
    parcial = list()
    vertices = list(range(0, n))
    vertices.sort(key=lambda v: sum(G[v]))
    return backtracking(vertices, heuristic(vertices))
    

def read_line():
    line = next(sys.stdin).strip()
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

#Voy a usar el input de UVA 193, que es el complemento de clique (i.e., conjunto independiente)
if __name__ == "__main__":
    n,m = map(int, read_line().split(" "))
    G = [[0]*n for i in range(0, n)]


    for e in range(0, m):
        v,w = map(int, read_line().split(" "))
        G[v][w] = 1
        G[w][v] = 1

    print(clique_number10(G))
