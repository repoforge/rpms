# $Id$
# Authority: dries
# Upstream: Stefan Bauer <yoltia-maintain$freenet,de>

%define real_version 0.21.0

Summary: Program for editing image files
Name: yoltia
Version: 0.21.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://people.freenet.de/yoltia

Source: http://people.freenet.de/yoltia/dl/yoltia-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, gcc-c++, desktop-file-utils

%description
Yoltia is a computer program for editing image files. It provides the
functionality to do simple changes to a large number of pictures
quickly and very comfortably and exactly. It can read and write PNG,
XPM, BMP, and in most cases JPEG (depends on the Qt library). It can
use and preview custom compression levels for JPEG and PNG, create
new pictures, rotate pictures with 0.5 degree accuracy, perform color
depth conversion with usage of different dithers, manipulate the RGB
and HSV values and hotkey inverting, and perform resizing, cutting,
and stretching. It has many user orientated zoom modes. A
multi-document interface, quick editing of many pictures via browsing
directories or self-defined file lists, mirroring, clipboard and
drag-and-drop-interaction, and a simple and fast GUI with
hotkey-orientated usage.

%prep
%setup
%{__perl} -pi -e 's|/usr/X11/bin|%{_bindir}|g;' install.sh
%{__perl} -pi -e 's|/usr|%{buildroot}%{_prefix}|g;' install.sh

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Yoltia
Comment=Edit images
Exec=yoltia
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
cd src
%{__rm} -f yoltia
qmake yoltia.pro
lrelease yoltia_de.ts
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_docdir}/packages %{buildroot}%{_datadir}/yoltia
bash install.sh
%{__rm} -Rf %{buildroot}%{_docdir}/packages/yoltia

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHOR BUGS CHANGELOG COPYING README TODO
%{_bindir}/yoltia
%{_datadir}/yoltia/
%{_datadir}/applications/rpmforge-yoltia.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.21.0-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.21.0-1
- Updated to release 0.21.0.

* Thu Mar 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.20.1-1
- Updated to release 0.20.1.

* Thu Mar 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.20.0-1
- Updated to release 0.20.0.

* Tue Feb 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.19.2.0-1
- Updated to release 0.19.2.

* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.19.0.0-1
- Initial package.
