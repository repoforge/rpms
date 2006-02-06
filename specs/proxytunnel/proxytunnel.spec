# $Id$
# Authority: dag
# Upstream: <proxytunnel-users$lists,sourceforge,net>

Summary: Punching holes in HTTP(S) proxy's
Name: proxytunnel
Version: 1.5.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://proxytunnel.sourceforge.net/

Source: http://proxytunnel.sf.net/files/proxytunnel-%{version}.tgz
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
%setup

### Remove ownership changes from Makefile
%{__perl} -pi.orig -e 's| -[og] root | |g' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__make} install \
	INSTALLPATH="%{buildroot}%{_bindir}" \
	MANPATH="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS LICENSE.txt README
%doc %{_mandir}/man1/proxytunnel.1*
%{_bindir}/proxytunnel

%changelog
* Fri Dec 23 2005 Dag Wieers <dag@wieers.com> - 1.5.0
- Initial package. (using DAR)
