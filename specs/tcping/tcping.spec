# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Marc Kirchner <kirchner@stud.fh-heilbronn.de>

Summary: Check TCP connection to a given ip/port
Name: tcping
Version: 1.3.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://stud.fh-heilbronn.de/~kirchner/tcping/tcping.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://stud.fh-heilbronn.de/~kirchner/tcping/tcping-%{version}.tar.gz
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
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 tcping %{buildroot}%{_bindir}/tcping

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_bindir}/*

%changelog
* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 1.3.3-1
- Initial package. (using DAR)
