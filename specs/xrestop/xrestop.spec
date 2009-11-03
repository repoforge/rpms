# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: X resource monitor
Name: xrestop
Version: 0.4
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.freedesktop.org/wiki/Software/xrestop

Source: http://projects.o-hand.com/sources/xrestop/xrestop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel
%{!?_without_modxorg:BuildRequires: libXres-devel, libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
xrestop is a utility to monitor the usage of resources within the X Server,
and display them in a manner similar to top.

Xrestop uses the X-Resource extension to provide 'top' like statistics of
each connected X11 client's server side resource usage. It is intended as
a developer tool to aid more efficient server resource usage and debug
server side leakage.

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
%doc %{_mandir}/man1/xrestop.1*
%{_bindir}/xrestop

%changelog
* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Wed Dec 24 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
