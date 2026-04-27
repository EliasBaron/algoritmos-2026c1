#include <iostream>
#include <vector>

using namespace std;

void hanoi(int count, int from, int middle, int to, vector<pair<int, int>>* moves) {
    if(count == 0) return;
    hanoi(count-1, from, to, middle, moves);
    moves->push_back({from, to});
    hanoi(count-1, middle, from, to, moves);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    vector<pair<int, int>> moves;
    hanoi(n, 1, 2, 3, &moves);

    cout << moves.size() << '\n';
    for(auto [f, t] : moves) cout << f << " " << t << '\n';

    return 0;
}
