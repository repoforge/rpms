#!/bin/bash
# Convert a live CD iso so that it can be booted over the network
# using PXELINUX.
# Copyright 2008 Red Hat, Inc.
# Written by Richard W.M. Jones <rjones@redhat.com>
# Based on a script by Jeremy Katz <katzj@redhat.com>
# Based on original work by Chris Lalancette <clalance@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

export PATH=/sbin:/usr/sbin:$PATH

usage() {
    echo "Usage: livecd-iso-to-pxeboot <isopath>"
    exit 1
}

cleanup() {
    [ -d "$CDMNT" ] && umount $CDMNT && rmdir $CDMNT
}

exitclean() {
    echo "Cleaning up to exit..."
    cleanup
    exit 1
}

if [ $(id -u) != 0 ]; then
    echo "You need to be root to run this script."
    exit 1
fi

# Check pxelinux.0 exists.
if [ ! -f /usr/lib/syslinux/pxelinux.0 ]; then
    echo "Warning: /usr/lib/syslinux/pxelinux.0 not found."
    echo "Make sure syslinux or pxelinux is installed on this system."
fi

while [ $# -gt 1 ]; do
    case "$1" in
	*) usage ;;
    esac
    shift
done

ISO="$1"

if [ -z "$ISO" -o ! -e "$ISO" ]; then
    usage
fi

if [ -d tftpboot ]; then
    echo "Subdirectory tftpboot exists already.  I won't overwrite it."
    echo "Delete the subdirectory before running."
    exit 1
fi

mkdir tftpboot

# Mount the ISO.
# FIXME: would be better if we had better mountpoints
CDMNT=$(mktemp -d /media/cdtmp.XXXXXX)
mount -o loop "$ISO" $CDMNT || exitclean

trap exitclean SIGINT SIGTERM

# Does it look like an ISO?
if [ ! -d $CDMNT/isolinux -o ! -f $CDMNT/isolinux/initrd0.img ]; then
    echo "The ISO image doesn't look like a LiveCD ISO image to me."
    exitclean
fi

# Create a cpio archive of just the ISO and append it to the
# initrd image.  The Linux kernel will do the right thing,
# aggregating both cpio archives (initrd + ISO) into a single
# filesystem.
ISOBASENAME=`basename "$ISO"`
ISODIRNAME=`dirname "$ISO"`
( cd "$ISODIRNAME" && echo "$ISOBASENAME" | cpio -H newc --quiet -o ) |
  gzip -9 |
  cat $CDMNT/isolinux/initrd0.img - > tftpboot/initrd0.img

# Kernel image.
cp $CDMNT/isolinux/vmlinuz0 tftpboot/vmlinuz0

# pxelinux bootloader.
if [ -f /usr/lib/syslinux/pxelinux.0 ]; then
    cp /usr/lib/syslinux/pxelinux.0 tftpboot
else
    echo "Warning: You need to add pxelinux.0 to tftpboot/ subdirectory"
fi

# pxelinux configuration.
mkdir tftpboot/pxelinux.cfg
cat > tftpboot/pxelinux.cfg/default <<EOF
DEFAULT pxeboot
TIMEOUT 20
PROMPT 0
LABEL pxeboot
	KERNEL vmlinuz0
	APPEND initrd=initrd0.img root=/$ISOBASENAME rootfstype=iso9660 rootflags=loop
ONERROR LOCALBOOT 0
EOF

# All done, clean up.
umount $CDMNT
rmdir $CDMNT

echo "Your pxeboot image is complete."
echo
echo "Copy tftpboot/ subdirectory to /tftpboot or a subdirectory of /tftpboot."
echo "Set up your DHCP, TFTP and PXE server to serve /tftpboot/.../pxeboot.0"
echo
echo "Note: The initrd image contains the whole CD ISO and is consequently"
echo "very large.  You will notice when pxebooting that initrd can take a"
echo "long time to download.  This is normal behaviour."

exit 0
