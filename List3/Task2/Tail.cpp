#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {

    string line;
    string arg;
    vector<string> vector;
    int n=0;
    int x=0;

    if (argc < 2 || argc > 3) return 2;

    if ((arg = argv[1]) == "/S") {
        n = stoi(argv[2]);
    } else {
        n = stoi(argv[1]);
    }


    while (getline(cin, line)) {
        vector.push_back(line);
        x++;
    }

    if (n <= x) {
        for(int i=x-n;i<x;i++){
            cout << vector.at(i) << endl;
        }
        return 0;
    } else {
        for(int i=0;i<x;i++){
            cout << vector.at(i) << endl;
        }
        if (arg != "/S") cout << "Braklo " << n - x << " lini do wypisania" << endl;
        return 2;
    }


    return 0;
}
