// #include <iostream>
// #include <vector>

// using namespace std;
// using tint = long;

// const tint INF = 1e6 + 1;

// long main()
// {
//   size_t n;
//   long k;
//   cin >> n >> k;

//   v.assign(n, 0);
//   p.assign(n, 0);

//   for (auto &e : v)
//     cin >> e;
//   for (auto &e : p)
//     cin >> e;
// }

// long mochila(size_t i, long k)
// {
//   if (k == 0 or i == 0)
//     return 0;
//   if (k < 0)
//     return -INF;
//   if (M[i, k] == NULL)
//   {
//     M[i, k] = max(mochila(i - i, k), v[i - 1] + mochila(i - 1, k - p(i - 1)))
//   }
//   return M[i, k]
// }

#include <iostream>
#include <vector>
#include <map>

using namespace std;
using tint = long;

const tint INF = 1e6 + 1;

vector<tint> v, p;
map<pair<size_t, tint>, tint> M;

tint mochila(size_t i, tint k)
{
  if (k == 0 or i == 0)
    return 0;
  if (k < 0)
    return -INF;

  auto key = make_pair(i, k);
  if (M.find(key) == M.end())
  {
    M[key] = max(mochila(i - 1, k), v[i - 1] + mochila(i - 1, k - p[i - 1]));
  }
  return M[key];
}

int main()
{
  size_t t;
  cin >> t;

  while (t--)
  {
    size_t n;
    cin >> n;

    v.assign(n, 0);
    p.assign(n, 0);

    for (size_t i = 0; i < n; i++)
      cin >> v[i] >> p[i];

    size_t g;
    cin >> g;

    tint total = 0;
    while (g--)
    {
      tint mw;
      cin >> mw;

      M.clear();
      total += mochila(n, mw);
    }

    cout << total << "\n";
    M.clear(); // limpieza entre test cases
  }

  return 0;
}