#include <stdio.h>
#include <string.h>
#include <ctype.h>


#define TABLE_SIZE 65536

static char *map_names[]={
	"plain","shift","ctrl","altgr","shift_ctrl",
	"altgr_ctrl","alt","shift_alt","ctrl_alt", NULL
};

static char *def_map="us";
static char *def_ext=".map";
static char *prog;
static int table[TABLE_SIZE];

struct hexbuf
{
	int ct;
	int buf[1024];
};

struct map
{
	struct hexbuf maps[9];
};

static struct map kbd;
static struct map def;

static void usage(void)
{
	fprintf(stderr, "usage: %s [ -p old_code=new_code ] ...\n"
		"%*s[path]default_layout[.map] ] "
		"[path]kbd_layout[.map]\n",
		prog, strlen(prog)-8, "");
	exit(1); 
}


static void hexify(struct hexbuf *hb, char *p)
{
	while(*p)
	{
		char *n;
		while(*p && isspace(*p))
			p++;
		if(!*p)
			return;
		if(strncmp(p,"0x",2))
		{
			fprintf(stderr, "%s: bad format.\n", prog);
			exit(1);
		}
		n=p+2;
		p=strchr(p,',');
		if(p!=NULL)
			*p++=0;
		if(sscanf(n, "%x", &hb->buf[hb->ct++])!=1)
		{
			fprintf(stderr, "%s: bad format.\n", prog);
			exit(1);
		}
	}
}
	
static int which_map(char *p)
{
	int i;
	for(i=0;i<9;i++)
	{
		if(strcmp(p, map_names[i])==0)
			return i;
	}
	fprintf(stderr, "%s: bad map name '%s'.\n", prog, p);
	exit(1);
}




static void load_map(struct map *m, char *map)
{
	int empty;
	char *map_ext;
	char buf[1024];
	FILE *file;
	int n = 0;
	struct hexbuf *current;

	if(map==NULL)
		map=def_map;
	if(strchr(map,'.'))
		map_ext="";
	else
		map_ext=def_ext;
		
	fprintf(stderr, "going to run loadkeys\n");
	snprintf(buf, 1024, "loadkeys -m \"%s%s\"", map, map_ext);
	fprintf(stderr, "buf is %s\n", buf);
	
	file=popen(buf, "r");
	if(file==NULL)
	{
		perror("loadkeys");
		exit(1);
	}
	
	current=NULL;
	empty = 1;
	
	while(fgets(buf, 1024, file)!=NULL)
	{
		char *dp=buf;
		if(strncmp(dp, "static ", 7)==0)
			dp+=7;
		if(strncmp(dp, "u_short ", 8)==0)
		{
			if(current)
			{
				fprintf(stderr, "%s: active at beginning of map.\n", prog);
				exit(1);
			}
			else
			{
				char *ep=strchr(dp+8,'_');
				*ep=0;
				current = &m->maps[which_map(dp+8)];
				continue;
			}
		}
		if(strncmp(buf, "};",2)==0)
		{
			current=NULL;
		}
		if(current==NULL)
			continue;
		hexify(current, buf);
		empty = 0;
	}
	pclose(file);
	if(empty)
	{
		fprintf(stderr, "%s: Keymap is empty\n", prog);
		exit(1);
	}
}


static void build_table(char *maps[])
{
 	int set = 0;
	char *map;
 	int i=0,j;
 	static unsigned int tmp[9*256];
 	
 	for(i=0;maps[i]!=NULL;i++)
 	{
		struct hexbuf *hb = &def.maps[i];
		int code = set;
		for (j=0;j<256;j++)
		{
			if(tmp[code]==0)
				tmp[code] = hb->buf[j];
			code++;
		}
		set += 256;
	}
	set = 0;
	
	i=0;
	for(i=0;maps[i]!=NULL; i++)
	{
		struct hexbuf *hb = &kbd.maps[i];
		int code = set;
		for(j=0;j<256;j++)
		{
			if(table[tmp[code]]==0)
				table[tmp[code]] = hb->buf[j];
			code++;
		}
		set += 256;
	}
	table[0] = 0;
}

int main(int argc, char *argv[])
{
	int i;
	prog=argv[0];
	argv++;
	/*
	 *	Load user set keyvals
	 */
	while(argv[0] && strcmp(argv[0],"-p")==0)
	{
		int o,n;
		argv++;
		if(argv[0]==NULL || sscanf(argv[0], "%d=%d", &o, &n)!=2)
			usage();
		if(o < TABLE_SIZE)
			table[o]=n;
		argv++;
	}
	
	if(argv[0]==NULL)
		usage();
	load_map(&def,argv[1] ? argv[0] : NULL);
	load_map(&kbd,argv[1] ? argv[1] : argv[0]);
	
	build_table(map_names);
	for (i = 0; i < 256; i++) {
		printf("%c",table[i] ? table[i] : i);
	}
	return 0;
}
