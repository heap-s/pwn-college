nclude <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>


int pwncollege(){
	pid_t pid = fork();

	if(pid==0){
		static char *argv[] = {"/challenge/embryoio_level31", "uzgirkzmoo", NULL};
		execv("/challenge/embryoio_level31", argv);
		exit(1);
	}
	else {
		waitpid(pid, 0, 0);
	}
	return 0;

}

int main(int argc, char *argv[]){
	return pwncollege(argc, argv);
}

