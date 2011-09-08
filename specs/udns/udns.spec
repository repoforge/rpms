# $Id$
# Authority: dag

Summary: DNS resolver library for both synchronous and asynchronous DNS queries
Name: udns
Version: 0.0.9
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.corpit.ru/mjt/udns.html

Source: http://www.corpit.ru/mjt/udns/udns_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
udns is a resolver library for C (and C++) programs, and a collection
of useful DNS resolver utilities.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
./configure --enable-ipv6
%{__make} %{?_smp_mflags} all sharedlib

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 libudns.so.0 %{buildroot}%{_libdir}/libudns.so.0
%{__ln_s} -f libudns.so.0 %{buildroot}%{_libdir}/libudns.so
%{__install} -Dp -m0755 dnsget %{buildroot}%{_bindir}/dnsget
%{__install} -Dp -m0755 rblcheck %{buildroot}%{_bindir}/rblcheck
%{__install} -Dp -m0444 dnsget.1 %{buildroot}%{_mandir}/man1/dnsget.1
%{__install} -Dp -m0444 rblcheck.1 %{buildroot}%{_mandir}/man1/rblcheck.1

%{__install} -Dp -m0755 libudns.a %{buildroot}%{_libdir}/libudns.a
%{__install} -Dp -m0444 udns.3 %{buildroot}%{_mandir}/man3/udns.3
%{__install} -Dp -m0644 udns.h %{buildroot}%{_includedir}/udns.h

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING.LGPL NEWS NOTES TODO
%doc %{_mandir}/man1/dnsget.1*
%doc %{_mandir}/man1/rblcheck.1*
%{_bindir}/dnsget
%{_bindir}/rblcheck
%{_libdir}/libudns.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/udns.3*
%{_includedir}/udns.h
%{_libdir}/libudns.a
%{_libdir}/libudns.so

%changelog
* Thu Nov 22 2007 Dag Wieers <dag@wieers.com> - 0.0.9-1
- Initial package. (using DAR)
