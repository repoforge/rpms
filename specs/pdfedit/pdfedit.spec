# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{!?dtag:%define _with_lesstif 1}
%{?fc6:%define _with_lesstif 1}
%{?fc3:%define _with_lesstif 1}
%{?el2:%define _with_lesstif 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: PDF document editing solution
Name: pdfedit
Version: 0.4.1
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://sourceforge.net/projects/pdfedit/

Source: http://dl.sf.net/pdfedit/pdfedit-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: boost-devel, libpaper-devel, qt-devel
BuildRequires: doxygen, t1lib-devel
%{!?_without_modxorg:BuildRequires: libXpm-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_lesstif:BuildRequires: lesstif-devel}
%{!?_with_lesstif:BuildRequires: openmotif-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Free pdf editing using PdfEdit. Complete editing of pdf documents is made
possible with PDFedit. You can change either raw pdf objects (for advanced
users) or use predefined gui functions. Functions can be easily added as
everything is based on a script.

%prep
%setup

%{__perl} -pi.orig -e 's|(\$\$[A-Z]+_PATH)|\$(QMAKE_DESTDIR)/$1|g' src/gui/pdfedit.pro

%{__cat} <<EOF >pdfedit.desktop
[Desktop Entry]
Name=pdfedit
GenericName=PDF Editor
Comment=Edit .pdf files
Exec=pdfedit
Icon=pdfedit.png
Terminal=false
Type=Application
Categories=Office;
Encoding=UTF-8
EOF

%build
export QMAKESPEC="linux-g++"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install QMAKE_DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 src/gui/icon/pdfedit_icon_16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/pdfedit.png
%{__install} -Dp -m0644 src/gui/icon/pdfedit_icon_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/pdfedit.png
%{__install} -Dp -m0644 src/gui/icon/pdfedit_icon_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/pdfedit.png
%{__install} -Dp -m0644 src/gui/icon/pdfedit_icon_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/pdfedit.png

desktop-file-install --vendor="%{desktop_vendor}" \
    --dir=%{buildroot}%{_datadir}/applications    \
    pdfedit.desktop

%{__mv} -v %{buildroot}%{_docdir}/pdfedit/ rpm-doc/

for file in doc/user/*.html; do
    %{__perl} -pi -e 's|gui/menuAndToolbarsFun/||g; s|gui/||g;' $file
done

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc COPYING rpm-doc/*
%doc %{_mandir}/man1/pdfedit.1*
%{_bindir}/pdfedit
%{_datadir}/applications/%{desktop_vendor}-pdfedit.desktop
%{_datadir}/icons/hicolor/*/apps/pdfedit.png
%{_datadir}/pdfedit/

%changelog
* Wed Jun 11 2008 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Initial package. (using DAR)
