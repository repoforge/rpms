/*
 *	T T C P . C
 *
 * Test TCP connection.  Makes a connection on port 5001
 * and transfers fabricated buffers or data copied from stdin.
 *
 * Usable on 4.2, 4.3, and 4.1a systems by defining one of
 * BSD42 BSD43 (BSD41a)
 * Machines using System V with BSD sockets should define SYSV.
 *
 * Modified for operation under 4.2BSD, 18 Dec 84
 *      T.C. Slattery, USNA
 * Minor improvements, Mike Muuss and Terry Slattery, 16-Oct-85.
 * Modified in 1989 at Silicon Graphics, Inc.
 *	catch SIGPIPE to be able to print stats when receiver has died 
 *	for tcp, don't look for sentinel during reads to allow small transfers
 *	increased default buffer size to 8K, nbuf to 2K to transfer 16MB
 *	moved default port to 5001, beyond IPPORT_USERRESERVED
 *	make sinkmode default because it is more popular, 
 *		-s now means don't sink/source 
 *	count number of read/write system calls to see effects of 
 *		blocking from full socket buffers
 *	for tcp, -D option turns off buffered writes (sets TCP_NODELAY sockopt)
 *	buffer alignment options, -A and -O
 *	print stats in a format that's a bit easier to use with grep & awk
 *	for SYSV, mimic BSD routines to use most of the existing timing code
 * Modified by Steve Miller of the University of Maryland, College Park
 *	-b sets the socket buffer size (SO_SNDBUF/SO_RCVBUF)
 * Modified Sept. 1989 at Silicon Graphics, Inc.
 *	restored -s sense at request of tcs@brl
 * Modified Oct. 1991 at Silicon Graphics, Inc.
 *	use getopt(3) for option processing, add -f and -T options.
 *	SGI IRIX 3.3 and 4.0 releases don't need #define SYSV.
 * Modified 1996/1997 at CERN Switzerland by Daniel DAVIDS
 *
 * Distribution Status -
 *      Public Domain.  Distribution Unlimited.
 */
#ifndef lint
static char RCSid[] = "ttcp.c $Revision: 1.1 $";
#endif

static char VersDate[] = "2-Dec-1997";

/* #define NT */
/* #define BSD43 */
/* #define BSD42 */
/* #define BSD41a */
#define SYSV            /* required on SGI-IRIX releases before 3.3 */
			/* as well as for the following OS  systems */
			/* HP-UX, Hewlett-Packard 9000 Series  OS's */
			/* SUN systems, Solaris Only (NOT SunOS OS) */
			/* OSF/1 V3.2 DEC Alpha-Chip Operating Syst */
			/* LINUX --- Which is Unix for PC Computers */
			/* Windows / NT, mandatory with variable NT */

#include <stdio.h>
#include <signal.h>
#include <ctype.h>
#include <errno.h>
#include <sys/types.h>
#if !defined(NT)
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <sys/time.h>		/* struct timeval */
#else /* NT */
#include <windows.h>	/* required for all Windows applications */
#include <winsock.h>
#include <memory.h>
#include <time.h>
#include <sys/timeb.h>
#include <process.h>       /* for _beginthread                      */
#include <stdlib.h>
#endif /* NT */

#if defined(SYSV) && !defined(__osf__) && !defined(__linux__)
#include <sys/times.h>
#if !defined(NT) && !defined(__SVR4)
#include <sys/param.h>
#else /* NT || __SVR4 */
#define bcopy(a,b,n) memcpy((b), (a), (n))
#define bzero(a,n) memset((a), 0, (n))
extern int getopt();
#endif /* NT */
struct rusage {
    struct timeval ru_utime, ru_stime;
};
#define RUSAGE_SELF 0
#else /* !SYSV || __osf__ || __linux__ */
#include <sys/resource.h>
#endif /* !SYSV || __osf__ || __linux__ */

#if defined(NT)
#ifndef _GETOPT_
#define _GETOPT_

int getopt(int argc, char **argv, char *optstring);

extern char *optarg;		// returned arg to go with this option
extern int optind;		// index to next argv element to process
extern int opterr;		// should error messages be printed?
extern int optopt;		//

#define BADCH ('?')

#endif // _GETOPT

/*
 * get option letter from argument vector
 */
int
	opterr = 1,		// should error messages be printed?
	optind = 1,		// index into parent argv vector
	optopt;			// character checked for validity
char
	*optarg;		// argument associated with option

#define EMSG	""

char *progname;			// may also be defined elsewhere

static void
error(char *pch)
{
	if (!opterr) {
		return;		// without printing
	}
	fprintf(stderr, "%s: %s: %c\n",
		(NULL != progname) ? progname : "getopt", pch, optopt);
}

int
getopt(int argc, char **argv, char *ostr)
{
	static char *place = EMSG;	/* option letter processing */
	register char *oli;			/* option letter list index */

	if (!*place) {
		// update scanning pointer
		if (optind >= argc || *(place = argv[optind]) != '-' || !*++place) {
			return EOF; 
		}
		if (*place == '-') {
			// found "--"
			++optind;
			return EOF;
		}
	}

	/* option letter okay? */
	if ((optopt = (int)*place++) == (int)':'
		|| !(oli = strchr(ostr, optopt))) {
		if (!*place) {
			++optind;
		}
		error("illegal option");
		return BADCH;
	}
	if (*++oli != ':') {	
		/* don't need argument */
		optarg = NULL;
		if (!*place)
			++optind;
	} else {
		/* need an argument */
		if (*place) {
			optarg = place;		/* no white space */
		} else  if (argc <= ++optind) {
			/* no arg */
			place = EMSG;
			error("option requires an argument");
			return BADCH;
		} else {
			optarg = argv[optind];		/* white space */
		}
		place = EMSG;
		++optind;
	}
	return optopt;			// return option letter
}
#endif /* NT */


struct sockaddr_in sinme;
struct sockaddr_in sinhim;
struct sockaddr_in frominet;

int domain, fromlen;
#if defined(NT)
SOCKET fd;				/* fd of network socket */
#else
int fd;				/* fd of network socket */
#endif

int buflen = 8 * 1024;		/* length of buffer */
char *buf;			/* ptr to dynamic buffer */
int nbuf = 2 * 1024;		/* number of buffers to send in sinkmode */

int bufoffset = 0;		/* align buffer to this */
int bufalign = 16*1024;		/* modulo this */

int udp = 0;			/* 0 = tcp, !0 = udp */
int options = 0;		/* socket options */
int one = 1;                    /* for 4.3 BSD style setsockopt() */
short port = 5001;		/* TCP port number */
char *host;			/* ptr to name of host */
int trans;			/* 0=receive, !0=transmit mode */
int debug = 0;                  /* 0=No-Debug, 1=Debug-Set-On */
int sinkmode = 0;		/* 0=normal I/O, !0=sink/source mode */
int verbose = 0;		/* 0=print basic info, 1=print cpu rate, proc
				 * resource usage. */
int nodelay = 0;		/* set TCP_NODELAY socket option */
int b_flag = 0;			/* use mread() */
int sockbufsize = 0;		/* socket buffer size to use */
char fmt = 'K';			/* output format: k = kilobits, K = kilobytes,
				 *  m = megabits, M = megabytes, 
				 *  g = gigabits, G = gigabytes */
int touchdata = 0;		/* access data after reading */

struct hostent *addr;
extern int errno;
extern int optind;
extern char *optarg;

char Usage[] = "\
Usage: ttcp -t [-options] host [ < in ]\n\
       ttcp -r [-options > out]\n\
Common options:\n\
	-V      prints version number and date of last modification\n\
	-l ##	length of bufs read from or written to network (default 8192)\n\
	-u	use UDP instead of TCP\n\
	-p ##	port number to send to or listen at (default 5001)\n\
	-s	-t: source a pattern to network\n\
		-r: sink (discard) all data from network\n\
	-A	align the start of buffers to this modulus (default 16384)\n\
	-O	start buffers at this offset from the modulus (default 0)\n\
	-v	verbose: print more statistics\n\
	-d	set SO_DEBUG socket option\n\
	-b ##	set socket buffer size (if supported)\n\
	-f X	format for rate: k,K = kilo{bit,byte}; m,M = mega; g,G = giga\n\
Options specific to -t:\n\
	-n##	number of source bufs written to network (default 2048)\n\
	-D	don't buffer TCP writes (sets TCP_NODELAY socket option)\n\
Options specific to -r:\n\
	-B	for -s, only output full blocks as specified by -l (for TAR)\n\
	-T	\"touch\": access each byte as it's read\n\
";	

char stats[128];
double nbytes;			/* bytes on net */
unsigned long numCalls;		/* # of I/O system calls */
double cput, realt;		/* user, real time (seconds) */

void err();
void mes();
int pattern();
void prep_timer();
double read_timer();
int Nread();
int Nwrite();
void delay();
int mread();
char *outfmt();

void
sigpipe()
{
}

main(argc,argv)
int argc;
char **argv;
{
	unsigned long addr_tmp;
	int c;
	int sockbufsndsize,sockbufrcvsize;
	int sockbuflen;
#if defined(NT)
	extern char *optarg;
	WSADATA WSAData;

	WSAStartup(MAKEWORD(1,1), &WSAData);
#endif /* NT */

	if (argc < 2) goto usage;

	while ((c = getopt(argc, argv, "drstuvVBDTb:f:l:n:p:A:O:")) != -1) {
		switch (c) {

		case 'V':
			fprintf(stdout,"%s %s\n" , RCSid , VersDate );
			exit(0);
		case 'B':
			b_flag = 1;
			break;
		case 't':
			trans = 1;
			break;
		case 'r':
			trans = 0;
			break;
		case 'd':
			options |= SO_DEBUG;
			++debug;
			break;
		case 'D':
#ifdef TCP_NODELAY
			nodelay = 1;
#else
			fprintf(stderr, 
	"ttcp: -D option ignored: TCP_NODELAY socket option not supported\n");
#endif
			break;
		case 'n':
			nbuf = atoi(optarg);
			break;
		case 'l':
			buflen = atoi(optarg);
			break;
		case 's':
			sinkmode = !sinkmode;
			break;
		case 'p':
			port = atoi(optarg);
			break;
		case 'u':
			udp = 1;
			break;
		case 'v':
			verbose = 1;
			break;
		case 'A':
			bufalign = atoi(optarg);
			break;
		case 'O':
			bufoffset = atoi(optarg);
			break;
		case 'b':
#if defined(SO_SNDBUF) || defined(SO_RCVBUF)
			sockbufsize = atoi(optarg);
#else
			fprintf(stderr, 
"ttcp: -b option ignored: SO_SNDBUF/SO_RCVBUF socket options not supported\n");
#endif
			break;
		case 'f':
			fmt = *optarg;
			break;
		case 'T':
			touchdata = 1;
			break;

		default:
			goto usage;
		}
	}
	if(trans)  {
		/* xmitr */
		if (optind == argc)
			goto usage;
		bzero((char *)&sinhim, sizeof(sinhim));
		host = argv[optind];
		if (atoi(host) > 0 )  {
			/* Numeric */
			sinhim.sin_family = AF_INET;
#if defined(cray)
			addr_tmp = inet_addr(host);
			sinhim.sin_addr = addr_tmp;
#else
			sinhim.sin_addr.s_addr = inet_addr(host);
#endif
		} else {
			if ((addr=gethostbyname(host)) == NULL)
				err("bad hostname");
			sinhim.sin_family = addr->h_addrtype;
			bcopy(addr->h_addr,(char*)&addr_tmp, addr->h_length);
#if defined(cray)
			sinhim.sin_addr = addr_tmp;
#else
			sinhim.sin_addr.s_addr = addr_tmp;
#endif /* cray */
		}
		sinhim.sin_port = htons(port);
		sinme.sin_port = 0;		/* free choice */
	} else {
		/* rcvr */
		sinme.sin_port =  htons(port);
	}
#if defined(NT)
	sinme.sin_family = AF_INET;
#endif


	if (udp && buflen < 5) {
	    buflen = 5;		/* send more than the sentinel size */
	}

	if ( (buf = (char *)malloc(buflen+bufalign)) == (char *)NULL)
		err("malloc");
	if (bufalign != 0)
		buf +=(bufalign - ((int)buf % bufalign) + bufoffset) % bufalign;

#if defined(NT)
	if ((fd = socket(AF_INET, udp?SOCK_DGRAM:SOCK_STREAM, 0)) == INVALID_SOCKET)
		err("socket");
#else
	if ((fd = socket(AF_INET, udp?SOCK_DGRAM:SOCK_STREAM, 0)) < 0)
		err("socket");
#endif

	if (verbose) {
		fprintf(stdout,
			"ttcp%s: File-Descriptor 0x%x Opened\n" ,
			trans?"-t":"-r", fd );
	}

	if (trans) {
	    fprintf(stdout,
	    "ttcp-t: buflen=%d, nbuf=%d, align=%d/%d, port=%d\nttcp-t: ",
		buflen, nbuf, bufalign, bufoffset, port);
	} else {
	    fprintf(stdout,
	    "ttcp-r: buflen=%d, nbuf=%d, align=%d/%d, port=%d\nttcp-r: ",
 		buflen, nbuf, bufalign, bufoffset, port);
	}

#if defined(NT)
	if (bind(fd, (struct sockaddr FAR *)&sinme, sizeof(sinme)) == SOCKET_ERROR) {
		fprintf(stderr, "bind: %d is the error\n", WSAGetLastError());
		perror("bind");
		exit(1);
	}
#else
	if (bind(fd, &sinme, sizeof(sinme)) < 0)
		err("bind");
#endif /* NT */

#if defined(SO_SNDBUF) || defined(SO_RCVBUF)
	if (sockbufsize) {
	    if (trans) {
		if (setsockopt(fd, SOL_SOCKET, SO_SNDBUF, &sockbufsize,
		    sizeof sockbufsize) < 0)
			err("setsockopt: sndbuf");
		mes("sndbuf");
	    } else {
		if (setsockopt(fd, SOL_SOCKET, SO_RCVBUF, &sockbufsize,
		    sizeof sockbufsize) < 0)
			err("setsockopt: rcvbuf");
		mes("rcvbuf");
	    }
	}
	else
	{
	  /*
	  ** Added by Daniel Davids to Know Socket-Buffer-Sizes
	  */
	  sockbuflen = sizeof sockbufsndsize;
	  getsockopt(fd, SOL_SOCKET, SO_SNDBUF, &sockbufsndsize, &sockbuflen);

	  sockbuflen = sizeof sockbufrcvsize;
	  getsockopt(fd, SOL_SOCKET, SO_RCVBUF, &sockbufrcvsize, &sockbuflen);

	  sockbufsize = ( sockbufsndsize + sockbufrcvsize ) / 2;

	  if ( sockbufsndsize != sockbufrcvsize )
	  {
	    fprintf(stdout, "sockbufsndsize=%d, ", sockbufsndsize );
	    fprintf(stdout, "sockbufrcvsize=%d, ", sockbufrcvsize );
	  }
	}
#endif

	if (trans) {
 	    if (sockbufsize)
		fprintf(stdout, "sockbufsize=%d, ", sockbufsize);
	    fprintf(stdout, " # %s -> %s #\n", udp?"udp":"tcp", host);
	} else {
 	    if (sockbufsize)
		fprintf(stdout, "sockbufsize=%d, ", sockbufsize);
	    fprintf(stdout, " # %s #\n", udp?"udp":"tcp");
	}

	if (!udp)  {
#if !defined(NT)
	    signal(SIGPIPE, sigpipe);
#endif /* !NT */
	    if (trans) {
		/* We are the client if transmitting */
		if (options)  {
#if defined(BSD42)
			if( setsockopt(fd, SOL_SOCKET, options, 0, 0) < 0)
#else /* BSD43 */
			if( setsockopt(fd, SOL_SOCKET, options, &one, sizeof(one)) < 0)
#endif
				err("setsockopt");
		}
#ifdef TCP_NODELAY
		if (nodelay) {
			struct protoent *p;
			p = getprotobyname("tcp");
			if( p && setsockopt(fd, p->p_proto, TCP_NODELAY, 
			    &one, sizeof(one)) < 0)
				err("setsockopt: nodelay");
			mes("nodelay");
		}
#endif
		if(connect(fd, &sinhim, sizeof(sinhim) ) < 0)
			err("connect");
		mes("connect");
	    } else {
		/* otherwise, we are the server and 
	         * should listen for the connections
	         */
#if defined(ultrix) || defined(sgi) || ( defined(__osf__) && ! defined(_CFE) )
		listen(fd,1);   /* workaround for alleged u4.2 bug */
#else
		listen(fd,0);   /* allow a queue of 0 */
#endif
		if(options)  {
#if defined(BSD42)
			if( setsockopt(fd, SOL_SOCKET, options, 0, 0) < 0)
#else /* BSD43 */
			if( setsockopt(fd, SOL_SOCKET, options, &one, sizeof(one)) < 0)
#endif
				err("setsockopt");
		}
		fromlen = sizeof(frominet);
		domain = AF_INET;
		if((fd=accept(fd, &frominet, &fromlen) ) < 0)
			err("accept");
		{ struct sockaddr_in peer;
		  int peerlen = sizeof(peer);
		  if (getpeername(fd, (struct sockaddr_in *) &peer, 
				&peerlen) < 0) {
			err("getpeername");
		  }
		  fprintf(stderr,"ttcp-r: accept from %s\n", 
			inet_ntoa(peer.sin_addr));
		}
	    }
	}
	prep_timer();
	errno = 0;
	if (sinkmode) {      
		register int cnt;
		int nb = 0;
		if (trans)  {
			pattern( buf, buflen );
			if(udp)  (void)Nwrite( fd, buf, 4 ); /* rcvr start */
			while (nbuf-- && (cnt=Nwrite(fd,buf,buflen)) == buflen) {
				++nb;
				if(debug&&((cnt!=buflen)||(debug>1))) fprintf(stdout,
					"ttcp%s: %5d | errno %d | %d Bytes Written\n",
					trans?"-t":"-r", nb, (cnt!=buflen?errno:0) , cnt );
				nbytes += buflen;
			}
			if(udp)  (void)Nwrite( fd, buf, 4 ); /* rcvr end */
		} else {
			if (udp) {
				while ((cnt=Nread(fd,buf,buflen)) > 0)  {
					static int going = 0;
					if( cnt <= 4 )  {
						if( going )
							break;      /* "EOF" */
						going = 1;
						prep_timer();
					} else {
						++nb;
						if(debug&&((cnt!=buflen)||(debug>1))) fprintf(stdout,
							"ttcp%s: %5d | errno %d | %d Bytes Read\n",
							trans?"-t":"-r", nb, (cnt!=buflen?errno:0) , cnt );
						nbytes += cnt;
					}
				}
			} else {
				while ((cnt=Nread(fd,buf,buflen)) > 0)  {
					++nb;
					if(debug&&((cnt!=buflen)||(debug>1))) fprintf(stdout,
						"ttcp%s: %5d | errno %d | %d Bytes Read\n",
						trans?"-t":"-r", nb, (cnt!=buflen?errno:0) , cnt );
					nbytes += cnt;
				}
			}
		}
#if !defined(NT)
	} else {
		register int cnt;
		if (trans)  {
			while((cnt=read(0,buf,buflen)) > 0 &&
			    Nwrite(fd,buf,cnt) == cnt)
				nbytes += cnt;
		}  else  {
			while((cnt=Nread(fd,buf,buflen)) > 0 &&
			    write(1,buf,cnt) == cnt)
				nbytes += cnt;
		}
#endif /* NT */
	}
	if(errno)
	{
	  fprintf(stderr,"ttcp%s: ", trans?"-t":"-r");
	  perror("IO");
	  fprintf(stderr,"ttcp%s: errno=%d\n",trans?"-t":"-r",errno);
	}
	(void)read_timer(stats,sizeof(stats));
	if(udp&&trans)  {
		(void)Nwrite( fd, buf, 4 ); /* rcvr end */
		(void)Nwrite( fd, buf, 4 ); /* rcvr end */
		(void)Nwrite( fd, buf, 4 ); /* rcvr end */
		(void)Nwrite( fd, buf, 4 ); /* rcvr end */
	}
	if( cput <= 0.0 )  cput = 0.001;
	if( realt <= 0.0 )  realt = 0.001;
	fprintf(stdout,
		"ttcp%s: %.0f bytes in %.3f real seconds = %s/sec +++\n",
		trans?"-t":"-r",
		nbytes, realt, outfmt(nbytes/realt));
	if (verbose) {
	    fprintf(stdout,
		"ttcp%s: %.0f bytes in %.3f CPU seconds = %s/cpu sec\n",
		trans?"-t":"-r",
		nbytes, cput, outfmt(nbytes/cput));
	}
	fprintf(stdout,
		"ttcp%s: %d I/O calls, msec/call = %.3f, calls/sec = %.3f\n",
		trans?"-t":"-r",
		numCalls,
		1024.0 * realt/((double)numCalls),
		((double)numCalls)/realt);
	fprintf(stdout,"ttcp%s: %s\n", trans?"-t":"-r", stats);
	if (verbose) {
	    fprintf(stdout,
		"ttcp%s: buffer address %#x\n",
		trans?"-t":"-r",
		buf);
	}
	close ( fd );
	if (verbose) {
		fprintf(stdout,
			"ttcp%s: File-Descriptor 0x%x Closed\n" ,
			trans?"-t":"-r", fd );
	}
	exit(0);

usage:
	fprintf(stderr,Usage);
	exit(1);
}

void
err(s)
char *s;
{
	fprintf(stderr,"ttcp%s: ", trans?"-t":"-r");
	perror(s);
	fprintf(stderr,"ttcp%s: errno=%d\n",trans?"-t":"-r",errno);
	exit(1);
}

void
mes(s)
char *s;
{
	fprintf(stderr,"ttcp%s: %s\n", trans?"-t":"-r", s);
}

pattern( cp, cnt )
register char *cp;
register int cnt;
{
	register char c;
	c = 0;
	while( cnt-- > 0 )  {
		while( !isprint((c&0x7F)) )  c++;
		*cp++ = (c++&0x7F);
	}
}

char *
outfmt(b)
double b;
{
    static char obuf[50];
    switch (fmt) {
	case 'G':
	    sprintf(obuf, "%.3f GB", b / 1024.0 / 1024.0 / 1024.0);
	    break;
	default:
	case 'K':
	    sprintf(obuf, "%.3f KB", b / 1024.0);
	    break;
	case 'M':
	    sprintf(obuf, "%.3f MB", b / 1024.0 / 1024.0);
	    break;
	case 'g':
	    sprintf(obuf, "%.3f Gbit", b * 8.0 / 1024.0 / 1024.0 / 1024.0);
	    break;
	case 'k':
	    sprintf(obuf, "%.3f Kbit", b * 8.0 / 1024.0);
	    break;
	case 'm':
	    sprintf(obuf, "%.3f Mbit", b * 8.0 / 1024.0 / 1024.0);
	    break;
    }
    return obuf;
}

static struct	timeval time0;	/* Time at which timing started */
static struct	rusage ru0;	/* Resource utilization at the start */

static void prusage();
static void tvadd();
static void tvsub();
static void psecs();

#if defined(SYSV) && !defined(__osf__) && !defined(__linux__)
/*ARGSUSED*/
static
getrusage(ignored, ru)
    int ignored;
    register struct rusage *ru;
{
    struct tms buf;
#if defined(NT)
    HANDLE phd;
    FILETIME CreateTime, ExitTime, KernelTime, UserTime;
    SYSTEMTIME SysTime;
    phd = GetCurrentProcess();
    if( GetProcessTimes(phd, &CreateTime, &ExitTime, &KernelTime, &UserTime) != TRUE) {
        ru->ru_stime.tv_sec  = 0;
        ru->ru_stime.tv_usec = 0;
        ru->ru_utime.tv_sec  = 0;
        ru->ru_utime.tv_usec = 0;
    } else {
        (void) FileTimeToSystemTime(&KernelTime, &SysTime);
/*
	    fprintf(stdout,
	    "System sec=%d, msec=%d\n", SysTime.wSecond, SysTime.wMilliseconds);
*/
        ru->ru_stime.tv_sec  = SysTime.wSecond; 
        ru->ru_stime.tv_usec = SysTime.wMilliseconds * 1000;
        (void) FileTimeToSystemTime(&UserTime, &SysTime);
/*
	    fprintf(stdout,
	    "   User sec=%d, msec=%d\n", SysTime.wSecond, SysTime.wMilliseconds);
*/
        ru->ru_utime.tv_sec  = SysTime.wSecond;
        ru->ru_utime.tv_usec = SysTime.wMilliseconds * 1000;
    }
#else /* !NT */
    times(&buf);

    /* Assumption: HZ <= 2147 (LONG_MAX/1000000) */
    ru->ru_stime.tv_sec  = buf.tms_stime / HZ;
    ru->ru_stime.tv_usec = ((buf.tms_stime % HZ) * 1000000) / HZ;
    ru->ru_utime.tv_sec  = buf.tms_utime / HZ;
    ru->ru_utime.tv_usec = ((buf.tms_utime % HZ) * 1000000) / HZ;
#endif /* !NT */
}

#if !defined(__hpux) && !defined(_AIX) && !defined(sun)
/*ARGSUSED*/
static 
gettimeofday(tp, zp)
    struct timeval *tp;
    struct timezone *zp;
{
#if defined(NT)
    struct _timeb timeptr;

    _ftime(&timeptr);
    tp->tv_sec = timeptr.time;
    tp->tv_usec = timeptr.millitm * 1000;
#else /* !NT */
    tp->tv_sec = time(0);
    tp->tv_usec = 0;
#endif /* !NT */
}
#endif /* !__hpux && !_AIX && !sun */
#endif /* SYSV && !__osf__ && !__linux__ */

/*
 *			P R E P _ T I M E R
 */
void
prep_timer()
{
	gettimeofday(&time0, (struct timezone *)0);
	getrusage(RUSAGE_SELF, &ru0);
}

/*
 *			R E A D _ T I M E R
 * 
 */
double
read_timer(str,len)
char *str;
{
	struct timeval timedol;
	struct rusage ru1;
	struct timeval td;
	struct timeval tend, tstart;
	char line[132];

	getrusage(RUSAGE_SELF, &ru1);
	gettimeofday(&timedol, (struct timezone *)0);
	prusage(&ru0, &ru1, &timedol, &time0, line);
	(void)strncpy( str, line, len );

	/* Get real time */
	tvsub( &td, &timedol, &time0 );
	realt = td.tv_sec + ((double)td.tv_usec) / 1000000;

	/* Get CPU time (user+sys) */
	tvadd( &tend, &ru1.ru_utime, &ru1.ru_stime );
	tvadd( &tstart, &ru0.ru_utime, &ru0.ru_stime );
	tvsub( &td, &tend, &tstart );
	cput = td.tv_sec + ((double)td.tv_usec) / 1000000;
	if( cput < 0.00001 )  cput = 0.00001;
	return( cput );
}

static void
prusage(r0, r1, e, b, outp)
	register struct rusage *r0, *r1;
	struct timeval *e, *b;
	char *outp;
{
	struct timeval tdiff;
	register time_t t;
	register char *cp;
	register int i;
	int ms;

	t = (r1->ru_utime.tv_sec-r0->ru_utime.tv_sec)*100+
	    (r1->ru_utime.tv_usec-r0->ru_utime.tv_usec)/10000+
	    (r1->ru_stime.tv_sec-r0->ru_stime.tv_sec)*100+
	    (r1->ru_stime.tv_usec-r0->ru_stime.tv_usec)/10000;
	ms =  (e->tv_sec-b->tv_sec)*100 + (e->tv_usec-b->tv_usec)/10000;

#define END(x)	{while(*x) x++;}
#if defined(SYSV) && !defined(__osf__) && !defined(__linux__)
	cp = "%Uuser %Ssys %Ereal %P";
#else
#if defined(sgi)		/* IRIX 3.3 will show 0 for %M,%F,%R,%C */
	cp = "%Uuser %Ssys %Ereal %P %Mmaxrss %F+%Rpf %Ccsw";
#else
	cp = "%Uuser %Ssys %Ereal %P %Xi+%Dd %Mmaxrss %F+%Rpf %Ccsw";
#endif
#endif
	for (; *cp; cp++)  {
		if (*cp != '%')
			*outp++ = *cp;
		else if (cp[1]) switch(*++cp) {

		case 'U':
			tvsub(&tdiff, &r1->ru_utime, &r0->ru_utime);
			sprintf(outp,"%d.%03d", tdiff.tv_sec, tdiff.tv_usec/1000);
			END(outp);
			break;

		case 'S':
			tvsub(&tdiff, &r1->ru_stime, &r0->ru_stime);
			sprintf(outp,"%d.%03d", tdiff.tv_sec, tdiff.tv_usec/1000);
			END(outp);
			break;

		case 'E':
			psecs(ms / 100, outp);
			END(outp);
			break;

		case 'P':
			sprintf(outp,"%d%%", (int) (t*100 / ((ms ? ms : 1))));
			END(outp);
			break;

#if !defined(SYSV) || defined(__osf__) || defined(__linux__)
		case 'W':
			i = r1->ru_nswap - r0->ru_nswap;
			sprintf(outp,"%d", i);
			END(outp);
			break;

		case 'X':
			sprintf(outp,"%d", t == 0 ? 0 : (r1->ru_ixrss-r0->ru_ixrss)/t);
			END(outp);
			break;

		case 'D':
			sprintf(outp,"%d", t == 0 ? 0 :
			    (r1->ru_idrss+r1->ru_isrss-(r0->ru_idrss+r0->ru_isrss))/t);
			END(outp);
			break;

		case 'K':
			sprintf(outp,"%d", t == 0 ? 0 :
			    ((r1->ru_ixrss+r1->ru_isrss+r1->ru_idrss) -
			    (r0->ru_ixrss+r0->ru_idrss+r0->ru_isrss))/t);
			END(outp);
			break;

		case 'M':
			sprintf(outp,"%d", r1->ru_maxrss/2);
			END(outp);
			break;

		case 'F':
			sprintf(outp,"%d", r1->ru_majflt-r0->ru_majflt);
			END(outp);
			break;

		case 'R':
			sprintf(outp,"%d", r1->ru_minflt-r0->ru_minflt);
			END(outp);
			break;

		case 'I':
			sprintf(outp,"%d", r1->ru_inblock-r0->ru_inblock);
			END(outp);
			break;

		case 'O':
			sprintf(outp,"%d", r1->ru_oublock-r0->ru_oublock);
			END(outp);
			break;
		case 'C':
			sprintf(outp,"%d+%d", r1->ru_nvcsw-r0->ru_nvcsw,
				r1->ru_nivcsw-r0->ru_nivcsw );
			END(outp);
			break;
#endif /* !SYSV || __osf__ || __linux__ */
		}
	}
	*outp = '\0';
}

static void
tvadd(tsum, t0, t1)
	struct timeval *tsum, *t0, *t1;
{

	tsum->tv_sec = t0->tv_sec + t1->tv_sec;
	tsum->tv_usec = t0->tv_usec + t1->tv_usec;
	if (tsum->tv_usec > 1000000)
		tsum->tv_sec++, tsum->tv_usec -= 1000000;
}

static void
tvsub(tdiff, t1, t0)
	struct timeval *tdiff, *t1, *t0;
{

	tdiff->tv_sec = t1->tv_sec - t0->tv_sec;
	tdiff->tv_usec = t1->tv_usec - t0->tv_usec;
	if (tdiff->tv_usec < 0)
		tdiff->tv_sec--, tdiff->tv_usec += 1000000;
}

static void
psecs(l,cp)
long l;
register char *cp;
{
	register int i;

	i = l / 3600;
	if (i) {
		sprintf(cp,"%d:", i);
		END(cp);
		i = l % 3600;
		sprintf(cp,"%d%d", (i/60) / 10, (i/60) % 10);
		END(cp);
	} else {
		i = l;
		sprintf(cp,"%d", i / 60);
		END(cp);
	}
	i %= 60;
	*cp++ = ':';
	sprintf(cp,"%d%d", i / 10, i % 10);
}

/*
 *			N R E A D
 */
Nread( fd, buf, count )
int fd;
void *buf;
int count;
{
	struct sockaddr_in from;
	int len = sizeof(from);
	register int cnt;
	if( udp )  {
		cnt = recvfrom( fd, buf, count, 0, &from, &len );
		numCalls++;
	} else {
		if( b_flag )
			cnt = mread( fd, buf, count );	/* fill buf */
		else {
#if defined(NT)
			cnt = recv( fd, buf, count, 0 );
#else
			cnt = read( fd, buf, count );
#endif
			numCalls++;
		}
		if (touchdata && cnt > 0) {
			register int c = cnt, sum;
			register char *b = buf;
			while (c--)
				sum += *b++;
		}
	}
	return(cnt);
}

/*
 *			N W R I T E
 */
Nwrite( fd, buf, count )
int fd;
void *buf;
int count;
{
	register int cnt;
	if( udp )  {
again:
		cnt = sendto( fd, buf, count, 0, &sinhim, sizeof(sinhim) );
		numCalls++;
#if defined(NT)
		if( cnt<0 && WSAENOBUFS == WSAGetLastError()) {
#else /* !NT */
		if( cnt<0 && errno == ENOBUFS )  {
#endif /* NT */
			delay(18000);
			errno = 0;
			goto again;
		}
	} else {
#if defined(NT)
		cnt = send( fd, buf, count, 0 );
#else
		cnt = write( fd, buf, count );
#endif
		numCalls++;
	}
	return(cnt);
}

void
delay(us)
{
	struct timeval tv;

	tv.tv_sec = 0;
	tv.tv_usec = us;
	(void)select( 1, (char *)0, (char *)0, (char *)0, &tv );
}

/*
 *			M R E A D
 *
 * This function performs the function of a read(II) but will
 * call read(II) multiple times in order to get the requested
 * number of characters.  This can be necessary because
 * network connections don't deliver data with the same
 * grouping as it is written with.  Written by Robert S. Miles, BRL.
 */
int
mread(fd, bufp, n)
int fd;
register char	*bufp;
unsigned	n;
{
	register unsigned	count = 0;
	register int		nread;

	do {
#if defined(NT)
		nread = recv(fd, bufp, n-count, 0);
#else
		nread = read(fd, bufp, n-count);
#endif
		numCalls++;
		if(nread < 0)  {
			perror("ttcp_mread");
			return(-1);
		}
		if(nread == 0)
			return((int)count);
		count += (unsigned)nread;
		bufp += nread;
	 } while(count < n);

	return((int)count);
}
