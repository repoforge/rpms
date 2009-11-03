# $Id$
# Authority: dries
# Upstream: Alexander Theel <alex,theel$gmx,net>

Summary: Manage notes and ideas in tree structures
Name: tuxcards
Version: 1.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://www.tuxcards.de/

Source: http://www.tifskom.de/tux/%{version}/tuxcards-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext

%description
TuxCards provides a hierarical notebook similar to CueCards under Windows.
Every kind of note and idea may be managed and sorted within a tree structure.

%prep
%setup
%{__perl} -pi -e 's|.*ccolorbar.h.*||g;' ./src/gui/dialogs/optionsDialog/IOptionsDialog.ui
%{__perl} -pi -e 's|/usr/local/doc|%{_datadir}|g;' src/CTuxCardsConfiguration.cpp tuxcards.pro
%{__perl} -pi -e 's|/usr/local/bin|%{_bindir}|g;' tuxcards.pro

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Tuxcards
Comment=Manage notes and ideas in tree structures
Icon=tuxcards.xpm
Exec=tuxcards
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Office;
Encoding=UTF-8
EOF

%build
qmake tuxcards.pro
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%{__install} -D ./src/icons/lo32-app-tuxcards.xpm %{buildroot}%{_datadir}/icons/tuxcards.xpm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README
%{_bindir}/tuxcards
%{_datadir}/tuxcards/
%{_datadir}/applications/*tuxcards.desktop
%{_datadir}/icons/tuxcards.xpm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1.2
- Rebuild for Fedora Core 5.

* Mon Feb 13 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
