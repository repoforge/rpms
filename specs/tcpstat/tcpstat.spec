# $Id$
# Authority: dag

Summary: Reports certain network interface statistics
Name: tcpstat
Version: 1.5
Release: 2%{?dist}
License: NSD
Group: Applications/Internet
URL: http://www.frenchfries.net/paul/tcpstat/

Source: http://www.frenchfries.net/paul/tcpstat/tcpstat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
tcpstat reports certain network interface statistics much like vmstat does
for system statistics.

tcpstat gets its information by either monitoring a specific interface, or
by reading previously saved tcpdump data from a file. 

%prep
%setup

%build
%configure 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL LICENSE NEWS README doc/Tips_and_Tricks.txt
%doc %{_mandir}/man1/tcpprof.1*
%doc %{_mandir}/man1/tcpstat.1*
%{_bindir}/tcpstat

%clean
%{__rm} -rf %{buildroot}

%changelog
* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 1.5-2
- Fixed group.

* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
