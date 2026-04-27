/**
 * Author: Francisco Soulignac
 * Time in UVA: 0
 */

#include <iostream>
#include <array>

using namespace std;

//Si bien se pueden agregar podas, no parece necesario por la cantidad de casos

array<int, 20> duration;  //odio las variables globables, pero evitan pasar parametros;
int N, tracks;

pair<int, int> backtracking(int partial = 0, int next = 0, int value = 0) {

    if(value > N) return make_pair(0, 0);
    if(next == tracks) return make_pair(partial, value);
    
    pair<int, int> left  = backtracking(partial, next+1, value);
    pair<int, int> right = backtracking(partial | (1 << next), next+1, value + duration[next]);
    
    return left.second > right.second ? left : right;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    while(cin >> N) {
        cin >> tracks;
        for(int i = 0; i < tracks; ++i) {
            cin >> duration[i];
        }
        
        pair<int, int> best = backtracking();
        for(int i = 0; i < tracks; ++i) {
            if(best.first & (1 << i)) cout << duration[i] << ' ';
        }
        cout << "sum:" << best.second << '\n';
    }
}
