#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int N, M;

  while (cin >> N >> M && (N != 0 || M != 0))
  {
    vector<int> jack(N), jill(M);

    for (int k = 0; k < N; k++)
      cin >> jack[k];
    for (int k = 0; k < M; k++)
      cin >> jill[k];

    int coincidences = 0;
    int i = 0, j = 0;

    while (i < N && j < M)
    {
      if (jack[i] == jill[j])
      {
        coincidences++;
        i++;
        j++;
      }
      else if (jack[i] < jill[j])
      {
        i++;
      }
      else
      {
        j++;
      }
    }

    cout << coincidences << endl;
  }

  return 0;
}