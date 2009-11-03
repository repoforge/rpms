# $Id$
# Authority: dag

Summary: Console application which monitors network traffic and bandwidth usage in real time
Name: nload
Version: 0.7.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.roland-riegel.de/nload/

Source: http://dl.sf.net/nload/nload-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel >= 5.0, gcc-c++

%description
nload is a console application which monitors network traffic and bandwidth
usage in real time. It visualizes the in and outgoing traffic using two graphs
and provides additional info like total amount of transfered data and min/max
network usage.

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
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/nload.1*
%{_bindir}/nload

%changelog
* Sun Jun 29 2008 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun Feb 03 2008 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Fri Jan 27 2006 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Initial package. (using DAR)
