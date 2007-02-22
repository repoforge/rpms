#if !defined(MAY_NOT_MODIFY)
/****==========------------------------------------------------==========****/
/*                                                                          */
/* tcpshow, v1.0                                                            */
/*                                                                          */
/* Quickie to decode a "tcpdump" savefile.                                  */
/*                                                                          */
/* The application data is displayed as ASCII -- application protocols are  */
/* not decoded.                                                             */
/*                                                                          */
/* The data captured by "tcpdump" might be less than in the original        */
/* packet.  We kludge a solution to this with setjmp()/longjmp().           */
/*                                                                          */
/* Although written to read tcpdump savefiles, with tcpdump itself as a     */
/* front-end, it'll decode any hex dump that adheres to the format          */
/* expected.  Some programs which capture network data offer an option to   */
/* save the trace to a file in hex format -- this can often be massaged     */
/* easily with Perl/awk/sh scripts to turn it into the format expected.     */
/* As a special case, "tcpdump -s 1518 -lenx | tcpshow -cooked" works       */
/* rather well, and "tcpdump -s 1518 -lenx | tcpshow -cooked -data" is nice */
/* for watching the data traffic in real time.                              */
/*                                                                          */
/* ------------------------------------------------------------------------ */
/*                                                                          */
/* Copyright (c) 1996 I.T. NetworX Ltd.  All rights reserved.               */
/*                                                                          */
/* This source code is owned and copyrighted by I.T. NetworX Ltd.  This     */
/* file and all files derived from it, directly or indirectly (such files   */
/* collectively and separately being referred to henceforth as "this file") */
/* may be used, modified and redistributed subject to the following six     */
/* Conditions.                                                              */
/*                                                                          */
/* Condition 1 of 6:                                                        */
/* That all text (code/comments, etc.) in this file surrounded by the macro */
/* block "#if !defined(MAY_NOT_MODIFY) ... #endif", including the macro     */
/* statements themselves, may not be modified in any way, or deleted.  In   */
/* particular, this comment block and the printf() statements identifying   */
/* I.T. NetworX as being the copyright owner, in the function usage(), may  */
/* not be modified or deleted.  The single, only, exception to this is that */
/* the non-inclusion of C comments by a C compiler/linker, in the object    */
/* and executable images it produces, is permitted.                         */
/*                                                                          */
/* Condition 2 of 6:                                                        */
/* That no financial gain be made from using this file or modifying this    */
/* file.  It is permitted to charge for redistributing this file.           */
/*                                                                          */
/* Condition 3 of 6:                                                        */
/* That no conditions other than these six Conditions be applied to the     */
/* use, modification or redistribution of this file.                        */
/*                                                                          */
/* Condition 4 of 6:                                                        */
/* That all modifications to this file show prominently the name of the     */
/* person that made the change and the date on which the change was made.   */
/*                                                                          */
/* Condition 5 of 6:                                                        */
/* That I.T. NetworX, its employees, agents and everybody else in the world */
/* dead, living and yet to be born, are hereby free from liability of all   */
/* and every kind arising from the use of this file by anybody for any      */
/* purpose.  This file comes "as is" and all warranties, express or         */
/* implied, are disclaimed.  As the manual page for chat(1) says, "if it    */
/* breaks, then you get to keep both pieces".                               */
/*                                                                          */
/* Condition 6 of 6:                                                        */
/* That I.T. NetworX reserves the right to alter these Conditions at any    */
/* time without giving prior notice, such alterations to apply only to the  */
/* version current at the time of issue of the alterations and all later    */
/* versions, and such alterations to apply only to versions produced        */
/* exclusively by I.T. NetworX or its agents.                               */
/*                                                                          */
/* Addendum to Copyright:                                                   */
/* I'm not a legal eagle and I worded the above notice off the top of my    */
/* head, so it may be full of holes, but the spirit of my intentions are    */
/* clear from reading it.  Please respect these intentions.                 */
/*                                                                          */
/* Me too:                                                                  */
/* If anybody makes significant improvements to this file, such as adding   */
/* decode support for DNS traffic or IP and TCP options, I would appreciate */
/* it if they sent me a copy of their work (mike@NetworX.ie).  Thanks.      */
/*                                                                          */
/* ------------------------------------------------------------------------ */
/*                                                                          */
/* File layout is as follows:                                               */
/* system includes                                                          */
/* local includes                                                           */
/* #define macros                                                           */
/* typedefs                                                                 */
/* declarations of extern variables                                         */
/* declarations of extern functions                                         */
/* declarations of global variables                                         */
/* declarations of global functions                                         */
/* declarations of static variables                                         */
/* declarations of static functions                                         */
/* definitions of functions                                                 */
/* (all functions and variables are declared/defined in alphabetical order) */
/*                                                                          */
/* ------------------------------------------------------------------------ */
/*                                                                          */
/* Compiles as follows:                                                     */
/* cc -s -O -o tcpshow tcpshow.c                                            */
/*                                                                          */
/* ------------------------------------------------------------------------ */
/*                                                                          */
/* Who and when:                                                            */
/* MikeRyan, 11apr96.                                                       */
/*                                                                          */
/* I.T. NetworX,                                                            */
/* 67 Merrion Square,                                                       */
/* Dublin 2,                                                                */
/* Ireland.                                                                 */
/* Phone: +353-1-676-8866                                                   */
/* Fax:   +353-1-676-8868                                                   */
/* Email: mike@NetworX.ie                                                   */
/*                                                                          */
/* ------------------------------------------------------------------------ */
/*                                                                          */
/* Modification History                                                     */
/* MikeRyan, 14may96: Allow "tcpdump" expressions to be passed in.          */
/* MikeRyan, 15may96: Added UDP decode logic.                               */
/* MikeRyan, 16may96: Added ICMP decode logic.                              */
/* MikeRyan, 16may96: Added -b switch to break long lines                   */
/*                          -w option to specify the width of the page      */
/*                          -h flag to give help on usage.                  */
/* MikeRyan, 28may96: Added -nolink                                         */
/*                          -nodata                                         */
/*                          -noip                                           */
/*                          -track                                          */
/*                          -terse                                          */
/*                          -sb                                             */
/*                          -s                                              */
/* MikeRyan, 25jun96: Incorporated my "general.h" typedef's, so that the    */
/* present source file doesn't depend on any non-standard header files.     */
/* This allows it to be distributed as a single file.  Also included the    */
/* copyright notice, as I'm making the program freely available.            */
/*                                                                          */
/* MikeRyan, 26jun96: Added -cooked                                         */
/*                          -pp                                             */
/*                                                                          */
/****==========------------------------------------------------==========****/
#endif


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <netdb.h>
#include <setjmp.h>


/* Some general defines.                                                    */
#if defined(FALSE)
#undef FALSE
#endif
#if defined(TRUE)
#undef TRUE
#endif
#define FALSE        (boolean)0
#define TRUE         (boolean)1
#define elif            else if
#if !defined(reg)
#define reg            register        /* For debugging purposes            */
#endif


#define VERSION             1.0        /* Please change when appropriate    */
#define COOKER        "tcpdump"
#define MAXCOOKARGS         100        /* Max tcpdump expression words      */

#define MAXPKT            10240        /* Should be 1518 for Ethernet       */
#define NCOLS                60

/* IP header elements.                                                      */
#define IPHDRLEN             20
#define FRAGOFF          0x1FFF
#define MF               0x2000
#define DF               0x4000

/* TCP header elements.                                                     */
#define TCPHDRLEN            20
#define URG              0x0020
#define ACK              0x0010
#define PSH              0x0008
#define RST              0x0004
#define SYN              0x0002
#define FIN              0x0001

/* UDP header elements.                                                     */
#define UDPHDRLEN             8

/* ICMP header elements.                                                    */
#define ICMPHDRLEN            4

/* IP protocol types.                                                       */
#define IP                    0
#define ICMP                  1
#define IGMP                  2
#define GGP                   3
#define IPENCAP               4
#define ST                    5
#define TCP                   6
#define EGP                   8
#define PUP                  12
#define UDP                  17
#define HMP                  20
#define XNSIDP               22
#define RDP                  27
#define ISOTP4               29
#define XTP                  36
#define IDPRCMTP             39
#define RSVP                 46
#define VMTP                 81
#define OSPF                 89
#define IPIP                 94
#define ENCAP                98

/* ICMP types.                                                              */
#define ECHO_REPLY            0
#define DST_UNREACH           3
#define SRC_QUENCH            4
#define REDIRECT              5
#define ECHO_REQ              8
#define ROUTER_AD             9
#define ROUTER_SOL           10
#define TIME_EXCEED          11
#define PARAM_PROB           12
#define TIME_REQ             13
#define TIME_REPLY           14
#define INFO_REQ             15
#define INFO_REPLY           16
#define MASK_REQ             17
#define MASK_REPLY           18

/* ICMP codes for type == Destination Unreachable.                          */
#define NET_UNREACH           0
#define HOST_UNREACH          1
#define PROTO_UNREACH         2
#define PORT_UNREACH          3
#define DF_SET                4
#define SRCROUTE_FAILED       5
#define DSTNET_UNKNOWN        6
#define DSTHOST_UNKNOWN       7
#define SRCHOST_ISOLATED      8
#define DSTNET_PROHIB         9
#define DSTHOST_PROHIB       10
#define NET_UNREACH_TOS      11
#define HOST_UNREACH_TOS     12
#define COMM_PROHIB          13
#define HOST_PREC_VIOL       14
#define PREC_CUTOFF          15

/* ICMP codes for type == Redirect.                                         */
#define REDIR_FOR_NET         0
#define REDIR_FOR_HOST        1
#define REDIR_FOR_TOSNET      2
#define REDIR_FOR_TOSHOST     3

/* ICMP codes for type == Time Exceeded.                                    */
#define TTL_ZERO              0
#define REASS_TIMEOUT         1

/* ICMP codes for type == Parameter Problem.                                */
#define IP_HDR_BAD            0
#define MISSING_OPT           1

/* Skip remaining lines of current packet.  Note that this causes a         */
/* longjmp(), so a succeeding "return" from a function isn't needed.        */
#define nextpkt()   for ( ; ; ) (void)getpkt()
/* Display a separator line between packet decodes.                         */
#define prsep() \
printf( \
   "-----------------------------------------------------------------\n" \
)


/* My own preferred basic data types -- amend per target machine.           */
typedef char boolean;
typedef float float4;
typedef double float8;
typedef char int1;
typedef short int2;
typedef int int4;
typedef unsigned char uint1;
typedef unsigned short uint2;
typedef unsigned int uint4;
typedef unsigned char uchar;


void main(int, char **);


static boolean bflag = FALSE;
static char *cookargs[MAXCOOKARGS+1];
static boolean cookedflag = FALSE;
static boolean dataflag = FALSE;
static uint2 datalen = 0;
static char *dflt_cookargs[] = {
   COOKER, "-enx", "-s10240", "-r-", (char *)NULL
};
static char dip[16];
static boolean isip;
static jmp_buf jmpbuf;
static boolean nodataflag = FALSE;
static boolean noipflag = FALSE;
static boolean nolinkflag = FALSE;
static int npkts_shown = 0;
static char *off = "off,";             /* "off" in middle of list           */
static char *off_e = "off";            /* "off" at end of list              */
static char *on = "on, ";              /* "on" in middle of list            */
static char *on_e = "on";              /* "on" at end of list               */
static int pagewidth = NCOLS;
static char *pkt;
static boolean ppflag = FALSE;
static uint1 proto;
static boolean sflag = FALSE;
static boolean sbflag = FALSE;
static char sip[16];
static boolean terseflag = FALSE;
static boolean trackflag = FALSE;
static char *unknown = "<unknown>";


static void error(char *);
static char *etheraddr(char *);
static char *ether_proto(char *);
static void fork_tcpdump(int, char **);
static uint1 getbyte(char **);
static uint4 getlongword(char **);
static char *getpkt(void);
static uint2 getword(char **);
static char *icmpcode(uint1, uint1);
static char *icmptype(uint1);
static char *ipaddr(char **);
static char *ip_proto(uint1);
static char nextchar(char **);
static char *rmwspace(char *);
static char *showdata(char *);
static char *showhdr(char *);
static char *showicmp(char *);
static char *showip(char *);
static void showpkt(char *);
static char *showtcp(char *);
static char *showudp(char *);
static char *skip(char *, uint2);
static char *svcname(uint2, char *, boolean);
static void usage(void);


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Print an error message and exit.                                         */
/*                                                                          */
/****==========------------------------------------------------==========****/

static void error (
   char *msg
) {

   fprintf(stderr, "***Error: %s\n", msg);
   exit(1);

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Print a formatted Ethernet address.                                      */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *etheraddr (
   char *eaddr
) {

   static char formatted[18];
   int i;
   int j;


   for (i = j = 0; i < 6; i++)
      if (eaddr[1] == ':') {
         formatted[j++] = '0';
         formatted[j++] = toupper(eaddr[0]);
         formatted[j++] = ':';
         eaddr += 2;
      }
      else {
         formatted[j++] = toupper(eaddr[0]);
         formatted[j++] = toupper(eaddr[1]);
         formatted[j++] = ':';
         eaddr += 3;
      }
   formatted[j-1] = '\0';

   return formatted;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Print the type of protocol encapsulated in the Ethernet frame.           */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *ether_proto (
   char *type
) {

   if (strcmp(type, "0800") == 0)
      return "IP";
   elif (strcmp(type, "0806") == 0)
      return "ARP";
   elif (strcmp(type, "8035") == 0)
      return "RARP";
   else
      return type;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Run tcpdump to pre-process the trace file.                               */
/*                                                                          */
/****==========------------------------------------------------==========****/

static void fork_tcpdump (
   int argc,
   char **argv
) {

   int fd[2];
   int i;
   pid_t pid;


   /* Required "tcpdump" flags.                                             */
   i = 0;
   while (dflt_cookargs[i]) {
      cookargs[i] = dflt_cookargs[i];
      i++;
   }
   while (argc-- > 0) {
      if (i >= MAXCOOKARGS) error("Too many expressions");
      cookargs[i++] = *argv++;
   }
   cookargs[i] = (char *)NULL;

   /* Fork tcpdump to cook our input.                                       */
   if (pipe(fd)) error("pipe() failed");
   if ((pid=fork()) < 0) error("fork() failed");
   if (pid == 0) {
      (void)close(1);
      if (dup(fd[1]) != 1) error("dup() failed");
      (void)close(fd[0]);
      (void)close(fd[1]);
      execvp(COOKER, cookargs);
      error("execvp() failed");
   }

   (void)close(0);
   if (dup(fd[0]) != 0) error("dup() failed");
   (void)close(fd[0]);
   (void)close(fd[1]);

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Return the byte value and increment the pointer by sizeof(byte).         */
/*                                                                          */
/****==========------------------------------------------------==========****/

static uint1 getbyte (
   char **pkt
) {

   char byte[1*2+1];                   /* ASCII representation of a byte    */
   unsigned int val;


   byte[0] = nextchar(pkt);
   byte[1] = nextchar(pkt);
   byte[2] = '\0';

   (void)sscanf(byte, "%x", &val);

   return (uint1)val;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Return the longword value and increment the pointer by sizeof(longword). */
/*                                                                          */
/****==========------------------------------------------------==========****/

static uint4 getlongword (
   char **pkt
) {

   char longword[4*2+1];              /* ASCII representation of a longword */
   unsigned long val;


   longword[0] = nextchar(pkt);
   longword[1] = nextchar(pkt);
   longword[2] = nextchar(pkt);
   longword[3] = nextchar(pkt);
   longword[4] = nextchar(pkt);
   longword[5] = nextchar(pkt);
   longword[6] = nextchar(pkt);
   longword[7] = nextchar(pkt);
   longword[8] = '\0';

   (void)sscanf(longword, "%lx", &val);

   return (uint4)val;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Read in the next line of packet data.                                    */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *getpkt (
) {

   static boolean been_here_already = FALSE;
   static char pktbuf[MAXPKT+1];


   if (fgets(pktbuf, MAXPKT+1, stdin) == (char *)NULL) exit(0);

   /* Line without leading <tab> means start of new packet.                 */
   if (*pktbuf == '\t')
      return rmwspace(pktbuf);
   elif (! been_here_already) {        /* setjmp() won't have been called   */
      been_here_already = TRUE;        /*  before reading 1st packet        */
      return pkt = pktbuf;
   }
   else {
      if (datalen > 0)
         printf("\n\t<*** Rest of data missing from packet dump ***>\n");
      pkt = pktbuf;
      longjmp(jmpbuf, 1);
   }

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Return the word value and increment the pointer by sizeof(word).         */
/*                                                                          */
/****==========------------------------------------------------==========****/

static uint2 getword (
   char **pkt
) {

   char word[2*2+1];                   /* ASCII representation of a word    */
   unsigned int val;


   word[0] = nextchar(pkt);
   word[1] = nextchar(pkt);
   word[2] = nextchar(pkt);
   word[3] = nextchar(pkt);
   word[4] = '\0';

   (void)sscanf(word, "%x", &val);

   return (uint2)val;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Print the code relating to the ICMP type.                                */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *icmpcode (
   uint1 type,
   uint1 code
) {

   char *bad;
   char *descr;


   bad = "<*** CORRUPT ***>";
   descr = (char *)NULL;

   switch (type) {
    case ECHO_REPLY:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case DST_UNREACH:
      switch (code) {
       case NET_UNREACH:       descr = "network-unreachable";           break;
       case HOST_UNREACH:      descr = "host-unreachable";              break;
       case PROTO_UNREACH:     descr = "protocol-unreachable";          break;
       case PORT_UNREACH:      descr = "port-unreachable";              break;
       case DF_SET:            descr = "frag-needed-but-DF-set";        break;
       case SRCROUTE_FAILED:   descr = "source-route-failed";           break;
       case DSTNET_UNKNOWN:    descr = "destination-network-unknown";   break;
       case DSTHOST_UNKNOWN:   descr = "destination-host-unknown";      break;
       case SRCHOST_ISOLATED:  descr = "source-host-isolated";          break;
       case DSTNET_PROHIB:     descr = "dest-net-admin-prohibited";     break;
       case DSTHOST_PROHIB:    descr = "dest-host-admin-prohibited";    break;
       case NET_UNREACH_TOS:   descr = "network-unreachable-for-TOS";   break;
       case HOST_UNREACH_TOS:  descr = "host-unreachable-for-TOS";      break;
       case COMM_PROHIB:       descr = "trafffic-prohibited-by-filter"; break;
       case HOST_PREC_VIOL:    descr = "host-precedence-violation";     break;
       case PREC_CUTOFF:       descr = "precedence-cutoff-in-effect";   break;
       default:                descr = bad;                             break;
      }
      break;
    case SRC_QUENCH:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case REDIRECT:
      switch (code) {
       case REDIR_FOR_NET:     descr = "route-wrong-for-network";       break;
       case REDIR_FOR_HOST:    descr = "route-wrong-for-host";          break;
       case REDIR_FOR_TOSNET:  descr = "route-wrong-for-TOS-and-net";   break;
       case REDIR_FOR_TOSHOST: descr = "route-wrong-for-TOS-and-host";  break;
       default:                descr = bad;                             break;
      }
      break;
    case ECHO_REQ:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case ROUTER_AD:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case ROUTER_SOL:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case TIME_EXCEED:
      switch (code) {
       case TTL_ZERO:          descr = "TTL-reached-zero";              break;
       case REASS_TIMEOUT:     descr = "reassembly-timer-expired";      break;
       default:                descr = bad;                             break;
      }
      break;
    case PARAM_PROB:
      switch (code) {
       case IP_HDR_BAD:        descr = "IP-header-bad";                 break;
       case MISSING_OPT:       descr = "required-option-is-missing";    break;
       default:                descr = bad;                             break;
      }
      break;
    case TIME_REQ:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case TIME_REPLY:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case INFO_REQ:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case INFO_REPLY:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case MASK_REQ:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    case MASK_REPLY:
      switch (code) {
       case 0:                                                          break;
       default:                descr = bad;                             break;
      }
      break;
    default:
      break;
   }

   return descr;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Print the type of ICMP packet.                                           */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *icmptype (
   uint1 type
) {

   char *descr;


   switch (type) {
    case ECHO_REPLY:  descr = "echo-reply";              break;
    case DST_UNREACH: descr = "destination-unreachable"; break;
    case SRC_QUENCH:  descr = "source-quench";           break;
    case REDIRECT:    descr = "redirect";                break;
    case ECHO_REQ:    descr = "echo-request";            break;
    case ROUTER_AD:   descr = "router-advertisement";    break;
    case ROUTER_SOL:  descr = "router-solicitation";     break;
    case TIME_EXCEED: descr = "time-exceeded";           break;
    case PARAM_PROB:  descr = "parameter-problem";       break;
    case TIME_REQ:    descr = "timestamp-request";       break;
    case TIME_REPLY:  descr = "timestamp-reply";         break;
    case INFO_REQ:    descr = "information-request";     break;
    case INFO_REPLY:  descr = "information-reply";       break;
    case MASK_REQ:    descr = "address-mask-request";    break;
    case MASK_REPLY:  descr = "address-mask-reply";      break;
    default:          descr = unknown;                   break;
   }

   return descr;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Print the IP address in dotted-quad.                                     */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *ipaddr (
   char **pkt
) {

   static char addr[16];
   uint2 byte1;
   uint2 byte2;
   uint2 byte3;
   uint2 byte4;


   /* We don't use inet_ntoa() because it wants a socket structure.         */
   byte1 = (uint2)getbyte(pkt);
   byte2 = (uint2)getbyte(pkt);
   byte3 = (uint2)getbyte(pkt);
   byte4 = (uint2)getbyte(pkt);
   (void)sprintf(addr, "%d.%d.%d.%d", byte1, byte2, byte3, byte4);

   return addr;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Print the type of protocol encapsulated in the IP datagram.              */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *ip_proto (
   uint1 code
) {

   char *name;


   /* A simple table won't do, as the codes aren't contiguous.               */
   switch (code) {
    case IP:
       name = "IP"; break;
    case ICMP:
       name = "ICMP"; break;
    case IGMP:
       name = "IGMP"; break;
    case GGP:
       name = "GGP"; break;
    case IPENCAP:
       name = "IPENCAP"; break;
    case ST:
       name = "ST"; break;
    case TCP:
       name = "TCP"; break;
    case EGP:
       name = "EGP"; break;
    case PUP:
       name = "PUP"; break;
    case UDP:
       name = "UDP"; break;
    case HMP:
       name = "HMP"; break;
    case XNSIDP:
       name = "XNSIDP"; break;
    case RDP:
       name = "RDP"; break;
    case ISOTP4:
       name = "ISOTP4"; break;
    case XTP:
       name = "XTP"; break;
    case IDPRCMTP:
       name = "IDPRCMTP"; break;
    case RSVP:
       name = "RSVP"; break;
    case VMTP:
       name = "VMTP"; break;
    case OSPF:
       name = "OSPF"; break;
    case IPIP:
       name = "IPIP"; break;
    case ENCAP:
       name = "ENCAP"; break;
    default:
       name = unknown; break;
   }

   return name;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Decode a "tcpdump" savefile.                                             */
/*                                                                          */
/****==========------------------------------------------------==========****/

void main (
   int argc,
   char **argv
) {

   /* Command line options.                                                 */
   while (--argc > 0 && **++argv == '-')
      if (strcmp(*argv, "-data") == 0)
	 dataflag = nolinkflag = noipflag = TRUE;
      elif (strcmp(*argv, "-s") == 0) sflag = TRUE;
      elif (strcmp(*argv, "-b") == 0) bflag = TRUE;
      elif (strcmp(*argv, "-sb") == 0) sbflag = TRUE;
      elif (strcmp(*argv, "-terse") == 0) terseflag = TRUE;
      elif (strcmp(*argv, "-track") == 0) trackflag = TRUE;
      elif (strcmp(*argv, "-nodata") == 0) nodataflag = TRUE;
      elif (strcmp(*argv, "-nolink") == 0) nolinkflag = TRUE;
      elif (strcmp(*argv, "-noip") == 0) noipflag = TRUE;
      elif (strcmp(*argv, "-cooked") == 0) cookedflag = TRUE;
      elif (strcmp(*argv, "-pp") == 0) ppflag = TRUE;
      elif (strcmp(*argv, "-h") == 0) usage();
      elif (strcmp(*argv, "-w") == 0) {
         if (--argc <= 0) error("-w needs a numeric argument");
         if ((pagewidth=atoi(*++argv)) < 1) error("-w value too small");
      }
      else error("Unknown command line flag");

   if (! cookedflag)
      fork_tcpdump(argc, argv);
   elif (argc != 0)
      fprintf(stderr, "input is cooked -- ignoring tcpdump expressions\n");

   pkt = getpkt();
   for ( ; ; ) if (! setjmp(jmpbuf)) showpkt(pkt);

   exit(0);

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Return the next character in the packet buffer.                          */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char nextchar (
   char **pkt
) {

   if (! **pkt) *pkt = getpkt();

   return *(*pkt)++;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Remove whitespace from the buffer.                                       */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *rmwspace (
   reg char *pktbuf
) {

   static char cleanpkt[MAXPKT+1];
   reg char *pkt;


   pkt = cleanpkt;
   while (*pktbuf) {
      if (! isspace(*pktbuf)) *pkt++ = *pktbuf;
      pktbuf++;
   }
   *pkt = '\0';

   return cleanpkt;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Decode the TCP/UDP data.                                                 */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *showdata (
   char *pkt
) {

   uint1 byte;
   int col;
   char *descr;


   if (dataflag)
      putchar('\t');
   elif (terseflag)
      printf("DATA:\t");
   else {
      switch (proto) {
       case TCP:  descr = "TCP";   break;
       case UDP:  descr = "UDP";   break;
       case ICMP: descr = "ICMP";  break;
       default:   descr = unknown; break;
      }
      printf("%s Data\n\t", descr);
   }
   if (nodataflag) {
      uint2 ndatabytes = datalen;
      datalen = 0;
      printf("%d bytes\n", ndatabytes);
      return skip(pkt, ndatabytes);
   }

   if (datalen == 0) {
      printf("<No data>\n");
      return pkt;
   }

   switch (bflag) {
    case TRUE:
      for (col = 1; datalen > 0; datalen--, col++) {
         byte = getbyte(&pkt);
	 if (byte == '\n') {
	    putchar('\n');
	    byte = '\t';
	    col = 0;
         }
	 elif (col > pagewidth) {
            printf("%s\n\t", sbflag? "<break>": "");
	    col = 1;
	 }
         if (byte != '\t' && byte != '\n' && !isprint(byte)) byte = '.';
         putchar(byte);
      }
      break;
    case FALSE:
      for ( ; datalen > 0; datalen--) {
         byte = getbyte(&pkt);
         if (byte == '\n') {
	    putchar('\n');
	    byte = '\t';
         }
         if (byte != '\t' && byte != '\n' && !isprint(byte)) byte = '.';
         putchar(byte);
      }
      break;
    default:
      error("Tri-valued boolean!");
   }
   putchar('\n');

   return pkt;
   
}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Decode the packet header.                                                */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *showhdr (
   char *pkt
) {

   char efrom[18];                     /* Source Ethernet address           */
   char eto[18];                       /* Destination Ethernet address      */
   char time[16];                      /* Packet timestamp                  */
   char etype[20];                     /* Ethernet type (decoded to ASCII)  */


   if (ppflag) {
      (void)sscanf(pkt, "%s", time);
      isip = TRUE;                     /* tcpdump doesn't supply link type  */
      if (! nolinkflag)
	 if (terseflag) printf("TIME:\t%s\n", time);
	 else printf("\tTimestamp:\t\t\t%s\n", time);
      return getpkt();
   }

   (void)sscanf(pkt, "%s %s %s %s", time, efrom, eto, etype);

   isip = (boolean)(strcmp(etype, "0800") == 0);
   (void)strcpy(efrom, etheraddr(efrom));
   (void)strcpy(eto, etheraddr(eto));

   if (! nolinkflag)
      if (terseflag) {
	 printf("TIME:\t%s\n", time);
	 printf("LINK:\t%s -> %s type=%s\n", efrom, eto, ether_proto(etype));
      }
      else {
	 printf("\tTimestamp:\t\t\t%s\n", time);
	 printf("\tSource Ethernet Address:\t%s\n", efrom);
	 printf("\tDestination Ethernet Address:\t%s\n", eto);
	 printf("\tEncapsulated Protocol:\t\t%s\n", ether_proto(etype));
      }

   return getpkt();

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Decode the ICMP header.                                                  */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *showicmp (
   char *pkt
) {

   uint2 cksum;
   uint1 code;
   uint2 nskipped;
   uint1 type;
   char *why;


   type = getbyte(&pkt);  nskipped  = sizeof(type);
   code = getbyte(&pkt);  nskipped += sizeof(code);
   cksum = getword(&pkt); nskipped += sizeof(cksum);

   /* The length of the ICMP packet isn't recorded in the packet itself.    */
   /* Must calculate it from the size of the IP datagram - the IP header.   */
   datalen -= ICMPHDRLEN;

   why = icmpcode(type, code);
   if (dataflag) {
      printf(
         "%s -> %s ICMP%s%s%s%s\n",
         sip, dip,
         why? "\n": " ", icmptype(type), why? " because ": "", why? why: ""
      );
      return pkt;                      /* Header is read; nothing to skip   */
   }

   if (terseflag)
      printf(
	 "ICMP:\t%s%s%s cksum=%04X\n",
	 icmptype(type), why? " because ": "", why? why: "", cksum
      );
   else {
      printf("ICMP Header\n");
      printf(
	 "\tType:\t\t\t\t%s%s%s\n",
	 icmptype(type), why? "\n\tBecause:\t\t\t": "", why? why: ""
      );
      printf("\tChecksum:\t\t\t0x%04X\n", cksum);
   }

   return pkt;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Decode the IP header.                                                    */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *showip (
   char *pkt
) {

   uint2 cksum;
   uint2 dgramlen;
   uint2 flags;
   uint2 hlen;
   uint2 id;
   uint2 nskipped;
   uint1 servtype;
   uint1 ttl;
   uint1 ver;


   ver = getbyte(&pkt);             nskipped  = sizeof(ver);
   if ((ver & 0xF0) != 0x40) {
      if (terseflag) printf("IP:\tnot v4\n");
      else
	 printf(
	    "IP Header\n\t<Not an IPv4 datagram (ver=%d)>\n",
	    (ver & 0xF0) >> 4
	 );
      nextpkt();
   }
   servtype = getbyte(&pkt);        nskipped += sizeof(servtype);
   dgramlen = getword(&pkt);        nskipped += sizeof(dgramlen);
   id = getword(&pkt);              nskipped += sizeof(id);
   flags = getword(&pkt);           nskipped += sizeof(flags);
   ttl = getbyte(&pkt);             nskipped += sizeof(ttl);
   proto = getbyte(&pkt);           nskipped += sizeof(proto);
   cksum = getword(&pkt);           nskipped += sizeof(cksum);
   (void)strcpy(sip, ipaddr(&pkt)); nskipped += 4;
   (void)strcpy(dip, ipaddr(&pkt)); nskipped += 4;
   hlen = (ver & 0x0F) * 4;
   datalen = dgramlen - hlen;

   if (noipflag) return skip(pkt, hlen - nskipped);

   printf("%s", terseflag? "  IP:\t": "IP Header\n");

   if (terseflag) {
      printf(
	 "%s -> %s hlen=%d TOS=%02X dgramlen=%d id=%04X\n",
	 sip, dip, hlen, (uint2)servtype, dgramlen, id
      );
      printf(
	 "\tMF/DF=%s/%s frag=%d TTL=%d proto=%s cksum=%04X\n",
	 (flags & MF) == MF? "1": "0", (flags & DF) == DF? "1": "0",
	 flags & FRAGOFF, ttl, ip_proto(proto), cksum
      );
   }

   else {
      printf("\tVersion:\t\t\t4\n\tHeader Length:\t\t\t%d bytes\n", hlen);
      printf("\tService Type:\t\t\t0x%02X\n", (uint2)servtype);
      printf("\tDatagram Length:\t\t%d bytes\n", dgramlen);
      printf("\tIdentification:\t\t\t0x%04X\n", id);
      printf(
	 "\tFlags:\t\t\t\tMF=%s DF=%s\n",
	 (flags & MF) == MF? on: off, (flags & DF) == DF? on_e: off_e
      );
      printf("\tFragment Offset:\t\t%d\n", flags & FRAGOFF);
      printf("\tTTL:\t\t\t\t%d\n", ttl);
      printf("\tEncapsulated Protocol:\t\t%s\n", ip_proto(proto));
      printf("\tHeader Checksum:\t\t0x%04X\n", cksum);
      printf("\tSource IP Address:\t\t%s\n", sip);
      printf("\tDestination IP Address:\t\t%s\n", dip);
   }

   if (hlen > IPHDRLEN) {
      if (! terseflag) printf("\t<Options not displayed>\n");
      pkt = skip(pkt, hlen - IPHDRLEN);
   }

   return pkt;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Decode the packet chunk in the buffer.                                   */
/*                                                                          */
/****==========------------------------------------------------==========****/

static void showpkt (
   reg char *pkt
) {

   isip = FALSE;

   if (++npkts_shown > 1) prsep();
   if (! dataflag) printf("Packet %d\n", npkts_shown);

   pkt = showhdr(pkt);
   if (! isip) {
      if (! dataflag)
         printf("\t<*** No decode support for non-IP protocols ***>\n");
      nextpkt();                       /* Doesn't return                    */
   }
   pkt = showip(pkt);
   switch (proto) {
    case TCP:
      pkt = showtcp(pkt);
      pkt = showdata(pkt);
      break;
    case UDP:
      pkt = showudp(pkt);
      pkt = showdata(pkt);
      break;
    case ICMP:
      pkt = showicmp(pkt);
      pkt = showdata(pkt);
      break;
    default:
      printf("\t<*** No decode support for encapsulated protocol ***>\n");
      datalen = 0;
      nextpkt();                       /* Doesn't return                    */
   }
   /* "tcpdump" sometimes displays data at the end of a packet which, given */
   /* the recorded Datagram Length, don't belong to the packet.             */
   if (*pkt && sflag)
      printf("\t<*** Spurious data at end: \"%s\" ***>\n", pkt);
   (void)getpkt();                     /* Load start of next packet         */

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Decode the TCP header.                                                   */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *showtcp (
   char *pkt
) {

   uint4 ack;
   uint2 advert;
   uint2 cksum;
   uint2 dport;
   uint4 expect;
   uint2 flags;
   uint2 hlen;
   uint2 nskipped;
   uint4 seq;
   uint2 sport;
   uint2 urgptr;


   sport = getword(&pkt);   nskipped  = sizeof(sport);
   dport = getword(&pkt);   nskipped += sizeof(dport);
   seq = getlongword(&pkt); nskipped += sizeof(seq);
   ack = getlongword(&pkt); nskipped += sizeof(ack);
   flags = getword(&pkt);   nskipped += sizeof(flags);
   advert = getword(&pkt);  nskipped += sizeof(advert);
   cksum = getword(&pkt);   nskipped += sizeof(cksum);
   urgptr = getword(&pkt);  nskipped += sizeof(urgptr);

   hlen = (flags >> 12 & 0x0F) * 4;
   datalen -= hlen;

   if (dataflag) {
      char dname[20];
      char sname[20];
      (void)strcpy(sname, svcname(sport, "tcp", TRUE));
      (void)strcpy(dname, svcname(dport, "tcp", TRUE));
      printf("%s.%s -> %s.%s over TCP\n", sip, sname, dip, dname);
      return skip(pkt, hlen - nskipped);
   }

   if (trackflag) {
      expect = seq + datalen;
      if ((flags & SYN) == SYN || (flags & FIN) == FIN) expect++;
   }

   if (terseflag) {
      printf(" TCP:\tport %d -> %d seq=%010lu", sport, dport, seq);
      if (trackflag) printf(" (expect=%010lu)", expect);
      printf(" ack=%010lu\n", ack);
      printf(
	 "\thlen=%d (data=%u) UAPRSF=%s%s%s%s%s%s",
	 hlen, datalen,
	 (flags & URG) == URG? "1": "0", (flags & ACK) == ACK? "1": "0",
	 (flags & PSH) == PSH? "1": "0", (flags & RST) == RST? "1": "0",
	 (flags & SYN) == SYN? "1": "0", (flags & FIN) == FIN? "1": "0"
      );
      printf(" wnd=%d cksum=%04X urg=%d\n", advert, cksum, urgptr);
   }

   else {
      printf("TCP Header\n");
      printf(
	 "\tSource Port:\t\t\t%d (%s)\n",
	 sport, svcname(sport, "tcp", FALSE)
      );
      printf(
	 "\tDestination Port:\t\t%d (%s)\n",
	 dport, svcname(dport, "tcp", FALSE)
      );
      printf("\tSequence Number:\t\t%010lu\n", seq);
      if (trackflag) printf("\tExpect peer ACK:\t\t%010lu\n", expect);
      printf("\tAcknowledgement Number:\t\t%010lu\n", ack);
      printf("\tHeader Length:\t\t\t%d bytes (data=%u)\n", hlen, datalen);
      printf(
	 "\tFlags:%s%s%s%s%s%s\n%s%s%s%s%s%s\n",
	 "\t\t\t\tURG=",   (flags & URG) == URG? on: off,
	 " ACK=",          (flags & ACK) == ACK? on: off,
	 " PSH=",          (flags & PSH) == PSH? on_e: off_e,
	 "\t\t\t\t\tRST=", (flags & RST) == RST? on: off,
	 " SYN=",          (flags & SYN) == SYN? on: off,
	 " FIN=",          (flags & FIN) == FIN? on_e: off_e
      );
      printf("\tWindow Advertisement:\t\t%d bytes\n", advert);
      printf("\tChecksum:\t\t\t0x%04X\n", cksum);
      printf("\tUrgent Pointer:\t\t\t%d\n", urgptr);
   }

   if (hlen > TCPHDRLEN) {
      if (! terseflag) printf("\t<Options not displayed>\n");
      pkt = skip(pkt, hlen - TCPHDRLEN);
   }

   return pkt;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Decode the UDP header.                                                   */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *showudp (
   char *pkt
) {

   uint2 cksum;
   uint2 dgramlen;
   uint2 dport;
   uint2 nskipped;
   uint2 sport;


   sport     = getword(&pkt); nskipped  = sizeof(sport);
   dport     = getword(&pkt); nskipped += sizeof(dport);
   dgramlen  = getword(&pkt); nskipped += sizeof(dgramlen);
   cksum     = getword(&pkt); nskipped += sizeof(cksum);

   /* The size of the IP data field should equal the UDP packet length.     */
   if (datalen != dgramlen) {
      printf("\t<*** Packet length corrupt ***>\n");
      nextpkt();                       /* Doesn't return                    */
   }
   datalen -= UDPHDRLEN;

   if (dataflag) {
      char dname[20];
      char sname[20];
      (void)strcpy(sname, svcname(sport, "udp", TRUE));
      (void)strcpy(dname, svcname(dport, "udp", TRUE));
      printf("%s.%s -> %s.%s over UDP\n", sip, sname, dip, dname);
      return pkt;                      /* Header is read; nothing to skip   */
   }

   if (terseflag)
      printf(
	 " UDP:\tport %d -> %d hdr=%u data=%u\n",
	 sport, dport, UDPHDRLEN, datalen
      );
   else {
      printf("UDP Header\n");
      printf(
	 "\tSource Port:\t\t\t%d (%s)\n",
	 sport, svcname(sport, "udp", FALSE)
      );
      printf(
	 "\tDestination Port:\t\t%d (%s)\n",
	 dport, svcname(dport, "udp", FALSE)
      );
      printf(
	 "\tDatagram Length:\t\t%u bytes (Header=%u, Data=%u)\n",
	 dgramlen, UDPHDRLEN, datalen
      );
      printf("\tChecksum:\t\t\t0x%04X\n", cksum);
   }

   return pkt;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Skip over un-interesting bytes.                                          */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *skip (
   char *pkt,
   uint2 nbytes
) {

   for ( ; nbytes > 0; nbytes--) (void)getbyte(&pkt);
   return pkt;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Return the WKS name for the given port.                                  */
/*                                                                          */
/****==========------------------------------------------------==========****/

static char *svcname (
   uint2 port,
   char *proto,
   boolean want_number
) {

   char *name;
   static char number[6];
   struct servent *service;            /* Doesn't need to be static         */


   /* The crappy manpage doesn't say the port must be in net byte order.    */
   if (service = getservbyport((int)htons(port), proto))
      name = service->s_name;
   elif (! want_number)
      name = unknown;
   else {
      sprintf(number, "%u", port);
      name = number;
   }

   return name;

}


/****==========------------------------------------------------==========****/
/*                                                                          */
/* Give a summary of usage.                                                 */
/*                                                                          */
/****==========------------------------------------------------==========****/

static void usage (
) {

#if !defined(MAY_NOT_MODIFY)
   printf("\nCopyright (c) 1996 I.T. NetworX Ltd.  All rights reserved.\n");
   printf("mailto:mike@NetworX.ie\n\n");
#endif
   printf("tcpshow -- decode a tcpdump(1) savefile, giving a verbose\n");
   printf("           display of the headers and an ASCII display of\n");
   printf("           ICMP, UDP and TCP data.\n\n");
   printf("Version %3.1f\n\n", VERSION);
   printf("Usage: tcpshow [ options ... ] [ expr ]\n");
   printf("\nwhere options are as follows\n");
   printf("\t-b\t\tbreak long lines so they don't wrap\n");
   printf("\t-sb\t\tshow breaks (show where we broke a line)\n");
   printf("\t-w width\tset pagewidth to \"width\" columns (used by -b)\n");
   printf("\t-nolink\t\tdon't decode link header (Ethernet header)\n");
   printf("\t-noip\t\tdon't decode IP header\n");
   printf("\t-nodata\t\tdon't show data (show headers only)\n");
   printf("\t-data\t\tdisplay data only; minimal header decode\n");
   printf("\t-track\t\ttrack sequence numbers (show next-expected ACK)\n");
   printf("\t-terse\t\tshow header decode in compact format\n");
   printf("\t-cooked\t\tdon't run tcpdump to pre-process the input\n");
   printf("\t-pp\t\tpoint-to-point link (no Ethernet header available)\n");
   printf("\t-s\t\tdisplay hex dump of spurious data at packet-end\n");
   printf("\t-h\t\tdisplay this help summary\n\n");
   printf("expr is a tcpdump(1) expression, and is only valid when ");
   printf("the -cooked\noption is not used.\n\n");
   printf("Input is from stdin, ");
   printf("which must be a raw tcpdump(1) data file (savefile),\n");
   printf("unless the -cooked option is used, in which case stdin ");
   printf("must be in the\nformat produced by tcpdump -lenx.\n\n");
   printf("Output is to stdout\n\n");
   printf("tcpdump(1) must be on your PATH unless -cooked is used.\n\n");

   exit(0);

}
