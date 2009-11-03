# $Id$
# Authority: dag
# Upstream: 

%define _bindir /bin

Summary: Program that allows to transform input and output of a terminal
Name: mapchan
Version: 2.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.iceb.vc.ukrtel.net/

Source: http://www.iceb.vc.ukrtel.net/download/mapchan-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mapchan is a program which allows you to transform the input and output
of a terminal (including a serial port terminal). It is useful when:

  * You need to work with various encodings on various virtual
    terminals
  * You have an assortment of terminals, not one of which supports
    your favorite encoding.

This software is an incomplete implementation of the functionality of
the utility "mapchan" of SCO Unix. 

%prep
%setup -n %{name}

%build
#%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 mapchan %{buildroot}%{_bindir}/mapchan
%{__install} -dp -m0755 %{buildroot}%{_sysconfdir}/mapchan/
%{__install} -p -m0644 examples/* %{buildroot}%{_sysconfdir}/mapchan/
%{__install} -Dp -m0644 doc/mapchan.F %{buildroot}%{_mandir}/man5/mapchan.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LSM README* VERSION doc/
%doc %{_mandir}/man5/mapchan.5*
%config(noreplace) %{_sysconfdir}/mapchan/
%{_bindir}/mapchan

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
