# $Id$
# Authority: dag
# Upstream: <socat$dest-unreach,org>

Summary: Relay for bidirectional data transfer between 2 channels
Name: socat
Version: 1.6.0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.dest-unreach.org/socat/

Source: http://www.dest-unreach.org/socat/download/socat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel, openssl-devel
Requires: tcp_wrappers

%description
socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (serial line
etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
line editor, a program, or a combination of two of these.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGREPORTS CHANGES COPYING* DEVELOPMENT EXAMPLES FAQ FILES PORTING README SECURITY
%doc *.sh doc/*.css doc/*.help doc/*.html
%doc %{_mandir}/man1/socat.1*
%{_bindir}/filan
%{_bindir}/procan
%{_bindir}/socat

%changelog
* Sun Feb 10 2008 Dag Wieers <dag@wieers.com> - 1.6.0.1-1
- Updated to release 1.6.0.1.

* Sat Mar 10 2007 Dag Wieers <dag@wieers.com> - 1.6.0.0-1
- Updated to release 1.6.0.0.

* Wed Jul 19 2006 Dag Wieers <dag@wieers.com> - 1.5.0.0-1
- Updated to release 1.5.0.0.

* Tue Jan 31 2006 Dag Wieers <dag@wieers.com> - 1.4.3.1-1
- Updated to release 1.4.3.1.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 1.4.3.0-1
- Updated to release 1.4.3.0.

* Sat Mar 19 2005 Dag Wieers <dag@wieers.com> - 1.4.2.0-1
- Updated to release 1.4.2.0.

* Sun Nov 14 2004 Dag Wieers <dag@wieers.com> - 1.4.0.3-1
- Updated to release 1.4.0.3.

* Sat Sep 25 2004 Dag Wieers <dag@wieers.com> - 1.4.0.2-1
- Updated to release 1.4.0.2.

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 1.4.0.0-1
- Updated to release 1.4.0.0.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.3.2.2-1
- Initial package. (using DAR)
