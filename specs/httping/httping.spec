# $Id$
# Authority: dag
# Upstream: Folkert Vanheusden <folkert$vanheusden,com>

Summary: Ping alike tool for http requests
Name: httping
Version: 1.0.8
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.vanheusden.com/httping/
Source: http://www.vanheusden.com/httping/httping-%{version}.tgz
Patch: httping-1.0.8-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel

%description
Httping is like 'ping' but for http-requests.
Give it an url, and it'll show you how long it takes to connect,
send a request and retrieve the reply (only the headers). Be aware
that the transmission across the network also takes time!

%prep
%setup
%patch -p1 -b .makefile

%build
# The CFLAGS in the makefile are needed, so VERSION is set correctly
# (fixed with the included patch, won't work without)
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" DEBUG=""

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license.txt readme.txt
%{_bindir}/httping
%{_mandir}/man1/httping.1*

%changelog
* Mon Nov 14 2005 Matthias Saou <http://freshrpms.net/> 1.0.8-1
- Update to 1.0.8.
- Add OpenSSL build requirement.

* Sat Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.7-1
- Updated to release 1.0.7.

* Sun Nov 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.6-1
- Updated to release 1.0.6.

* Tue Oct 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1
- Updated to release 1.0.5.

* Fri Aug 05 2005 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Mon Mar 28 2005 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Sun Jan 09 2005 Dag Wieers <dag@wieers.com> - 0.0.96-1
- Updated to release 0.0.96.

* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 0.0.95-1
- Updated to release 0.0.95.

* Wed May 26 2004 Dag Wieers <dag@wieers.com> - 0.0.93-1
- Updated to release 0.0.93.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 0.0.9-1
- Initial package. (using DAR)
