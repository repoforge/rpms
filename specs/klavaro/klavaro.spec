# $Id$
# Authority: dries
# Upstream: fechjo-klavaro00$yahoo,com,br

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Typing tutor
Name: klavaro
Version: 0.9.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://klavaro.sourceforge.net/en/

Source: http://dl.sf.net/klavaro/klavaro-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext, bison
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, desktop-file-utils
BuildRequires: gtk+-devel, gtkextra-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Klavaro  is a touch typing tutor that is very
flexible and supports customizable keyboard
layouts. Users can edit and save new or unknown
keyboard layouts, as the basic course provided by
the program was designed to not depend on specific
layouts.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Klavaro
Comment=Typing tutor
#Icon=name.png
Exec=klavaro
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=KDE;Application;Education;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/klavaro
%{_datadir}/applications/*.desktop

%changelog
* Tue Sep 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Update to release 0.9.2.

* Sat Sep 24 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Update to release 0.9.1.

* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Update to release 0.9.

* Sat Sep 17 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Update to release 0.8.

* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Update to release 0.7.1.

* Sat Aug 20 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Update to release 0.6.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Update to release 0.5.

* Wed Jul 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Update to release 0.4.

* Fri Jul 01 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
