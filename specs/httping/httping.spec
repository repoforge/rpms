# $Id$
# Authority: dag
# Upstream: Folkert Vanheusden <folkert$vanheusden,com>

%{?dist: %{expand: %%define %dist 1}}

Summary: Ping alike tool for http requests
Name: httping
Version: 0.0.93
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.vanheusden.com/httping/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.vanheusden.com/httping/httping-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Httping is like 'ping' but for http-requests.
Give it an url, and it'll show you how long it takes to connect,
send a request and retrieve the reply (only the headers). Be aware
that the transmission across the network also takes time!

%prep
%setup

%{?el3:%{__perl} -pi -e 's|^(CFLAGS=.+)$|$1 -I/usr/kerberos/include|' Makefile}
%{?rh9:%{__perl} -pi -e 's|^(CFLAGS=.+)$|$1 -I/usr/kerberos/include|' Makefile}
%{__perl} -pi.orig -e 's|/usr/bin|\$(bindir)|' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license.txt readme.txt
%{_bindir}/*

%changelog
* Wed May 26 2004 Dag Wieers <dag@wieers.com> - 0.0.93-1
- Updated to release 0.0.93.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 0.0.9-1
- Initial package. (using DAR)
