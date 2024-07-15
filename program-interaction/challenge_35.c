#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>


int pwncollege(int argc, char **argv){
	pid_t pid = fork();

	if(pid==0){

		execv("/challenge/embryoio_level35", argv);
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

