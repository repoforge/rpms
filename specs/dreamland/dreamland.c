/* This program is designed to drop privileges, chroot, and run something there.
 Besides it can also impose resource limits, and other nice ( renice :) features.

 I'm trying to provide ability to drop all kinds of privileges, defined
 in Linux. If something is missed, you are encouraged to write to szh@7ka.mipt.ru
 Designed for Linux 2.2 & 2.4 ;

 Note - setting capabilities doesn't work because after exec()
 kernel setup capabilities again if uid=0 (and clears otherwise)

 http://www.7ka.mipt.ru/~szh/dreamland/

 Copyright/left Zhitomirsky Sergey <szh@7ka.mipt.ru>, 2000.
 Distributed under GNU General Public License, version 2.
 I call it "root's dreamland" (or "nobody's jail")
 It is normal that compiler generates several warnings.*/
char* version=" Version 1.9,  14 Jan 2003\n";

#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <grp.h>
//#include <dirent.h>
#include <errno.h>
#include <stdlib.h>
//#include <getopt.h>
#include <string.h>
#include <pwd.h>
#include <sys/resource.h>
#include <sys/time.h>
#include <sys/prctl.h>

#include <linux/capability.h>
#include <asm/param.h>

extern char **environ;

#define true 1
#define false 0

#define NON -600
#define OVER 250

#define NN 99
#define MAX_GROUPS NGROUPS

//used in set_uids_and_gids(), check_uids(), analize_options()
uid_t user_real  = NN;
uid_t user_eff   = NN;
uid_t user_saved = NN;
gid_t group      = NN;
int num_of_groups= 0;
gid_t groups[MAX_GROUPS] = { NN };

//used in main() && analize_options()
int v=0, env=0;
char* program=NULL;
char* params[OVER];
char* environments[OVER] = { NULL };


//used in  process_linux_capabilities() && analize_options() 
int reset_caps = 0, caps = 0, pr_cap = 0 , prctl_keep_cap = 0;

//used in set_resource_limits() && analize_options()
//there is a reason for uppercase names. 
int n = NON, NPROC = NON, CPU = NON, RSS = NON, NOFILE = NON, CORE = NON;

//used in dreamland_chroot() && analize_options()
char* chroot_dir="/";
int keep_fileids = 0;


int giveuidgid(char* s, int ug);
int check_atoi(char* str, char* error_param , int strict);
void help(char *s);
void help_about(char *s);
void process_linux_capabilities();
void check_uids();
void set_uids_and_gids();
void analize_options(int argc, char* argv[]);
void dreamland_chroot();
void set_resource_limits();
    


int main(int argc, char* argv[])
{   

    analize_options(argc, argv);

    //Accurately && Securely do chroot,  exit in case of error.
    //Also closes all dir & file(>2) descriptors.
    dreamland_chroot();
    
    // Setting resource limits, if ordered. 
    // Do it before changing UIDs or caps to less powerful!
    set_resource_limits();
    
    //setting [r,e,s]GID , groups , [r,e,s]UID  in THIS order.(guess why!)
    set_uids_and_gids();
    
    // Won't do anything, if you haven't change some exec() related things in kernel !
    // or haven't specified command line options about capabilities ( -cap, --reset-caps ) 
    process_linux_capabilities();

    //paranoya
    check_uids();
 
    // Executing desired & limited program.
    /* After exec() all user ids become equal to effective user id.
    This is Linux feature, may be I'll overcome it later, if it will
    make any sensible application. */

    environments[env] = NULL ;
    if( execve(program, params, environments) )
    {   
	perror("execve"); 
        exit(-3);
    }
    
    while(true)  // <-- my favorite piece of code (never reached)
	fprintf(stderr,"This is impossible\n");
	
	
} /* main */


//Checking if chroot was ordered, and chrooting, if so.
//Also close dir/file descriptors
void dreamland_chroot()
{
    unsigned int fd, fd_max = 1023;
    struct stat buf;
    struct rlimit lim;
    
    if( !getrlimit(RLIMIT_NOFILE,&lim) && (fd_max < lim.rlim_max) )
	fd_max = lim.rlim_max ;

    for( fd=0; fd < fd_max; fd++ )
    {
	if( !fstat(fd, &buf) && 
	    ( S_ISDIR(buf.st_mode) || ((fd > 2) && !keep_fileids) )
	)  
	    if( close(fd) ) 
	    {
		perror("close");
	        fprintf(stderr,"Unable close INsecure DIR/file ID %i, before chroot'ing\n",fd);
		exit(-2);
	    }
    }

    if( !strncmp(chroot_dir,"/",2) )
    {
	if(v) 
	    printf("warning: chroot directory not set \n");
	return;
    } 
    if(v) printf("chrootdir=%s\n",chroot_dir);



    if( chroot(chroot_dir) )
    {  
	perror("chroot");
        exit(-1);
    }
    if( chdir("/") )
    { 
	perror("chdir after chroot");
        exit(-1);
    }
    if(v) printf("We reached the chroot dreamland :)\n");
 

}



// This function checks, if the string parameter is name, or digit, 
// and returns binary number (uid or gid)  for both cases.
int giveuidgid(char* s, int ug)
{ 
    struct passwd * pw = NULL;
    struct group * gr = NULL;
    char* ss = s;

    if(!s) help("LACK OF USER/GROUP PARAMETER");

    s--;
    while(*(++s))
	if ( *s<'0' || *s>'9' ) 
	{
	    if(ug) pw = getpwnam(ss); 
	    else   gr = getgrnam(ss);

	    if(!pw && !gr)
    	    {   
	    	fprintf(stderr,"Unable to determine User/Group ID for %s\n",ss);
		exit(-1);
	    }

	    if(ug) return pw->pw_uid; 
	    else   return gr->gr_gid;
	}
	
    return atoi(ss);
}

//checking that the string consist of "isdigits", 
//and return atoi(str) , or print error & exit(-1) otherwise
int check_atoi(char* str, char* error_param , int strict)
{
    int i;

    if(!str) help("LACKING NUMERIC PARAMETER");

    for(i=0; i<strlen(str); i++)
	if( str[i]<'0' || str[i]>'9' )
	{  
	    if( i || strict==true || !(str[0]=='-' || str[0]=='+') ) 
	    { 	
		fprintf(stderr,"The string %s does not consist of digits\n"
	    		"There must be digits after %s\n %s", 
			str, error_param, strict ? " + and -  are not accepted\n" : " ");
	        exit(-1);
	    }    
	}

    return atoi(str);
}

void exit_error(char* s)
{
    fprintf(stderr,"ERROR: %s\n",s);
    exit(-1);
}


//analysing given options
void analize_options(int argc, char* argv[]) 
{
    argc--;
    argv++;
    while ( argc && *argv)
    {
        //if (!strcmp(*argv, "-s")) {s=1;user_saved= giveuidgid(*(++argv),true);} else
	if (!strcmp(*argv, "-u") || !strcmp(*argv, "--user")) 
				    user_eff = user_real = giveuidgid(*(++argv),true);else
	if (!strcmp(*argv, "-g") || !strcmp(*argv, "--group")) 
				    group = giveuidgid(*(++argv),false); else
        if (!strcmp(*argv, "-G")) 
	{
	    if(num_of_groups >= MAX_GROUPS)
		 exit_error("TOO MANY groups");
	    
	    groups[num_of_groups++]=giveuidgid(*(++argv),false);
	} else

	if (!strcmp(*argv, "-n"))      n = check_atoi(*(++argv),"-n",false); 	     else
	if (!strcmp(*argv, "-nproc"))  NPROC = check_atoi(*(++argv),"-nproc",true);  else
    	if (!strcmp(*argv, "-cpu"))    CPU = check_atoi(*(++argv),"-cpu",true);      else
	if (!strcmp(*argv, "-rss"))    RSS = check_atoi(*(++argv),"-rss",true);      else
	if (!strcmp(*argv, "-nofile")) NOFILE = check_atoi(*(++argv),"-nofile",true);else
	if (!strcmp(*argv, "-core"))   CORE = check_atoi(*(++argv),"-core",true);    else
	if (!strcmp(*argv, "-env"))    environments[env++] = *(++argv); 	     else
	if (!strcmp(*argv, "--keep-env"))
	{
	    while(*environ)
	    {
		if( env > OVER-2 )  exit_error("too many environment variables\n");
		environments[env++]=*environ++;
	    }
	    argc++;
	}
	else 
	if (!strcmp(*argv, "--reset-caps")) {reset_caps = 1; pr_cap =1;argc++;} else
	if (!strcmp(*argv, "-cap"))
	{   int empty=1;
	    pr_cap=1;
	    while( *(++argv) && (*argv)[0]!='-')//accepting enumeration of capabilities
	    {
	    	caps |= 1<<check_atoi(*argv,"-cap",true);
		empty=0;
		argc--;
	    }
	    argc++;
	    argv--;
	    
	    if(empty) 
		exit_error("list of capabilities after -cap wasn't specified\n"
		"use explicitly --reset-caps if you want to reset capabilities\n");
	}
	else
        if (!strcmp(*argv, "-h") || !strcmp(*argv, "-H") ||
            !strcmp(*argv, "--help") || !strcmp(*argv, "-?")) help(NULL); else
        if (!strcmp(*argv, "--verbose")) {v=1;argc++;} else
        if (!strcmp(*argv, "--version")) { printf("%s",version); exit(0);} else
        if (!strcmp(*argv, "--keep_fileids")) {keep_fileids=1;argc++;} else
        if (!strcmp(*argv, "-d") || !strcmp(*argv, "--chroot")) {
	    chroot_dir= *(++argv); 
	    if(!chroot_dir || (*argv)[0]=='-' ) exit_error("Lacking chroot dir parameter");
	}
	else
        if (!strcmp(*argv, "-e") || !strcmp(*argv, "-E"))
	{ 
	    int e = 1;
	    params[0] = program = *(++argv);
	    if(!program) exit_error("Lacking program name!");
	    argc--;
	    while(argc--)
	    { 
		if( e>(OVER-2) ) exit(-1);
	        params[e++]= *(++argv);
	    }
	    params[e]=NULL;
	    if(v) 
	    {	int ee;
 		for(ee=0;ee<e;ee++) printf("params[%i]=%s\n",ee,params[ee]);
 	    }

	    break;
	   
	} else 	{ 
		fprintf(stderr,"Incorrect option: %s\n",*argv);
		exit(-1); 
	}
	 
         argc-=2;
	 argv++;
    }

    user_saved=user_real;
    //if(!s) user_saved=user_real;
    /*if(keep_env && env) 
    {  cerr<<"Sorry, can't both keep old environment, and 
	assign new environment variables ; not implemented yet.\n";
	exit(-2);
    }*/
    if(v)
    {
	printf(" group=%u chroot_dir=%s user_real = %u user_eff = %u user_saved = %u\n"
		" program = %s\n",
		group, chroot_dir, user_real, user_eff, user_saved, program);
	
    }
    if(! program ) help_about("Nothing to execute! (-E option)");
 
}


// Setting resourse limits for current process, if it were ordered.
void set_resource_limits()
{
    struct rlimit lim;

    if( n!=NON ) if( nice(n) ) perror("Re-nice");

#define SET_RLIMIT( LIMIT )			\
    if( (LIMIT) != (NON) ) {			\
	lim.rlim_cur = LIMIT;			\
	lim.rlim_max = LIMIT;			\
						\
	if( setrlimit(RLIMIT_##LIMIT, &lim) ) {	\
	    perror("set resource limit");	\
    	    exit(-1);				\
	}					\
    }						\

    SET_RLIMIT ( CPU );

    SET_RLIMIT ( NOFILE );

    SET_RLIMIT ( CORE );
    
    /*Linux lets you set a limit on how many processes a user can have, via a
    setrlimit(2) call with RLIMIT_NPROC.  Unfortunately, this limit is only
    looked at when a new process is created on fork(2).  If a process changes
    its UID, it might exceed the limit for its new UID.*/

    SET_RLIMIT ( NPROC );

    /* Linux lets you set resource limits, including on how much memory a process
    can consume, via setrlimit(2).  Unfortunately, shared memory segments are
    allowed to exist without association with any process, and thus might not
    be counted against any resource limits.*/

    SET_RLIMIT ( RSS );

}



void help_about(char *s) {

    if(s) fprintf(stderr,"\n   ERROR:  %s\n",s);

    fprintf(stderr,
    "\n This program executes specified program in a CHROOT environment,\n"
    "drops privileges, changes UIDs, GIDs to specified ones,\n"
    " Besides it can impose resource limits\n"
    "and is able to drop most privileges defined in Linux.\n"
    "(If you specify dropping them in command line)\n"
    "It can make root's dream come true about where (chrooted land),\n"
    "and with what privileges (nobody's) services should run.\n"
    "Before chroot Closes all DIR descriptors and (if not disabled)file descr > 2\n"

    "\n   type \"dreamland --help\"  for options info\n\n");

    exit(0);
}  



void help(char* s)
{ 
    if(s) fprintf(stderr,"\n   ERROR:  %s\n",s);
 
    fprintf(stderr,"\n USAGE EXAMPLE:\n"
    "/sbin/dreamland -u nobody -g 66 -G 98 -G floppy --chroot /var/chroot\n"
    "    -env PATH=/bin:/sbin -nproc 10 -n 7 -E /sbin/service service_params\n");

    fprintf(stderr,
    "\n OPTIONS: \n"
    "[ --chroot chroot_dir] chroot to chroot_dir    \n"
    "[ -u user ]    real, effective and saved USER IDs will be set, default user=99\n"
    "[ -g group ]   group may be number or name (as well as user), default=99\n"
    "[ -G additional_group_id ] may be many -G , sets list of supplementary group ID\n"
    "[ -E program_to_execute its params]  \n\n"
    
    "[ -n nice ] modified scheduling priority; [-core max_core_file_size] \n"
    "[-nproc max_number_of_child_processes] [-cpu max_CPU_time(in seconds)] \n"
    "[-rss max_resident_set_size ] [-nofile max_number_of_open_files] \n"
    "[--version ]  [--verbose ]  [-h --help ] print this message\n"
    "[-env environment_variable ] (example: -env PATH=/bin:/sbin -env CRACKERS=loosers )\n"
    "[--keep-env ] orders to keep all environment variables instead of clearing them\n"
    "[--keep_fileids] don't specially close open files (but will close dirs)\n"
    "[--reset-caps ] clear all process capabilities (this is NOT properly supported by kernel!\n"
    "[-cap number_of_capability] may be several -cap ; (NOT properly supported by kernel!)\n\n"
    
    "\n DEFAULTS: All process's user IDs=99, group IDs=99, no chroot_dir,\n"
    "if dreamland is run with user id = 0 and no -G options were given,\n"
    "set NULL groups massive;  --user is alias to -u , --group to -g \n"
    "all environment variables are reset, and only those given with -env options (if any) are set.\n"
    "if --chroot - close all opened directories, and files( except stdin,stdout,stderr)\n"); 
    
    fprintf(stderr,"\nNOTE: -E must be the last parameter, and is the only required parameter,\n"
    "options after -E will be given to executed program; however if you are running dreamland\n"
    "under user, you need two additional options -u user -g user, or dreamland\n"
    "will fail, while trying to set user and group IDs to default ones (99,99)\n");

    fprintf(stderr," You may specify as many \"-G\" as you want(up to %u), \n"
    "all will become a part of groups massive\n"
    "You can use both user names and UIDs(GIDs) in command line after options -u -g -G \n"
    "In case of any error (except setting nice level) dreamland will \n"
    "exit(-1) without running -E service\n",MAX_GROUPS);

    fprintf(stderr,"\n Copyright/left Zhitomirsky Sergey, 2001.\n");
    fprintf(stderr,"%s",version);
    fprintf(stderr," Distributed under GNU General Public License, version 2.\n");

    if(s) fprintf(stderr,"\n   ERROR:  %s\n",s);

    exit(-1);
} 

// Setting capabilities , won't work on default kernel - 
// after exec() if uid=0 kernel set them up!  else - down!
void process_linux_capabilities()
{ 

    cap_user_header_t header;
    cap_user_data_t data;
    
    if(!pr_cap) return;

    header = (cap_user_header_t) malloc(sizeof(struct __user_cap_header_struct));
    data = (cap_user_data_t) malloc(sizeof(struct __user_cap_data_struct));
    
    if(!header || !data) { perror("malloc"); exit(-1); }

    header->pid = 0; //getpid();  0 required if don't have cap_setpcap !!!
    header->version = _LINUX_CAPABILITY_VERSION;

    printf("Dropping capabilities doesn't work after exec() on default kernel if uid=0\n");

    if(v) printf("caps = %i\n",caps);
    if(reset_caps && caps) 
	fprintf(stderr,"warning: you set --reset-caps and -cap;"
		"--reset-caps will be processed\n"); 
    
    //Changing capabilities (usually useless, and returns with error, if user id != 0 )
    // Warning: This feature won't work after exec() , because ... see kernel sources.
    data->inheritable = data->effective = data->permitted = caps;
    if(reset_caps)
    {   if(v) printf("Dropping away all Capabilities\n");
        data->inheritable = data->effective = data->permitted = 0;
    }

    /*if( !prctl(PR_SET_KEEPCAPS,1, NULL, NULL, NULL) ) 
     	    prctl_reset_cap =1; setxuid*/
    
    if( capset(header, data) )
    { 	
	fprintf(stderr,"User Id=%u , Group Id=%u. Use [ -u UID ] [ -g GID ] "
			"for non-default\n", user_eff, group);
	perror("capset");
        exit(-1);
    }

    free(header);
    free(data);    
}
/*
#include <asm/unistd.h>

_syscall2(long, capset, cap_user_header_t, header, cap_user_data_t, data);
_syscall3(long, setresuid32, uid_t, ruid, uid_t, euid, uid_t, suid);
_syscall3(long, getresuid32, uid_t*, ruid, uid_t*, euid, uid_t***, *suid);
_syscall3(long, setresgid32, gid_t, rgid, gid_t, egid, gid_t, sgid);

#define setresuid setresuid32
#define setresgid setresgid32
#define getresuid getresuid32

*/


//setting [r,e,s]gid , groups , [r,e,s]uid  in THIS order.(guess why!)
void set_uids_and_gids()
{
    // Setting process group IDs to desired values.
    if(setresgid(group,group,group) )
    {   
	fprintf(stderr,"\nSetting Group ID %u    (for non default use -g option)\n",group);
	perror("setresgid");
        exit(-1);
    }
 
    // Setting process groups massive to desired values.
    // Unless -G options were given,  set by default groups massive to NULL.
    // In Linux it is allowed only for CAP_SETGID capable process, 
    // so if dreamland is run without root privileges and without -G options
    // by default don't changing group massive
    if(geteuid())
    { 
	if(num_of_groups) 
	{ 
	    fprintf(stderr,"Warning: setting groups massive is not allowed for users\n");
    	    //Desperate attempt anyway:
	    if(setgroups(num_of_groups,groups))
	    { 
		perror("setgroups");
		exit(-1);
	    } 
	}
        else /*if(v)*/ 
    	    printf("Warning: Don't have root privileges, so groups massive remains unchanged\n");
    }
    else
    { 
	if(v && (num_of_groups==0)) printf("Setting default groups massive(=NULL)\n");
        if(setgroups(num_of_groups,groups))
	{ 
	    perror("setgroups");
	    exit(-1);
	}
    }
    

    // Setting process user ids to desired values.
    if( setresuid(user_real,user_eff,user_saved))//setfsuid()||setreuid()||setuid()
    {  
	fprintf(stderr,"Setting User ID (real, effective, saved) to %u %u %u \n"
	    " (for non default use -u option)\n",user_real,user_eff,user_saved);
	perror("setresuid");
	exit(-1);
    }//WARNING: anyway after exec() all id's will become equal user_eff
  
}


// Making small unnecessary check.
void check_uids() {

    uid_t re,ef,sav;
    if(getresuid(&re,&ef,&sav)) 
    {
	 perror("getresuid"); 
    	 exit(-1); 
    }
    if(re!=user_real || ef!= user_eff || sav != user_saved) 
    {
        fprintf(stderr," What is going on ? %u!=%u  || %u!=%u  || %u!=%u\n"
    		"Crasy things happen in the sistem, aborting...\n",re,user_real,
        	ef,user_eff,sav,user_saved);
        exit(-1);
    }
} 

