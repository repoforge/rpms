#include <stdio.h>
#include <string.h>
int main(int argc, char **argv)
{
	FILE *f=fopen("/dev/urandom", "r");
	char key[61];
	int i=0;
	char tmp;
	memset(key, 0, 61);
	while(i<60) {
		tmp=fgetc(f);
		if((tmp>='a' && tmp<='z') ||
		   (tmp>='A' && tmp<='Z') ||
		   (tmp>='0' && tmp<='0'))
			key[i++]=tmp;
	}
	puts(key);
	fclose(f);
}
