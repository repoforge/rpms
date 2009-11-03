# $Id$

# Authority: dries
# Upstream: Jan Hambrecht
# Screenshot: http://www.gfai.de/~jaham/projects/kbirthday/kbirthday-0.5-2.png
# ScreenshotURL: http://www.gfai.de/~jaham/projects/kbirthday/kbirthday.html

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

Summary: Kicker-applet which reminds you of birthdays
Name: kbirthday
Version: 0.7.3
Release: 2%{?dist}
License: GPL
Group: Applications/Communications
URL: http://www.gfai.de/~jaham/projects/kbirthday/kbirthday.html

Source: http://www.gfai.de/~jaham/download/kbirthday-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel
BuildRequires: arts-devel, gcc-c++, gettext
BuildRequires: zlib-devel, libjpeg-devel
BuildRequires: kdelibs-devel, desktop-file-utils
%{!?_without_selinux:BuildRequires: libselinux-devel}

%description
Kbirthday is a kicker-applet that reminds you of birthdays and anniversaries
from your KDE addressbook. It uses the KDE addressbook API to access the
addressbook data. So you can use your favourite addressbook frontend to manage
your friends addresses, birthdays and anniversaries.

%prep
%setup

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure --with-pic
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/*.so
%{_libdir}/libkbirthday.la
%{_datadir}/apps/kicker/applets/kbirthday.desktop
%{_datadir}/icons/*/*/apps/kbirthday.png

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.3-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Mon Nov 01 2004 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1
- Initial package.
