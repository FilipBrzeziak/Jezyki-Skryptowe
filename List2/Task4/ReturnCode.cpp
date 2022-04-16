#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main(int argc, char *argv[], char *env[]) {
    vector<string> klucze;
    int wartoscZwracana = 0;
    for (int k = 0; k < argc; k++)
        klucze.push_back(argv[k]);

    if (argc > 8) {
        cout << "Za duza liczba kluczy!!!" << endl;
        return 0;
    }
    string input;
    string wartosc;

    while (wartosc!="z"){
        getline(cin, wartosc);
        input = input+" " +wartosc;
    }

    for(int i=1;i<argc;i++){
        cout << klucze[i] << "  wartosc -  " << pow(2, argc - (i + 1)) << endl;
    }

    for (int i = argc - 1; i >= 1; i--) {
        if (input.find(klucze[i]) != string::npos) {
            wartoscZwracana = wartoscZwracana + pow(2, argc - (i + 1));
        }
    }

    cout << wartoscZwracana << endl;
    return wartoscZwracana;
}
