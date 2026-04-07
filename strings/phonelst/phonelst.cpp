/*
Phone List
Primero entendamos bien el problema. Tenés una lista de números de teléfono y tenés que determinar si es consistente, lo que significa que ningún número debe ser prefijo de otro.
En el ejemplo, 911 es prefijo de 91125426 (el número de Bob), entonces la lista no es consistente porque al marcar el número de Bob, la central te redirige al 911 antes de que termines de marcar.
*/

#include <string>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

struct TrieNode
{
  TrieNode *childrens[10];
  bool isEnd;
  int cantHijos; // ← nuevo

  TrieNode()
  {
    isEnd = false;
    cantHijos = 0;
    for (int i = 0; i < 10; i++)
      childrens[i] = nullptr;
  }
};

bool insert(TrieNode *root, string number)
{
  TrieNode *actual = root;

  for (char c : number)
  {
    int idx = c - '0'; // ojo: usamos '0' en vez de 'a' porque son dígitos

    if (actual->isEnd == true)
      return false; // caso 1: este nodo es fin de un número anterior → inconsistente

    if (actual->childrens[idx] == nullptr)
    {
      actual->childrens[idx] = new TrieNode();
      actual->cantHijos++;
    }

    actual = actual->childrens[idx];
  }

  // caso 2: terminamos de insertar, ¿el nodo final ya tiene hijos?
  // ¿cómo detectarías eso?
  actual->isEnd = true;

  return actual->cantHijos == 0;
}

int main()
{
  int T;
  cin >> T;
  while (T--)
  {
    int N;
    cin >> N;
    vector<string> numberList(N);

    for (int k = 0; k < N; k++)
      cin >> numberList[k];

    TrieNode *root = new TrieNode();
    bool consistente = true;

    for (string number : numberList)
    {
      if (!insert(root, number))
      {
        consistente = false;
        break;
      }
    }
    cout << (consistente ? "YES" : "NO") << endl;
  }
}