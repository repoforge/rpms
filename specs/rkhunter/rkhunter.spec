# $Id$
# Authority: dag

Summary: Host-based tool to scan for rootkits, backdoors and local exploits
Name: rkhunter
Version: 1.2.9
Release: 2
License: GPL
Group: Applications/System
URL: http://www.rootkit.nl/

Source: http://dl.sf.net/rkhunter/rkhunter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: /bin/sh, coreutils, binutils, modutils, findutils, grep, mktemp
Requires: e2fsprogs, procps, lsof, prelink, iproute, net-tools, wget
Requires: perl, perl(strict), perl(IO::Socket), mailx

%description
Rootkit Hunter scans files and systems for known and unknown rootkits,
backdoors, and sniffers.  The package contains one shell script, a few
text-based databases, and optional Perl modules.  It should run on almost
every Unix clone.  This tool scans for rootkits, backdoors and local
exploits by running tests like: 

	MD5 hash compare,
	Look for default files used by rootkits,
	Wrong file permissions for binaries,
	Look for suspected strings in LKM and KLD modules,
	Look for hidden files,
	Optional scan within plaintext and binary files,
	Software version checks and
	Application tests

%prep
%setup -n %{name}-%{version}/files

%{__cat} <<EOF >rkhunter.conf.new
# This is the configuration file of Rootkit Hunter. Please change
# it to your needs.
#
# All lines beginning with a hash (#) or empty lines, will be ignored.
#
INSTALLDIR=%{_prefix}

# Links to files. Don't change if you don't need to.
LATESTVERSION=/rkhunter_latest.dat
UPDATEFILEINFO=/rkhunter_fileinfo.dat

# Send a warning message to the admin when one or more warnings
# are available (rootkit and MD5 check). Note: uses default `mail`
# commmand to send the warning message.
MAIL-ON-WARNING=root@localhost

# Use a custom temporary directory (you can override it with the
# --tmpdir parameter)
# Note: don't use /tmp as your temporary directory, because some
# important files will be written to this directory. Be sure
# you have setup your permissions very tight.
TMPDIR=%{_localstatedir}/rkhunter/tmp

# Use a custom database directory (you can override it with the
# --dbdir parameter)
DBDIR=%{_localstatedir}/rkhunter/db

# Whitelist files (and their MD5 hash)
# Usage: MD5WHITELIST=<binary>:<MD5 hash>
#MD5WHITELIST=/bin/ps:9bd8bf260adc81d3a43a086fce6b430a
#MD5WHITELIST=/bin/ps:404583a6b166c2f7ac1287445a9de6b3

# Allow direct root login via SSH
# Don't use this option if you don't know what the warning about
# this option means!!
#ALLOW_SSH_ROOT_USER=0

# Allow hidden directory
# One directory per line (use multiple ALLOWHIDDENDIR lines)
#
#ALLOWHIDDENDIR=/etc/.java
#ALLOWHIDDENDIR=/dev/.udev
#ALLOWHIDDENDIR=/dev/.udevdb
#ALLOWHIDDENDIR=/dev/.udev.tdb
#ALLOWHIDDENDIR=/dev/.static
#ALLOWHIDDENDIR=/dev/.initramfs
#ALLOWHIDDENDIR=/dev/.SRC-unix

# Allow hidden file
# One file per line (use multiple ALLOWHIDDENFILE lines)
# 
#ALLOWHIDDENFILE=/etc/.java
#ALLOWHIDDENFILE=/usr/share/man/man1/..1.gz
#ALLOWHIDDENFILE=/etc/.pwd.lock
#ALLOWHIDDENFILE=/etc/.init.state

# Allow process to use deleted files
# One process per line (use multiple ALLOWPROCDELFILE lines)
#
#ALLOWPROCDELFILE=/sbin/cardmgr
#ALLOWPROCDELFILE=/usr/sbin/gpm
#ALLOWPROCDELFILE=/usr/libexec/gconfd-2
#ALLOWPROCDELFILE=/usr/sbin/mysqld

# Allow process to listen on any interface
# One process per line (use multiple ALLOWPROCLISTEN lines)
#
#ALLOWPROCLISTEN=/sbin/dhclient
#ALLOWPROCLISTEN=/usr/bin/dhcpcd
#ALLOWPROCLISTEN=/usr/sbin/pppoe
#ALLOWPROCLISTEN=/usr/sbin/tcpdump
#ALLOWPROCLISTEN=/usr/sbin/snort-plain
#ALLOWPROCLISTEN=/usr/local/bin/wpa_supplicant

# The End
EOF

### Check what has been changed
diff -u rkhunter.conf rkhunter.conf.new || :

%{__perl} -pi.orig -e 's| /usr/man| %{_mandir}|g' rkhunter

%{__cat} <<EOF >rkhunter.logrotate
%{_localstatedir}/log/rkhunter.log {
	weekly
	notifempty
	create 640 root root
}
EOF

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0750 rkhunter %{buildroot}%{_bindir}/rkhunter

%{__install} -Dp -m0644 rkhunter.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/rkhunter
%{__install} -Dp -m0640 rkhunter.conf.new %{buildroot}%{_sysconfdir}/rkhunter.conf
#%{__install} -Dp -m0640 rkhunter.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/rkhunter
#%{__install} -Dp -m0750 01-rkhunter %{buildroot}%{_sysconfdir}/cron.daily/01-rkhunter

%{__install} -d -m0750 %{buildroot}%{_localstatedir}/rkhunter/db/
%{__install} -p -m640 *.dat %{buildroot}%{_localstatedir}/rkhunter/db/

%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__install} -p -m0644 -p development/*.8 %{buildroot}%{_mandir}/man8/

%{__install} -d -m0755 %{buildroot}%{_prefix}/lib/rkhunter/scripts/
%{__install} -p -m0750 *.pl check_*.sh %{buildroot}%{_prefix}/lib/rkhunter/scripts/

%{__install} -d -m0750 %{buildroot}%{_localstatedir}/rkhunter/tmp/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/rkhunter.log
%{__chmod} 0640 %{buildroot}%{_localstatedir}/log/rkhunter.log

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README WISHLIST
%doc %{_mandir}/man8/*.8*
%config(noreplace) %{_sysconfdir}/rkhunter.conf
#%config(noreplace) %{_sysconfdir}/sysconfig/rkhunter
#%config %{_sysconfdir}/cron.daily/01-rkhunter
%config %{_sysconfdir}/logrotate.d/rkhunter
%{_bindir}/rkhunter
%{_prefix}/lib/rkhunter/
%{_localstatedir}/rkhunter/
%ghost %{_localstatedir}/log/rkhunter.log

%changelog
* Thu May 17 2007 Dag Wieers <dag@wieers.com> - 1.2.9-2
- Fixed the INSTALLDIR location in rkhunter.conf. (Phil Schaffner)

* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 1.2.9-1
- Initial package. (using DAR)
