#include<iostream>
#include<string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[], char *env[]) {
    vector<string> envs;
    vector<string> names;
    vector<string> values;
    vector<string> result;

    bool silent = false;
    while (*env != NULL) {
        envs.push_back(*env++);
    }

    for (int i = 0; i < argc; i++) {
        string string2=argv[i];
        if (string2 == "/S") {
            silent = true;
        }
    }

    for (int j = 0; j < envs.size(); j++) {
        int lastIndex = 0;
        int lastIndexValues = 0;
        string env = envs.at(j);
        for (int i = 0; i < env.size(); i++) {
            if (env[i] == '=') {
                names.push_back(env.substr(lastIndex, i - lastIndex));
                lastIndex = i + 1;
                if (env.find(";") == string::npos) {
                    if (values.empty()) {
                        values.push_back("\t" + env.substr(lastIndex, i - lastIndex));
                    } else {
                        values.push_back(values[lastIndexValues] + "\n\t" + env.substr(lastIndex, i - lastIndex));
                    }
                    lastIndexValues++;
                    break;
                }
            } else if (env[i] == ';') {
                if (values.empty()) {
                    values.push_back("\t" + env.substr(lastIndex, i - lastIndex));
                } else {
                    values.push_back(values[lastIndexValues] + "\n\t" + env.substr(lastIndex, i - lastIndex));
                }
                lastIndexValues++;
                lastIndex = i + 1;
            }
        }
    }


    vector<bool> boolek;
    boolek.push_back(true);
    for (int j = 1; j < argc; j++) {
        if(argv[j]!="/S") {
            bool change = false;
            for (int i = 0; i < names.size(); i++) {
                if (names[i].find(argv[j]) != string::npos) {
                    result.push_back(names.at(i) + "\n=\n" + values.at(i));
                    change = true;
                }
            }
            boolek.push_back(change);
        }
    }


    for (int j = 1; j < argc; j++) {
        if(argv[j]!="/S") {
            string string1 = argv[j];
            if (!boolek[j]) {
                if (silent == false) {
                    result.push_back(string1 + "= NONE");
                }
            }
        }
    }


    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    for (int i = 0; i < result.size(); i++) {
        cout << "\n" << result.at(i) << endl;
    }

}
