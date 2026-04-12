/**
 * Author: Francisco Soulignac
 * Time in UVA: 0s
 *
 * Input: secuencia de pares pares p_1, ..., p_n con p_i = (c_i, d_i)
 * Output: verificar si {p_i + d_i} = {1,...,n}.  En caso afirmativo, imprimir
 * la secuencia [c_{p_i + d_i}] para la secuencia p_i+d_i ordenada.  En caso negativo,
 * imprimir -1
 * Restricciones: n \lqe 1000, 1 \leq c \leq 10000 y -10^5 < d_i < 10^6
 *
 * Solucion: construir un diccionario con claves [0,...,n-1] donde la i-esima posicion
 * tiene a c_j cuando p_j + d_j = i.  Si es posible cubrir todas las posiciones,
 * imprimir la secuencia ordenada
 * Complejidad: O(n)
 * Dificultad: 1
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

using tint = int;

int main() {
    
    tint n;
    while(cin >> n, n) {
        
        vector<tint> pole(n, -1);
        for(tint i = 0; i < n; ++i) {
            tint car, delta, start;
            cin >> car >> delta;
            start = i + delta;
            if(start >= 0 and start < n) pole[start] = car;
        }

        if(none_of(pole.begin(), pole.end(), [](tint p){return p == -1;})) {
            copy(pole.begin(), pole.end()-1, ostream_iterator<tint>(cout, " ")); cout << pole.back();
        } else {
            cout << -1;
        }
        cout << '\n';   
    }
    
    return 0;
}
