# $Id$
# Authority: dries

# Screenshot: http://www.kmyirc.de/images/screenshots/thumb_kmyirc-01.png
# ScreenshotURL: http://www.kmyirc.de/screenshots.php?handed=0

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Internet Relay Chat client for KDE
Name: kmyirc
Version: 0.2.9
Release: 5%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.kmyirc.de/

Source: http://dl.sf.net/kmyirc/kmyirc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libart_lgpl-devel, gettext, arts-devel, libjpeg-devel
BuildRequires: libpng-devel, gcc, gcc-c++, make
BuildRequires: kdelibs-devel, qt-devel, zlib-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}

%description
An Internet Relay Chat (IRC) client for KDE.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO
%{_bindir}/kmyirc
%{_libdir}/lib*
%{_datadir}/apps/kmyirc/icons/*
%{_datadir}/apps/kmyirc/pics/*
%{_datadir}/doc/HTML/en/kmyirc
%{_datadir}/applnk/Internet/kmyirc.desktop
%{_datadir}/icons/locolor/32x32/apps/kmyirc.png
%{_datadir}/icons/locolor/16x16/apps/kmyirc.png
%{_datadir}/config/kmyircrc

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.9-5
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.2.9-4
- Spec file cleanup, use %%find_lang.

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.2.9-4
- cleanup of spec file, fix

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 0.2.9-3
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.2.9-2
- cleanup of spec file

* Sat Nov 29 2003 Dries Verachtert <dries@ulyssis.org> 0.2.9-1
- first packaging for Fedora Core 1
