# $Id$
# Authority: dag
# Upstream: Marc Kirchner <kirchner$stud,fh-heilbronn,de>

Summary: Check TCP connection to a given ip/port
Name: tcping
Version: 1.3.5
Release: 1
License: LGPL
Group: Applications/Internet
URL: http://www.linuxco.de/tcping/tcping.html

Source: http://www.linuxco.de/tcping/tcping-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
tcping does a TCP connect to the given ip/port combination. The user
can specify a timeout in seconds. This is useful in shell scripts
running in firewalled environments. Often SYNs are just being dropped
by firewalls, thus connection establishment will be retried several
times (for minutes) until a TCP timeout is reached. With tcping it
is possible to check first if the desired port is reachable and then
start connection establishment.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 tcping %{buildroot}%{_bindir}/tcping

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_bindir}/tcping

%changelog
* Fri May 08 2009 Dag Wieers <dag@wieers.com> - 1.3.5-1
- Updated to release 1.3.5.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 1.3.4-1
- Updated to release 1.3.4.

* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 1.3.3-1
- Initial package. (using DAR)
