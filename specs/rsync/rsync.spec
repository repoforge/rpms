# $Id$

# Authority: dag

# Upstream: Martin Pool <mbp@sourcefrog.net>
# Tag: test

Summary: Program for synchronizing files over a network
Name: rsync
Version: 2.5.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://rsync.samba.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://rsync.samba.org/ftp/rsync/rsync-%{version}.tar.gz
Patch0: rsync-2.5.4-maxdel.patch
Patch1: rsync-2.4.6-segv.patch
Patch2: rsync-2.5.6-moresignage.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Rsync uses a reliable algorithm to bring remote and host files into
sync very quickly. Rsync is fast because it just sends the differences
in the files over the network instead of sending the complete
files. Rsync is often used as a very powerful mirroring process or
just as a more capable replacement for the rcp command. A technical
report which describes the rsync algorithm is included in this
package.

%prep
%setup
#%patch0 -p1 -b .maxdel
#%patch1 -p1 -b .segv
#%patch2 -b .moresignage

%{__cat} <<EOF >rsync.xinet
# default: off
# description: The rsync server is a good addition to an ftp server, as it \
#	allows crc checksumming etc.
service rsync
{
	disable	= yes
	socket_type     = stream
	wait            = no
	user            = root
	server          = %{_bindir}/rsync
	server_args     = --daemon
	log_on_failure  += USERID
}
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/xinetd.d/
%{__install} -m0644 rsync.xinet %{buildroot}%{_sysconfdir}/xinetd.d/rsync

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README tech_report.tex TODO *.txt
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/xinetd.d/rsync
%{_bindir}/rsync

%changelog
* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 2.5.6-0
- Initial package. (using DAR)
