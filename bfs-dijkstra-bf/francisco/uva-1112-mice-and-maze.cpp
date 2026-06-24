/**
 * Author: Francisco Soulignac
 * Time in UVA: 0s
 */

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

/**
 * Solucion: Dijkstra con las aristas del reves empezando de la salida
 */

constexpr int INF = 1 << 28;

using ii = pair<int, int>;
//cada arista es peso + vecino
using digraph = vector<vector<ii>>;


vector<int> dijkstra(const digraph& D, int from) {
    vector<int> dist(D.size(), INF);
    priority_queue<ii, vector<ii>, greater<ii>> q;
    q.push({0, from});
    while(not q.empty()) {
        auto u = q.top();
        q.pop();
        if(dist[u.second] < INF) continue;
        dist[u.second] = u.first;
        for(auto v : D[u.second]) if(dist[v.second] == INF) {
            q.push({u.first + v.first, v.second});
        }
    }
    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);


    int c,n,m,e,t,u,v,w;
    cin >> c;

    while(c--) {
        cin >> n >> e >> t >> m;

        digraph G(n+1);

        for(int i=0; i < m; ++i) {
            cin >> u >> v >> w;
            G[v].push_back({w,u});
        }

        auto res = dijkstra(G, e);
        cout << count_if(res.begin(), res.end(), [t](int v){return v <= t;}) << '\n';

        if (c) cout << '\n';
    }

    return 0;
}
