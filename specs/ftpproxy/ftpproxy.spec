# $Id$
# Authority: dag

Summary: FTP proxy server
Name: ftpproxy
Version: 1.2.3
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://www.ftpproxy.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ftpproxy.org/download/ftpproxy-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ctags

%description
FTP proxy server.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|/usr/local/sbin|\$(sbindir)|g;
		s|/usr/local/man|\$(mandir)|g;
	' Makefile

%{__cat} <<EOF >ftpproxy.xinet
# default: off
# description: ftpproxy is an FTP proxy server.

service ftpproxy
{
	disable         = yes
	socket_type     = stream
	protocol        = tcp
	port            = 2121
	type		= UNLISTED
	wait            = no
	user            = ftp
	server          = %{_sbindir}/ftp.proxy
        server_args     = -b -B
}
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Create directories. (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man1/
%makeinstall

%{__install} -D -m0644 ftpproxy.xinet %{buildroot}%{_sysconfdir}/xinetd.d/ftpproxy

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY LICENSE doc/*.txt samples/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/xinetd.d/*
%{_sbindir}/*

%changelog
* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 1.2.3-1
- Updated to release 1.2.3.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 1.2.2-0
- Initial package. (using DAR)
