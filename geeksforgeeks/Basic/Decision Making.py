#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int result = (n>m) ? 1 : (n<m) ? 2 : 3;
    // code here
    switch (result){
        case 1:
        cout << "greater";
        break;
        case 2:
        cout << "less";
        break;
        case 3:
        cout << "equal";
        break;
    }

    return 0;
}