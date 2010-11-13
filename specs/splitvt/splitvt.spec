# $Id$
# Authority: dag

Summary: Splits any VT100 terminal window into two shell window
Name: splitvt
Version: 1.6.5
Release: 1%{?dist}
License: GPL
Group: System Environment/Console
URL: http://www.devolution.com/~slouken/projects/splitvt/

Source: http://www.devolution.com/~slouken/projects/splitvt/splitvt-%{version}.tar.gz
Patch0: splitvt-1.6.5-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This program takes any VT100 terminal window and splits it into two shell
windows, one on top and one on bottom. It allows you to watch two terminal
sessions at once, which can be very useful whenever you want more screen
real-estate without messing with windows. 

%prep
%setup
%patch0 -p0 -b .orig
%{__rm} -f Makefile

%build
./configure -q
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#%{__install} -Dp -m0755 splitvt.1 %{buildroot}%{_mandir}/man1/splitvt.1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE BLURB COPYING README TODO splitvt-1.6.5.lsm
%doc escapes/* examples/*
%doc %{_mandir}/man1/splitvt.1*
%{_bindir}/splitvt
%{_bindir}/xsplitvt

%changelog
* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 1.6.5-1
- Initial package. (using DAR)
