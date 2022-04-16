#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string static ReplaceAll(std::string str, const std::string& from, const std::string& to) {
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // Handles case where 'to' is a substring of 'from'
    }
    return str;
}


vector<string> paths(char *env[]) {
    string getPath = std::getenv("PATH");
    string path = ReplaceAll(getPath, ";;", ";");
    cout << path << endl;
    string temp = "";

    vector<string> folders;

    while (path != "") {
        int pozycjaSrednika = 0;
        if (path.find(";") != string::npos) {
            pozycjaSrednika = path.find(";");
        }

        if (pozycjaSrednika != 0) {
            temp = path.substr(0, pozycjaSrednika);
            path = path.substr(pozycjaSrednika + 1, path.size() - 1);
        }
        else {
            temp = path;
            path = "";
        }
        folders.push_back(temp);
    }


    return folders;
}

void showPathsA(int argc, char *argv[], vector<string> &folders) {
    for (int i = 0; i < folders.size(); i++) {
        cout << folders[i] << endl;
    }
}

void showPathsB(int argc, char *argv[], vector<string> &folders) {
    sort(folders.begin(), folders.end());
    for (int i = 0; i < folders.size(); i++) {
        cout << folders[i] << endl;
    }
}

void showPathsCD(int argc, char *argv[], vector<string> &folders) {
    sort(folders.begin(), folders.end());

    for (int j = 0; j < argc; j++) {
        if (argv[j] == "/D") {
            for (int i = 1; i < folders.size(); i++) {
                if (folders.at(i) == folders.at(i - 1) || folders.at(i) + "\tDUPLIKAT" == folders.at(i - 1)) {
                    folders.at(i) = folders.at(i) + "\tDUPLIKAT";
                }
            }
        }
        if (argv[j] == "/B") {
            for (int i = 0; i < folders.size(); i++) {
                if (folders.at(i) == "") {
                    folders.at(i) = "\tBRAK" + folders.at(i);
                }
            }
        }
    }

    for (int i = 0; i < folders.size(); i++) {
        cout << folders[i] << endl;
    }

}




int main(int argc, char *argv[], char *env[]) {
    vector<string> folders = paths(env);

    //a)
    cout << "a)\n\n" << endl;
    showPathsA(argc, argv, folders);


    //b)
    cout << "\n\n\nb)\n\n" << endl;
    showPathsB(argc, argv, folders);


    //c) i d)
    cout << "\n\n\nc) i d)\n\n" << endl;
    showPathsCD(argc, argv, folders);

    return 0;
}
