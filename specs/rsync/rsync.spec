# $Id$
# Authority: dag
# Upstream: Martin Pool <mbp$sourcefrog,net>

# Rationale: rsync 2.6.2 uses less resources and has lots of improvements

%define real_version 2.6.3pre1

Summary: Program for synchronizing files over a network
Name: rsync
Version: 2.6.3
Release: 0.pre1
License: GPL
Group: Applications/Internet
URL: http://rsync.samba.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://rsync.samba.org/ftp/rsync/preview/rsync-%{real_version}.tar.gz
#Source: http://rsync.samba.org/ftp/rsync/rsync-%{version}.tar.gz
Patch1: rsync-2.6.2-lastdir-corruption.patch
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
%setup -n %{name}-%{real_version}
#%patch1 -p1 -b .lastdir-corruption

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
%{__install} -D -m0644 rsync.xinet %{buildroot}%{_sysconfdir}/xinetd.d/rsync


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README tech_report.tex TODO *.txt
%doc %{_mandir}/man1/rsync.1*
%doc %{_mandir}/man5/rsyncd.conf.5*
%config(noreplace) %{_sysconfdir}/xinetd.d/rsync
%{_bindir}/rsync


%changelog
* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 2.6.3-0.pre1
- Updated to release 2.6.3pre1.

* Sun Jun 13 2004 Dag Wieers <dag@wieers.com> - 2.6.2-1
- Updated to release 2.6.2.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 2.5.6-0
- Initial package. (using DAR)
