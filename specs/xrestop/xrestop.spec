# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: X resource monitor
Name: xrestop
Version: 0.3
Release: 1
License: GPL
Group: Applications/System
URL: http://www.freedesktop.org/Software/xrestop/

Source: http://freedesktop.org/Software/xrestop/xrestop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}


%description
A utility to monitor the usage of resources within the X Server, and
display them in a manner similar to top.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README 
%doc %{_mandir}/man1/xrestop.1*
%{_bindir}/xrestop

%changelog
* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Wed Dec 24 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
