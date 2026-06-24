
#include <iostream>
#include <vector>
#include <limits>

using namespace std;
using tint = long;

const tint MINF = numeric_limits<tint>::min();
using Graph = vector<vector<pair<tint,tint>>>;

pair<vector<tint>, vector<bool>> dists_from(const Graph& G, tint from) {
    vector<tint> process{from};
    vector<bool> changed(G.size(), false);
    vector<tint> dist(G.size(), MINF);
    dist[from] = 0;
    for(auto i = 0ul; i < G.size() and not process.empty(); ++i) {
        for(auto w : process) changed[w] = false;
        vector<tint> prev;
        swap(prev, process);
        for(auto v : prev) {
            for(auto [w,d] : G[v]) {
                if(dist[w] < dist[v] + d) {
                    dist[w] = dist[v] + d;
                    if(not changed[w]) process.push_back(w);
                    changed[w] = true;
                }
            }
        }
    }
    return {dist, changed};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    tint n, m;
    cin >> n >> m;

    Graph F(n+1);     //neighbor, dist
    Graph B(n+1);

    for(tint e = 0; e < m; ++e) {
        tint v,w,d;
        cin >> v >> w >> d;
        F[v].push_back({w,d});
        B[w].push_back({v,d});
    }

    auto [dist_f, changed_f] = dists_from(F, 1);
    auto [dist_b, changed_b] = dists_from(B, n);


    for(tint v = 1; v <= n; ++v)
    if(changed_f[v] and dist_b[v] != MINF) {
        cout << "-1\n";
        return 0;
    }

    cout << dist_f[n] << '\n';

    return 0;
}
