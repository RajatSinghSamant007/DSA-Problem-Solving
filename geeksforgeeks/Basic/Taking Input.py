#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int n;
    float f;
    int ff = f; // To Store floor of float variable f

    // code here
    getline(cin , s);
    cin >> n >>ff;

    cout << s << endl;
    cout << n << endl;
    cout <<ff << endl;
    return 0;
}