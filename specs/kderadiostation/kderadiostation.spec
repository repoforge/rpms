# $Id$
# Authority: dries
# Upstream: Josef Spillner <spillner$kde,org>

# Screenshot: http://kderadiostation.coolprojects.org/shots/kderadioshot1.thumb.png
# ScreenshotURL: http://kderadiostation.coolprojects.org/screenshots.html

# ExcludeDist: fc1 el3

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Tool which presents you a list of internet streaming radio stations
Name: kderadiostation
Version: 0.6
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://kderadiostation.coolprojects.org/

Source: http://kderadiostation.coolprojects.org/source/kderadiostation-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, gettext, libjpeg-devel, libpng-devel
BuildRequires: zlib-devel
BuildRequires: arts-devel, qt-devel, kdelibs-devel
%{?el4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}

%description
This tool presents you a list of internet streaming radio stations. Just
select your favorite one, and xmms or noatun will pick up the right stream.

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/kderadiostation
%{_datadir}/applnk/Multimedia/kderadiostation.desktop
%{_datadir}/apps/kderadiostation
%{_datadir}/config/kderadiostationrc
%{_datadir}/icons/*/*/apps/kderadiostation.png
%{_libdir}/kde3/*.so.*
%{_libdir}/kde3/*.la
%{_libdir}/kde3/*.so

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> 0.6-1
- update to version 0.6

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.5-3
- cleanup of spec file

* Sat Dec 27 2003 Dries Verachtert <dries@ulyssis.org> 0.5-2
- added %post and %postun: /sbin/ldconfig

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.5-1
- first packaging for Fedora Core 1

