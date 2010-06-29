# $Id$
# Authority: dag
# Upstream: Andrew Patterson <andrew-spew@fwe.com>

Summary: I/O performance measurement and load generation tool
Name: spew
Version: 1.0.8
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://spew.berlios.de/

Source: ftp://ftp.berlios.de/pub/spew/1.0.4/spew-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, ncurses-devel

%description
Spew is used to measure I/O performance of character devices, block devices,
and regular files. It can also be used to generate high I/O loads to stress
systems while verifying data integrity.

Spew is easy to use and is flexible. No configuration files or complicated
client/server configurations are needed. Spew also generates its own data
patterns that are designed to make it easy to find and debug data integrity
problems.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/gorge.1*
%doc %{_mandir}/man1/regorge.1*
%doc %{_mandir}/man1/spew.1*
%config(noreplace) %{_sysconfdir}/spew.conf
%{_bindir}/gorge
%{_bindir}/regorge
%{_bindir}/spew

%changelog
* Thu Jun 24 2010 Dag Wieers <dag@wieers.com> - 1.0.8-1
- Updated to release 1.0.8.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Initial package. (using DAR)
