/*
rpcmgr, a DVD RPC (Region Playback Control) tool.
Copyright (C) 2000  Dag Lem <rpcmgr@nimrod.no>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
*/

/*
This program uses SCSI commands to report and modify the RPC2 settings
of DVD drives.

USE THIS PROGRAM AT YOUR OWN RISK! I have tested it with an LG
DRN8080B and a Pioneer DVD-303 and believe it to be safe, but I could
be wrong. This program might cause your particular DVD drive to be
permanently region locked, it might cause your DVD drive to blow up,
it might set your house on fire, whatever; I take zero responsibility.

What is RPC? RPC stands for Region Playback Control. RPC divides the
world into eight regions and potentially denies you the right to play
back DVD discs from all but one of these regions. RPC comes in two
flavors; software control (RPC Phase I / RPC1) and hardware control
(RPC Phase II / RPC2). RPC1 is enforced by the DVD player software,
while RPC2 is enforced by both the software and by the DVD drive
itself.

With RPC2 drives you are allowed to change the region five times,
after which the drive region is permanently set. The drive vendor may
reset the user region counter thus unlocking the permanent state,
however this is also normally limited to five times.

There are several methods of bypassing RPC. RPC1 can by bypassed by
patching the DVD playback software or by intercepting the
communication between the software and the DVD drive, always telling
the software that the disc in the drive is coded with one specific
region. It has been reported that RPC2 in some cases can be bypassed
by interception as well, however as one might guess this does not
always work since RPC2 is really a hardware enforcement of RPC. To
bypass RPC2, the most common measure is to upgrade the drive with
microcode (or firmware) that does not enforce RPC2. In some cases the
existing microcode allows the user to disable RPC2 compliance, in
these cases a microcode upgrade is not necessary. Finally, it can be
noted that the region mask in RPC is a bit mask with one bit for each
region. On some drives it is possible to specify that playback is
allowed for all regions while still complying to RPC2. In this case it
is important to use DVD playback software that does not enforce a
setting of only one region. OMS for Linux works fine, whereas
e.g. WinDVD for Windows will set a new region, thus decrementing the
user region counter and possibly permanently setting the region.

This program was originally developed for LG DRD8080B and DRN8080B
drives. The options --disable, --reset-user, and --reset-vendor invoke
special commands for these drives. The nifty thing about these
commands is that they allow you to set new regions at your hearts
desire, or even temporarily disable RPC2 compliance. The upshot of
this is that you may now play any DVD from your DVD collection on your
laptop, just as you do on your region free home DVD player.

As of version 1.1 of this program, the COMPAQ DRD8080B and DRN8080B
are recognized as LG drives, thanks to Arzeno Fabrice. Also, options
--disable and --enable should work for HITACHI GD-3000, HITACHI
GD-5000, and COMPAQ GD-5000 drives. A big thanks to XVI for reverse
engineering and Hunter for Windows source on behalf of Unix/Linux
users owning one of these drives. Hunter has also provided MMC-2
documentation - thank you. One note of caution for the GD-x000 drives:
Disable RPC2 and leave it at that, rumour has it that only a limited
amount of RPC2 status changes (32?) are allowed for these drives, and
you wouldn't want to lock your drive in RPC2 now, would you?

For ATAPI drives like the LG drives mentioned above, you need a SCSI
emulation layer in the kernel. In Linux, the kernel must be configured
with "SCSI emulation support"; see "IDE, ATA and ATAPI Block devices"
in 'make xconfig' (CONFIG_BLK_DEV_IDESCSI=y). It goes without saying
that you also need support for SCSI, generic SCSI, and SCSI CD-ROM
devices. Finally, you need to put a line of the form append="hdx=scsi"
in /etc/lilo.conf (e.g. append="hdc=scsi") and run lilo.

For interested readers, the LG SCSI commands in this program were
determined by running the LG utility RpcMan.exe under Wine. RpcMan
uses the ASPI SCSI layer in Windows, which also acts as a SCSI
emulation layer for ATAPI devices. By monitoring the data passing
through the ASPI layer, it is fairly simple to determine the SCSI
commands used in this program. This technique has earlier been
suggested by Henning Meier-Geinitz <hmg@gmx.de> in the SANE project as
a means of determining SCSI commands for undocumented scanners.
Running 'wine --debugmsg +aspi RpcMan.exe 2> debug.txt' almost does
the trick, the only thing missing is a printout of the SCSI data
buffer in addition to the SCSI command buffer; this needs to be added
to the file winaspi32.c in Wine first. If you have a DRN8080B you also
need to binary patch RpcMan.exe, modifying the string "DVD-ROM
DRD8080B" to "DVD-ROM DRN8080B". This last piece of information might,
by the way, be of interest to Windows users with LG DRN8080B
drives. Valid passwords for RPC2 init are R2D2, R8021314, R8124618,
and RPB08143.

Finally, I have a few interesting suggestions for the adventurous. I
have not tried these things myself, and if your DVD drive should
somehow be destroyed, don't tell me I didn't warn you. Anyway, I would
like to hear from you if you do try these things.

- Try the --disable, --reset-user, and --reset-vendor commands on
other drive models, especially LG drives. You will need to disable the
drive model check in this program to do this.

- For LG DRx8080B owners: If you take a closer look at the --disable,
--reset-user, and --reset-vendor commands you will notice that the
only difference between these functions lies in the second byte and in
the second last byte in the command/data buffer.
         second  second last
reset:   0x00    0x81
init:    0x10    0x80
disable: 0x00    0x02

What happens if you try e.g. the following?:
reset:   0x00    0x80/0x82
init:    0x10    0x81/0x82
disable: 0x00 0x00/0x01 (tested, 0x00 is valid but does nothing)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <unistd.h>
#include <scsi/scsi.h>
#include <scsi/sg.h>


#define PROG "rpcmgr"

/* SCSI Multimedia Commands - 2 (MMC-2) */
#ifndef REPORT_KEY
#define REPORT_KEY 0xa4
#define SEND_KEY 0xa3
#define READ_DVD_STRUCTURE 0xad
#endif

#define HITACHI_RPC2 0xe7

/* SCSI buffers */
#define SG_SIZE sizeof(struct sg_header)
char buf_msg[SG_SIZE + 200];
char buf_reply[SG_SIZE + 200];
struct sg_header* sg_msg = (struct sg_header*)buf_msg;
struct sg_header* sg_reply = (struct sg_header*)buf_reply;
unsigned char* msg = buf_msg + SG_SIZE;
unsigned char* reply = buf_reply + SG_SIZE;

typedef enum { RPC2_ENABLE, RPC2_DISABLE, RPC2_RESET_USER, RPC2_RESET_VENDOR } rpc2_command_t;
typedef void (*rpc2_function_t)(int fd, rpc2_command_t command);

void rpc2_hitachi(int fd, rpc2_command_t command);
void rpc2_lg(int fd, rpc2_command_t command);

/* List of drives that respond to special RPC2 commands */
struct drive_model {
  char* vendor;
  char* product;
  rpc2_function_t rpc2_function;
}
rpcmgr_drives[] = {
  { "COMPAQ  ", "DVD-ROM DRD8080B", rpc2_lg },
  { "COMPAQ  ", "DVD-ROM DRN8080B", rpc2_lg },
  { "COMPAQ  ", "DVD-ROM GD-5000 ", rpc2_hitachi },
  { "HITACHI ", "DVD-ROM GD-3000 ", rpc2_hitachi },
  { "HITACHI ", "DVD-ROM GD-5000 ", rpc2_hitachi },
  { "LG      ", "DVD-ROM DRD8080B", rpc2_lg },
  { "LG      ", "DVD-ROM DRN8080B", rpc2_lg }
};


/* Display program usage and exit */
void usage(FILE* fd)
{
  fprintf(fd, "Usage: %s option [sg device]\n"
	  "Options:\n"
	  "  -d, --disable       disable RPC2\n"
	  "                      warning: limited number of changes for GD-x000!\n"
	  "                               only lasts until next boot for DRx-8080B!\n"
          "                      COMPAQ  DRD8080B, DRN8080B, GD-5000\n"
          "                      HITACHI GD-3000,  GD-5000\n"
	  "                      LG      DRD8080B, DRN8080B\n"
	  "  -e, --enable        enable RPC2\n"
	  "                      warning: limited number of changes for GD-x000!\n"
          "                      COMPAQ  DRD8080B, DRN8080B, GD-5000\n"
          "                      HITACHI GD-3000,  GD-5000\n"
	  "  -h, --help          display this help and exit\n"
	  "  -i, --dvdinfo       display DVD encryption and region info\n"
	  "  -r, --region=R|all  set RPC2 region R or attempt to set all regions at once\n"
	  "                      warning: decreases RPC2 user counter!\n"
	  "  -s, --status        display RPC status\n"
	  "  -u, --reset-user    reset RPC2 user counter\n"
	  "                      warning: decreases RPC2 vendor counter!\n"
          "                      COMPAQ  DRD8080B, DRN8080B\n"
	  "                      LG      DRD8080B, DRN8080B\n"
	  "  -v, --reset-vendor  reset RPC2 vendor counter\n"
          "                      COMPAQ  DRD8080B, DRN8080B\n"
	  "                      LG      DRD8080B, DRN8080B\n"
	  "  -V, --version       print version information and exit\n", PROG);
  exit(1);
}

/* Output version information and exit */
void version()
{
  fprintf(stdout, PROG " version 1.1\n"
	  "Copyright (C) 2000 Dag Lem.\n"
	  "This is free software; see the source for copying conditions.  There is NO\n"
	  "warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n");
  exit(0);
}

/* Create printable string of regions from region mask */
const char* region(char mask)
{
  static char text[20] = " not set";
  int bits = ~mask;

  if (bits) {
    int i;
    int end = 0;
    for (i = 0; i < 8; i++) {
      if (bits & 0x01) {
	end += sprintf(text + end, " %d", i + 1);
      }
      bits >>= 1;
    }
  }

  return text;
}

/* Send SCSI command to drive and retrieve reply */
void sgio(int fd, const unsigned char* cmd, int cmdlen, int replylen)
{
  int pack_len = SG_SIZE + cmdlen;
  int reply_len = SG_SIZE + replylen;

  memset(buf_msg, 0, pack_len);
  sg_msg->reply_len = reply_len;
  memcpy(msg, cmd, cmdlen);

  memset(buf_reply, 0, reply_len);

  if (write(fd, buf_msg, pack_len) != pack_len) {
    perror("sg write");
    exit(1);
  }

  if (read(fd, buf_reply, reply_len) != reply_len) {
    perror("sg read");
    exit(1);
  }
}

/* Drive model check */
void check_device(int fd)
{
  int replylen = 96;

  unsigned char cmd[] = { INQUIRY, 0x00, 0x00, 0x00, 0x00, 0x00 };
  cmd[4] = replylen;

  sgio(fd, cmd, sizeof(cmd), replylen);

  if (sg_reply->driver_status != 0x00) {
    fprintf(stderr, "Unable to read drive info\n");
    exit(1);
  }

  fprintf(stdout, "Vendor: %.8s Model: %.16s Rev: %.4s\n",
	  reply + 8, reply + 16, reply + 32);

  if (reply[0] != TYPE_ROM) {
    fprintf(stderr, "Not a DVD-ROM device\n");
    exit(1);
  }
}

/* DVD encryption and region info */
void dvdinfo(int fd)
{
  unsigned char cmd[] = { READ_DVD_STRUCTURE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x08, 0x00, 0x00 };

  sgio(fd, cmd, sizeof(cmd), 8);

  if (sg_reply->driver_status != 0x00) {
    fprintf(stderr, "Unable to read DVD structure, insert disc and wait for drive to finish\n");
    exit(1);
  }

  fprintf(stdout, "CSS: %s, region mask:%s\n", reply[4] ? "enabled" : "disabled", region(reply[5]));
}

/* RPC status */
void status(int fd)
{
  char* type_code[] = { "not set", "set", "last chance", "permanent" };

  unsigned char cmd[] = { REPORT_KEY, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08, 0x00 };

  sgio(fd, cmd, sizeof(cmd), 8);

  if (sg_reply->driver_status != 0x00 || reply[6] == 0x00) {
    fprintf(stdout, "RPC1\n");
  }
  else {
    fprintf(stdout, "RPC2: region mask:%s, user: %d, vendor: %d, status: %s\n", region(reply[5]), reply[4] & 0x07, (reply[4] >> 3) & 0x07, type_code[reply[4] >> 6]);
  }
}    

/* RPC2 set region */
void set_region(int fd, unsigned char rmask)
{
  unsigned char cmd[] = { SEND_KEY, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x06, 0x00,
		              0x00, 0x06, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00 };

  cmd[12 + 4] = rmask;

  sgio(fd, cmd, sizeof(cmd), 0);

  if (sg_reply->driver_status != 0x00) {
    fprintf(stderr, "Unable to set region, insert disc with requested region and wait for drive to finish\n");
    exit(1);
  }
}


/* Execute special RPC2 command */
void rpc2_execute(int fd, rpc2_command_t command)
{
  int i;
  for (i = 0; i < sizeof(rpcmgr_drives)/sizeof(struct drive_model); i++) {
    if (strncmp(reply + 8, rpcmgr_drives[i].vendor, 8) == 0
	&& strncmp(reply + 16, rpcmgr_drives[i].product, 16) == 0)
      {
	rpcmgr_drives[i].rpc2_function(fd, command);
	return;
      }
  }

  fprintf(stderr, "There are no known special RPC2 commands for this drive model\n");
  exit(1);
}


/* HITACHI RPC2 */
void rpc2_hitachi(int fd, rpc2_command_t command)
{
  unsigned char cmd[] = { HITACHI_RPC2, 'H', 'I', 'T', 'R', 'P', 'C', '2', 0x02, 0x00, 0x00, 0x00 };

  /* Can only execute RPC2_ENABLE and RPC2_DISABLE */
  switch (command) {
  case RPC2_ENABLE:
    cmd[9] = 0x02;
    break;
  case RPC2_DISABLE:
    cmd[9] = 0x01;
    break;
  default:
    fprintf(stderr, "HITACHI RPC2: invalid command\n");
    exit(1);
  }

  sgio(fd, cmd, sizeof(cmd), 0);

  if (sg_reply->driver_status != 0x00) {
    fprintf(stderr, "HITACHI RPC2: command failed\n");
    exit(1);
  }
}


/* LG RPC2 */
void rpc2_lg(int fd, rpc2_command_t command)
{
  int cmdlen = 12;
  unsigned char cmd[] = { MODE_SELECT_10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0c, 0x00, 0x00, 0x00,
			            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x21, 0x02, 0x00, 0x00 };

  /* Can execute everything except RPC2_ENABLE */
  switch (command) {
  case RPC2_DISABLE:
    cmd[1] = 0x00;
    cmd[12 + 10] = 0x02;
    break;
  case RPC2_RESET_USER:
    cmd[1] = 0x00;
    cmd[12 + 10] = 0x81;
    break;
  case RPC2_RESET_VENDOR:
    cmd[1] = 0x10;
    cmd[12 + 10] = 0x80;
    break;
  default:
    fprintf(stderr, "LG RPC2: invalid command\n");
    exit(1);
  }

  ioctl(fd, SG_NEXT_CMD_LEN, &cmdlen);
  sgio(fd, cmd, sizeof(cmd), 0);

  if (sg_reply->driver_status != 0x00) {
    fprintf(stderr, "LG RPC2: command failed\n");
    exit(1);
  }
}

	

/* Progam entry */
int main(int argc, char** argv)
{
  struct option longopts[] =
    {
      { "disable",      no_argument,       NULL, 'd' },
      { "enable",       no_argument,       NULL, 'e' },
      { "help",         no_argument,       NULL, 'h' },
      { "dvdinfo",      no_argument,       NULL, 'i' },
      { "region",       required_argument, NULL, 'r' },
      { "status",       no_argument,       NULL, 's' },
      { "reset-user",   no_argument,       NULL, 'u' },
      { "reset-vendor", no_argument,       NULL, 'v' },
      { "version",      no_argument,       NULL, 'V' },
      { NULL,           no_argument,       NULL, 0   }
    };

  int val;
  int flag = 0;
  char* region_str;
  unsigned char rmask;
  int fd;

  while ((val = getopt_long(argc, argv, "+dehir:suvV", longopts, NULL)) != -1)
  {
    if (flag) {
      usage(stderr);
    }

    switch (val) {
    case '?':
    case ':':
      usage(stderr);
    case 'h':
      usage(stdout);
    case 'V':
      version();
    }

    flag = val;
    region_str = optarg;
  }

  if (!flag || optind + 1 != argc) {
    usage(stderr);
  }

  fd = open(argv[optind], O_RDWR);
  if (fd == -1) {
    perror("sg open");
    exit(1);
  }

  check_device(fd);

  switch (flag) {
  case 'd':
    rpc2_execute(fd, RPC2_DISABLE);
    status(fd);
    break;
  case 'e':
    rpc2_execute(fd, RPC2_ENABLE);
    status(fd);
    break;
  case 'i':
    dvdinfo(fd);
    break;
  case 'r':
    if (strcmp(region_str, "all") == 0) {
      set_region(fd, 0x00);
    }
    else {
      rmask = atoi(region_str);
      if (rmask < 1 || rmask > 8) {
	fprintf(stderr, "Invalid region: %d\n", rmask);
	exit(1);
      }
      set_region(fd, ~(1 << (rmask - 1)));
    }
    status(fd);
    break;
  case 's':
    status(fd);
    break;
  case 'u':
    rpc2_execute(fd, RPC2_RESET_USER);
    status(fd);
    break;
  case 'v':
    rpc2_execute(fd, RPC2_RESET_VENDOR);
    status(fd);
    break;
  }

  close(fd);

  exit(0);
}
