#include <iostream>

using namespace std;

int main(int argc, char *argv[], char *env[]) {
    puts("ARGUMENTY PROGRAMU:");
    for (int k = 0; k < argc; k++)
        puts(argv[k]);

    puts("ZMIENNE ŚRODOWISKA:");
    while (*env != NULL)
        puts(*env++);

    return 10;
}