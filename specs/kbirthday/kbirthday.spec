# $Id: $

# Authority: dries
# Upstream: Jan Hambrecht
# Screenshot: http://www.gfai.de/~jaham/projects/kbirthday/kbirthday-0.5-2.png
# ScreenshotURL: http://www.gfai.de/~jaham/projects/kbirthday/kbirthday.html

Summary: Kicker-applet which reminds you of birthdays
Name: kbirthday
Version: 0.7.3
Release: 1
License: GPL
Group: Applications/Communications
URL: http://www.gfai.de/~jaham/projects/kbirthday/kbirthday.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.gfai.de/~jaham/download/kbirthday-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext, XFree86-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, desktop-file-utils
%{?fc2:BuildRequires: libselinux-devel}

%description
Kbirthday is a kicker-applet that reminds you of birthdays and anniversaries
from your KDE addressbook. It uses the KDE addressbook API to access the 
addressbook data. So you can use your favourite addressbook frontend to manage 
your friends addresses, birthdays and anniversaries. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
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
* Mon Nov 01 2004 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1
- Initial package.
