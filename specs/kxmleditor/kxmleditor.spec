# $Id$

# Authority: dries
# Upstream:
# Screenshot: http://kxmleditor.sourceforge.net/screenshot.png
# ScreenshotURL: http://kxmleditor.sourceforge.net/screenshots.htm

# ExcludeDist: el3

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

Summary: XML Editor
Name: kxmleditor
Version: 1.1.3
Release: 2
License: GPL
Group: Applications/Editors
URL: http://kxmleditor.sourceforge.net/

Source: http://dl.sf.net/kxmleditor/kxmleditor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, arts-devel
BuildRequires: gcc-c++, gettext, zlib-devel, qt-devel
BuildRequires: libjpeg-devel, kdelibs-devel, fam-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}

%description
KXML Editor is program, that display and edit contents of XML file. Main
features:
* Drag and drop editing, clipboard support
* Use DOM level 2 Qt library parser
* KParts technology support
* DCOP technology support
* Editing KOffice compressed files

%prep
%setup

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
sed -i "s/<UI version=\"3.2\" /<UI version=\"3.3\"/g;" $(find . | egrep "\.ui$")
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

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
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/libkxmleditorpart.la
%{_datadir}/applnk/Applications/kxmleditor.desktop
%{_datadir}/apps/kxmleditor/icons/*/*/actions/*.png
%{_datadir}/apps/kxmleditor/*.rc
%{_datadir}/apps/kxmleditor/pics/*.png
%{_datadir}/doc/HTML/en/kxmleditor
%{_datadir}/icons/*/*/apps/kxmleditor.png
%{_datadir}/services/kxmleditorpart.desktop

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.3-3
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Wed Nov 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.1.3-1
- Update to release 1.1.3.

* Sun May 30 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Initial package.
