# Authority: dag

Summary: Advanced TFTP program.
Name: atftp
Version: 0.6.2
Release: 1
License: GPL
Group: Applications/Internet
URL: ftp://ftp.mamalinux.com/pub/atftp/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.mamalinux.com/pub/atftp/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libtermcap-devel
Requires: binutils, gawk, readline
Conflicts: tftp-server

%description
atftp is an advanced client/server implementation of the TFTP
protocol that implements RFCs 1350, 2090, 2347, 2348, and 2349.
The server is multi-threaded and the client presents a friendly
interface using libreadline. The current server implementation
lacks IPv6 support.

%prep
%setup

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
	--enable-libwrap
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0755 %{buildroot}/tftpboot/ \
			%{buildroot}%{_sysconfdir}/xinetd.d/
%{__install} -m0644 tftp.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/tftp

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS FAQ LICENSE README* TODO docs/
%doc %{_mandir}/man?/*
%dir /tftpboot/
%{_sysconfdir}/xinetd.d/*
%{_bindir}/atftp
%{_sbindir}/atftpd
%{_sbindir}/in.tftpd

%changelog
* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Conflicts with tftp-server package.
- Added xinetd script.

* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Initial package. (using DAR)
