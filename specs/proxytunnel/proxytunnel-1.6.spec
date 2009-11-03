# $Id$
# Authority: dag
# Upstream: <proxytunnel-users$lists,sourceforge,net>

# Test: tag

Summary: Punching holes in HTTP(S) proxy's
Name: proxytunnel
%define real_version 1.6.0-rc1
Version: 1.6.0
Release: 0.rc1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://proxytunnel.sourceforge.net/

Source: http://dl.sf.net/proxytunnel/proxytunnel-%{version}-rc1.tgz
#Source: http://proxytunnel.sf.net/files/proxytunnel-%{version}.tgz
Patch: proxytunnel-1.6.0-rc1-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
ProxyTunnel is a program that connects stdin and stdout to a server somewhere
on the network, through a standard HTTPS proxy. We mostly use it to tunnel
SSH sessions through HTTP(S) proxies, allowing us to do many things that
wouldn't be possible without ProxyTunnel.

Proxytunnel can create tunnels using HTTP and HTTPS proxies, can work as a
back-end driver for an OpenSSH client, and create SSH connections through
HTTP(S) proxies and can work as a stand-alone application, listening on a
port for connections, and then tunneling these connections to a specified
destination.

If you want to make effective use of ProxyTunnel, the proxy server you are
going to be tunneling through must support HTTP CONNECT command and must
allow you to connect to destination machine and host, with or without HTTP
proxy authentication

%prep
%setup -n %{name}-%{real_version}
%patch -p0

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}" CFLAGS="-I/usr/kerberos/include"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS LICENSE.txt README
%doc %{_mandir}/man1/proxytunnel.1*
%{_bindir}/proxytunnel

%changelog
* Tue Feb 07 2006 Dag Wieers <dag@wieers.com> - 1.6.0-0.rc1
- Updated to release 1.6.0-rc1.

* Fri Dec 23 2005 Dag Wieers <dag@wieers.com> - 1.5.0-1
- Initial package. (using DAR)
