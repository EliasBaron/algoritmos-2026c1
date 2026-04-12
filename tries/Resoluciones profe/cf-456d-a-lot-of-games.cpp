/**
 * Author: Francisco Soulignac
 * Time in CF: 61ms
 */

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

#define SUBMIT

constexpr int WIN = 0;
constexpr int LOSE = 1;

struct Trie {

    struct Node {
        bool elem = false;  // en rigor, no hace falta guardar los elementos
        unordered_map<char, size_t> children;   // char -> node index
    };
    vector<Node> tree;

    Trie()
      : tree(1) //nodo raiz sin elementos
    { }

    // inserta el string s[i:n] en el tree desde el nodo apuntado por n
    void insert(const string& s, size_t i = 0, size_t n = 0) {
        if(i == s.size()) {
            tree[n].elem = true;
        } else {
            auto [it, inserted] = tree[n].children.insert({s[i], tree.size()});
            if(inserted)
                tree.push_back(Node());
            insert(s, i+1, it->second);
        }
    }
};

int main() {
#ifndef SUBMIT
    if(not freopen("in", "r", stdin)) return 1;
    if(not freopen("out", "w", stdout)) return 1;
#endif

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    size_t n, k;
    cin >> n >> k;

    Trie group;
    for(auto i = 0ul; i < n; ++i) {
        string s; cin >> s;
        group.insert(s);
    }

    // Calculamos el estado de forzar una victoria/derrota de cada nodo empezando por las hojas.
    // Afortunadamente, sabemos que un recorrido de group.tree desde ultimo a primero hace el truco
    // porque cada hijo de un nodo aparece despues del nodo
    auto& T = group.tree;
    vector<vector<bool>> forces(2, vector<bool>(T.size(), false));   // forces[x][i] = fuerza el resultado x en el nodo i
    for(auto i = T.size(); i > 0; --i) {
        if(T[i-1].children.empty())
            forces[LOSE][i-1] = true;
        else
        for(auto state : {WIN, LOSE})
            forces[state][i-1] = count_if(T[i-1].children.begin(), T[i-1].children.end(),
                [&](pair<char, size_t> child) {return not forces[state][child.second];}
            ) > 0;    // puede moverse a un estado donde el otro jugador no puede forzar el mismo estado
    }

    if(not forces[WIN][0])
        // Si el primer jugador no puede ganar, entonces el segundo jugador lo hace perder todos los partidos
        cout << "Second\n";
    else if(forces[LOSE][0])
        // Si el primer jugador puede ganar y perder, entonces pierde todos los juegos salvo el ultimo
        cout << "First\n";
    else
        // Finalmente, si al primer jugador le conviene ganar, va a forzar ganar; sino, lo van a forzar a ganar.
        cout << (k % 2 == 1 ? "First\n" : "Second\n");

    return 0;
}
