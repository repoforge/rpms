# $Id$

# Authority: dag

Summary: The client for the Trivial File Transfer Protocol (TFTP).
Name: tftp
Version: 0.34
Release: 0
License: BSD
Group: Applications/Internet
URL: http://www.kernel.org/pub/software/network/tftp/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.kernel.org/pub/software/network/tftp/%{name}-hpa-%{version}.tar.bz2
Patch: tftp-0.28-malta.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: tcp_wrappers

%description
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations.  The tftp package provides the user
interface for TFTP, which allows users to transfer files to and from a
remote machine.  This program and TFTP provide very little security,
and should not be enabled unless it is expressly needed.

%package server
Group: System Environment/Daemons
Summary: The server for the Trivial File Transfer Protocol (TFTP).
Requires: xinetd

%description server
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations.  The tftp-server package provides the
server for TFTP, which allows users to transfer files to and from a
remote machine. TFTP provides very little security, and should not be
enabled unless it is expressly needed.  The TFTP server is run from
/etc/xinetd.d/tftp, and is disabled by default on Red Hat Linux systems.

%prep
%setup -n tftp-hpa-%{version} 
%patch -p1 -b .malta

%{__cat} <<EOF >tftp.xinetd
# default: off
# description: The tftp server serves files using the trivial file transfer \
#	protocol.  The tftp protocol is often used to boot diskless \
#	workstations, download configuration files to network-aware printers, \
#	and to start the installation process for some operating systems.
service tftp
{
	socket_type		= dgram
	protocol		= udp
	wait			= yes
	user			= root
	server			= %{_sbindir}/in.tftpd
	server_args		= -s /tftpboot
	disable			= yes
	per_source		= 11
	cps			= 100 2
	flags			= IPv4
}
EOF

%build

%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man{1,8} \
			%{buildroot}%{_sbindir} \
			%{buildroot}%{_sysconfdir}/xinetd.d/
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	SBINDIR="%{buildroot}%{_sbindir}" \
	MANDIR="%{buildroot}%{_mandir}" 
%{__install} -m644 tftp.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/tftp

%post server
/sbin/service xinetd reload &>/dev/null || :

%postun server
if [ $1 -eq 0 ]; then
    /sbin/service xinetd reload &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_mandir}/man1/*

%files server
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/xinetd.d/*
%{_sbindir}/*
%{_mandir}/man8/*

%changelog
* Mon Jul 07 2003 Dag Wieers <dag@wieers.com> - 0.34-0
- Updated to release 0.34.

* Mon Jul 07 2003 Dag Wieers <dag@wieers.com> - 0.32-0
- Initial package. (using DAR)
