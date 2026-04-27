
import networkx as nx
import random
import itertools

def save(G, name):
    with open(name, "w") as f:
        f.write(f"{G.number_of_nodes()} {G.number_of_edges()}\n")
        for u, v in G.edges():
            f.write(f"{u} {v}\n")
        f.close()
    print(f"Generado {name}: N={G.number_of_nodes()}, M={G.number_of_edges()}")


def generate_kneser(n, k):
    nodes = list(itertools.combinations(range(n), k))
    G = nx.Graph()
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if not (set(nodes[i]) & set(nodes[j])):
                G.add_edge(i, j)
    return G

def generate_johnson(n, k, delta):
    nodes = list(itertools.combinations(range(n), k))
    G = nx.Graph()
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if len(set(nodes[i]) & set(nodes[j])) == delta:
                G.add_edge(i, j)
    return G

def generate_paley(q):
    G = nx.Graph()
    G.add_nodes_from(range(q))

    residuos = set()
    for i in range(1, q):
        residuos.add((i * i) % q)

    for u in range(q):
        for v in range(u + 1, q):
            diff = (u - v) % q
            if diff in residuos:
                G.add_edge(u, v)
    return G


if __name__ == "__main__":

    # Grafos de Erdos
    N = [10,20,30,40,50,60,70]
    P = [0.01, 0.1, 0.3, 0.5, 0.8, 0.99]
    k = 10
    for n in N:
        for i in range(0,k):
            for p in P:
                G = nx.fast_gnp_random_graph(n,p,10) #siempre la misma semilla
                save(G, f"test-{n}-{p}-{i}.erdos")

        # CASE 1: Hidden Clique (Grafo ralo con una clique grande escondida)
        # Esto confunde a las heurísticas de coloreo
        G_hidden = nx.fast_gnp_random_graph(n, 0.25)
        clique_nodes = random.sample(range(n), n//3) # Plantamos una de n//3
        for i in range(len(clique_nodes)):
            for j in range(i + 1, len(clique_nodes)):
                G_hidden.add_edge(clique_nodes[i], clique_nodes[j])
        save(G_hidden, f"test-hidden-{n}.special")

        # CASE 2: Complemento de un grafo ralo (Grafo muy denso)
        # Aquí el backtracking sufre si no tiene buena poda
        G_sparse = nx.fast_gnp_random_graph(n, 0.1)
        G_dense = nx.complement(G_sparse)
        save(G_dense, f"test-dense-{n}.special")

        # CASE 3: Brockington-like (Grafos con grados muy similares)
        # Son famosos en el benchmark DIMACS por ser difíciles
        # Generamos un grafo donde casi todos los nodos tienen el mismo grado
        G_reg = nx.random_regular_graph(d=n//2, n=n)
        save(G_reg, f"test-regular-{n}.special")

        # CASE 4: Peor caso para coloreo (Grafo completo partido)
        # Un grafo que es la unión de varias cliques pequeñas disjuntas
        G_multi = nx.disjoint_union_all([nx.complete_graph(n//4) for _ in range(4)])
        save(G_multi, f"test-multi-clique-{n}.special")

        # CASE 10: Grafo de Turán T(100, 5)
        # Es el grafo con más ejes que NO tiene una clique de tamaño 6.
        # N=100. Clique max = 5. Muy denso (M ~ 4000).
        G_turan = nx.turan_graph(n, 5)
        save(G_turan, f"test-turan-{n}-5.special")

        # CASE 7: Complemento de un Ciclo Largo (C_100)
        # N=100. Clique max es 50. Muchísimas ramas de backtracking.
        C = nx.cycle_graph(n)
        G_c = nx.complement(C)
        save(G_c, f"test-comp-cycle-{n}.special")


    # CASE 5: Kneser(7, 2) -> N=21, M=105. Famoso porque su clique max es 3
    # pero el coloreo suele dar mucho más alto (engaña la poda).
    G_k = generate_kneser(7, 2)
    save(G_k, "test-kneser-21.special")

    # CASE 6: Johnson(8, 4, 2) -> N=70, M=1050.
    # Muy denso y simétrico. Nodos tienen grado 30.
    G_j = generate_johnson(8, 4, 2)
    save(G_j, "test-johnson-70.special")

    # CASE 7: Complemento de un Ciclo Largo (C_100)
    # N=100. Clique max es 50. Muchísimas ramas de backtracking.
    C = nx.cycle_graph(100)
    G_c = nx.complement(C)
    save(G_c, "test-comp-cycle-100.special")

    # CASE 8: El Paley-61 es denso (1830 ejes posibles, tiene 915)
    # Su clique máxima es 5.
    G_paley = generate_paley(61)
    save(G_paley, "test-paley-61.special")

    # CASE 9: Grafo de mycielski
    G_myc = nx.mycielski_graph(6)
    save(G_myc, "test-mycielski-95.special")

    # CASE 10: Grafo de Turán T(100, 5)
    # Es el grafo con más ejes que NO tiene una clique de tamaño 6.
    # N=100. Clique max = 5. Muy denso (M ~ 4000).
    G_turan = nx.turan_graph(100, 5)
    save(G_turan, "test-turan-100-5.special")


