// Implementacion de clique_number10() en C++ por eficiencia
#include <bitset>
#include <vector>
#include <numeric>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

// Grafos con hasta 128 vertices
const size_t MAX_N = 256;
using Graph = vector<bitset<MAX_N>>;
using VertexSet = bitset<MAX_N>;
using Vertex = size_t;

pair<size_t, VertexSet> clique_number(const Graph& G) {

    vector<Vertex> vertices(G.size(), 0);
    iota(vertices.begin(), vertices.end(), 0);
    sort(vertices.begin(), vertices.end(), [&G](Vertex v, Vertex w) {
        return G[v].count() < G[w].count();
    });

    auto heuristic = [&G,&vertices]() -> VertexSet {
        VertexSet res;
        vector<Vertex> V = vertices, W;
        while(not V.empty()) {
            auto v = V.back();
            V.pop_back();
            res.set(v);

            for(auto w : V)
            if(G[v].test(w))
                W.push_back(w);

            swap(V, W);
            W.clear();
        }
        return res;
    };

    auto upper_bound = [&G](const vector<Vertex>& V, size_t i) -> size_t {

        vector<VertexSet> ind;
        for(auto j = V.size(); j > i; --j) {
            auto v = V[j-1];
            auto I = find_if(ind.begin(), ind.end(), [&G,v](const VertexSet& W) {return (G[v] & W).none();});
            if(I == ind.end())
                ind.push_back(VertexSet().set(v));
            else
                I->set(v);
        }
        return ind.size();
    };


    auto best = heuristic();
    auto best_count = best.count();
    VertexSet parcial;
    size_t parcial_count = 0;

    function<void(const vector<Vertex>&)> backtracking = [&](const vector<Vertex>& V) {
        if (V.empty()) {
            best = parcial;
            best_count = parcial_count;
            return;
        }

        for(auto i = 0ul; i < V.size(); ++i) {
            if(parcial_count + upper_bound(V, i) <= best_count)
                return;

            parcial.set(V[i]);
            parcial_count += 1;

            vector<Vertex> W;
            for(auto v : V)
            if(G[V[i]].test(v))
                W.push_back(v);
            backtracking(W);

            parcial_count -= 1;
            parcial.reset(V[i]);
        }
    };

    backtracking(vertices);
    return {best_count, best};
}

//el input es como aca: https://open.kattis.com/problems/maxclique
int main()
{
    size_t n, m; cin >> n >> m;

    Graph G(n);
    for(auto e = 0ul; e < m; ++e) {
        Vertex v, w; cin >> v >> w;
        G[v].set(w);
        G[w].set(v);
    }

    auto res = clique_number(G);
    cout << res.first << '\n';
    return 0;
}
