# $Id$
# Authority: dag
# Upstream: Jean-Pierre Lefebvre <helix@step.polymtl.ca>

Summary: Advanced Trivial File Transfer Protocol (TFTP) client
Name: atftp
Version: 0.7
Release: 3
License: GPL
Group: Applications/Internet
URL: ftp://ftp.mamalinux.com/pub/atftp/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.mamalinux.com/pub/atftp/atftp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtermcap-devel, pcre-devel
Requires: binutils, gawk, readline
Provides: tftp

%description
atftp is an advanced client implementation of the TFTP
protocol that implements RFCs 1350, 2090, 2347, 2348, and 2349.
The server is multi-threaded and the client presents a friendly
interface using libreadline. The current server implementation
lacks IPv6 support.

%package server
Summary: Advanced Trivial File Transfer Protocol (TFTP) server
Group: System Environment/Daemons

#Conflicts: tftp-server
Provides: tftp-server

%description server
atftpd is an advanced server implementation of the TFTP
protocol that implements RFCs 1350, 2090, 2347, 2348, and 2349.
The server is multi-threaded and the client presents a friendly
interface using libreadline. The current server implementation
lacks IPv6 support.

%prep
%setup

### FIXME: Change location of pcre.h to pcre/pcre.h (Please fix upstream)
%{__perl} -pi.orig -e 's|\bpcre.h\b|pcre/pcre.h|' configure tftpd.c tftpd_pcre.h

%{__cat} <<EOF >tftp.xinetd
# default: off
# description: The tftp server serves files using the trivial file transfer protocol. The tftp protocol is often used to boot diskless workstations, download configuration files to network-aware printers, and to start the installation process for some operating systems.
service tftp
{
	disable	= yes
	socket_type		= dgram
	protocol		= udp
	wait			= yes
	user			= root
	server			= %{_sbindir}/in.tftpd
	server_args		= /tftpboot
	per_source		= 11
	cps			= 100 2
	flags			= IPv4
}
EOF

%build
%configure \
	--disable-dependency-tracking \
	--enable-libreadline \
	--enable-libwrap \
	--enable-libpcre \
	--enable-mtftp
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d %{buildroot}/tftpboot/
%{__install} -D -m0644 tftp.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/tftp

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changelog FAQ INSTALL LICENSE README* TODO
%doc %{_mandir}/man?/atftp.*
%{_sysconfdir}/xinetd.d/*
%{_bindir}/atftp

%files server
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/atftpd.*
%doc docs/*
%dir /tftpboot/
%{_sbindir}/atftpd
%{_sbindir}/in.tftpd

%changelog
* Sun Mar 28 2004 Dag Wieers <dag@wieers.com> - 0.7.0-3
- Removed Conflicts-tag.

* Thu Mar 25 2004 Dag Wieers <dag@wieers.com> - 0.7.0-2
- Provide tftp and tftp-server.

* Sat Mar 20 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to new release 0.7.0.

* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Conflicts with tftp-server package.
- Added xinetd script.

* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Initial package. (using DAR)
