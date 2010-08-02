# $Id$
# Authority: dag
# Upstream: Folkert Vanheusden <folkert$vanheusden,com>

Summary: Ping alike tool for http requests
Name: httping
Version: 1.4.3
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.vanheusden.com/httping/

Source: http://www.vanheusden.com/httping/httping-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
Httping is like 'ping' but for http-requests.
Give it an url, and it'll show you how long it takes to connect,
send a request and retrieve the reply (only the headers). Be aware
that the transmission across the network also takes time!

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
    CFLAGS="%{optflags} -DVERSION=\\\"%{version}\\\" -I/usr/kerberos/include" \
    DEBUG=""

%install
%{__rm} -rf %{buildroot}
#{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 httping %{buildroot}%{_bindir}/httping
%{__install} -Dp -m0644 httping.1 %{buildroot}%{_mandir}/man1/httping.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license.txt readme.txt
%doc %{_mandir}/man1/httping.1*
%{_bindir}/httping

%changelog
* Tue Jul 13 2010 Dag Wieers <dag@wieers.com> - 1.4.3-1
- Updated to release 1.4.3.

* Mon Jan 11 2010 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Thu Dec 31 2009 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Updated to release 1.4.0.

* Thu Dec 31 2009 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Updated to release 1.3.2.

* Wed Aug 12 2009 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Thu Jul 17 2008 Dag Wieers <dag@wieers.com> - 1.2.9-1
- Updated to release 1.2.9.

* Sun Jun 29 2008 Dries Verachtert <dries@ulyssis.org> - 1.2.8-1
- Updated to release 1.2.8.

* Tue May 27 2008 Dag Wieers <dag@wieers.com> - 1.2.6-1 
- Updated to release 1.2.6.

* Wed Jul 11 2007 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Updated to release 1.2.4.

* Sat Nov 11 2006 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Tue Jul 25 2006 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Sun Jan 01 2006 Dag Wieers <dag@wieers.com> - 1.0.9-1
- Updated to release 1.0.9.
- Included fix for broken openssl/kerberos on RH9, EL3 and FC1.

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
