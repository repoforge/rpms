# $Id: rsync.spec 2540 2004-11-23 18:39:10Z dag $
# Authority: dag
# Upstream: Martin Pool <mbp$sourcefrog,net>

# Tag: test

# Rationale: rsync 2.6.3 uses less resources and has lots of improvements

Summary: Program for synchronizing files over a network
Name: rsync
Version: 2.6.4
Release: 0.cvs20050114
License: GPL
Group: Applications/Internet
URL: http://rsync.samba.org/

#Source: http://rsync.samba.org/ftp/rsync/preview/rsync-%{real_version}.tar.gz
Source: http://rsync.samba.org/ftp/rsync/rsync-%{version}-cvs20050114.tar.bz2
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
%setup -n %{name}-%{version}-cvs20050114

patch -p0 < patches/delay-renames.diff

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
* Fri Jan 14 2005 Dag Wieers <dag@wieers.com> - 2.6.4-0.cvs20050114
- Updated to release 2.6.4-cvs20050114.

* Tue Jan 11 2005 Dag Wieers <dag@wieers.com> - 2.6.4-0.cvs20050111
- Added delay-renames patch from CVS.
- Updated to release 2.6.4-cvs20050111.

* Tue Nov 23 2004 Dag Wieers <dag@wieers.com> - 2.6.3-1
- Updated to release 2.6.3.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 2.6.3-0.pre2
- Updated to release 2.6.3pre2.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 2.6.3-0.pre1
- Updated to release 2.6.3pre1.

* Sun Jun 13 2004 Dag Wieers <dag@wieers.com> - 2.6.2-1
- Updated to release 2.6.2.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 2.5.6-0
- Initial package. (using DAR)
