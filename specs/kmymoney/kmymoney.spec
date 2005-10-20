# $Id$
# Authority: dries

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

%define real_name kmymoney2

Summary: Double-entry accounting software package
Name: kmymoney
Version: 0.8
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://kmymoney2.sourceforge.net/

Source: http://dl.sf.net/kmymoney2/kmymoney2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext 
BuildRequires: zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
KMyMoney is striving to be a full-featured replacement for your
Windows-based finance software. We are a full double-entry accounting
software package, for personal or small-business use.

%prep
%setup -n %{real_name}-%{version}

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall
%find_lang %{real_name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog ChangeLog.original COPYING INSTALL README TODO
%doc %{_datadir}/doc/HTML/en/kmymoney2
%doc %{_mandir}/man?/*
%{_datadir}/apps/kmymoney2
%{_datadir}/applnk/Applications/kmymoney2.desktop
%{_datadir}/icons/*/*/apps/kmymoney2.png
%{_datadir}/icons/*/*/mimetypes/kmy.png
%{_datadir}/mimelnk/application/x-kmymoney2.desktop
%{_bindir}/*

%changelog
* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Sun Jun 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Initial package.
