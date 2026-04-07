/*
Se recibe primero un T detallando la cantidad de test casos.
Luego, por cada test cases, en una linea dos enteros N y M, siendo N tamaño de la primer lista y M el tamaño de la segunda lista.

Lo que se pide es, devolver la cantidad de elementos a eliminar para que, en cada lista queden los MISMOS elementos, sin importar el orden.

OBS:
Se tiene lista n y lista m, como estas son desordenadas, no puedo hacer la estrategía de doble puntero.

Tendría que basicamente, contar las diferencias de la primer lista respecto a la segunda, y viceversa, solamente agregando las diferencias no agregadas. Pero eso me implicaría recorrer enteramente las dos listas siendo el costo N + M, encima luego, preguntar para cada elemento si es contenido en la otra lista y así, para luego, devolver el size del array .. encima se pueden repetir elementos, y si en la otra lista está contenido una vez, debería de eliminar el repetido ...
*/

#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin >> T;
  while (T--)
  {
    int N, M;

    while (cin >> N >> M && (N != 0 || M != 0))
    {
      vector<int> listA(N), listB(M);

      for (int k = 0; k < N; k++)
        cin >> listA[k];
      for (int k = 0; k < M; k++)
        cin >> listB[k];

      map<int, int> freq1, freq2;

      int i = 0, j = 0;

      while (i < N)
      {
        freq1[listA[i]]++;
        i++;
      }
      while (j < M)
      {
        freq2[listB[j]]++;
        j++;
      }

      // se busca cada clave de freq1 en freq2 y se queda con el minimo entre los dos valores, con eso tenemos el total de los elementos a quedarnos. Luego hacemos el total de elementos - elementos a quedarnos, lo cual nos dará el total de los elementos a restar.

      int elementsToKeep = 0;

      for (auto &par : freq1)
      {
        int clave = par.first;
        int cantidad = par.second;
        elementsToKeep += min(cantidad, freq2[clave]);
      }

      int elementsToRemove = (M + N) - (elementsToKeep * 2);

      cout << elementsToRemove << endl;
    }

    return 0;
  }
}