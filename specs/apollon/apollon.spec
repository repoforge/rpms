# $Id$
# Authority: dries

# Screenshot: http://apollon.sourceforge.net/apollon1.png
# ScreenshotURL: http://apollon.sourceforge.net/pictures.html

Summary: KDE filesharing client which uses gift
Name: apollon
%{?fc2:Version: 0.9.3.2}
%{?fc2:%define real_version 0.9.3}
%{?fc1:Version: 0.9.2}
%{?fc1:%define real_version 0.9.2}
Release: 1
License: GPL
Group: Applications/Internet
URL: http://apollon.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/apollon/apollon-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext, XFree86-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, gift
%{?fc2:BuildRequires: libselinux-devel}
Requires: kdelibs, gift

%description
Apollon is a KDE filesharing client which uses gift.

%prep
%setup -n apollon-%{real_version}

%{__cat} <<EOF >apollon.desktop
[Desktop Entry]
Name=Apollon
Comment=File Sharing Client
Exec=apollon
Type=Application
Terminal=false
Icon=apollon
Encoding=UTF-8
Categories=Application;Network;
EOF

%build
source /etc/profile.d/qt.sh
for i in $(find . -type f | egrep '\.ui'); do sed -i 's/version="3.2"/version="3.1"/g;' $i; done
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source  /etc/profile.d/qt.sh
%{__install} -d -m0755 %{buildroot}%{_datadir}/apps/apollon
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor kde                  \
	--dir %{buildroot}%{_datadir}/applications \
	--add-category X-Red-Hat-Extras            \
	apollon.desktop

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README
%doc %{_docdir}/HTML/en/apollon/*
%{_bindir}/apollon
%exclude %{_libdir}/libapollon.la
%{_libdir}/libapollon.so*
%exclude %{_datadir}/applnk/Applications/Apollon.desktop
%{_datadir}/applications/kde-apollon.desktop
%{_datadir}/apps/apollon/
%{_datadir}/icons/crystalsvg/*/filesystems/folder_apollon.png
%{_datadir}/icons/hicolor/16x16/actions/gnutelladown.png
%{_datadir}/icons/hicolor/16x16/actions/gnutellaup.png
%{_datadir}/icons/hicolor/16x16/actions/kazaadown.png
%{_datadir}/icons/hicolor/16x16/actions/kazaaup.png
%{_datadir}/icons/hicolor/16x16/actions/napsterdown.png
%{_datadir}/icons/hicolor/16x16/actions/napsterup.png
%{_datadir}/icons/hicolor/16x16/actions/openftdown.png
%{_datadir}/icons/hicolor/16x16/actions/openftup.png
%{_datadir}/icons/hicolor/16x16/actions/soulseekdown.png
%{_datadir}/icons/hicolor/16x16/actions/soulseekup.png
%{_datadir}/icons/hicolor/*/apps/apollon.png
%{_datadir}/icons/hicolor/*/apps/gnutella.png
%{_datadir}/icons/hicolor/*/apps/kazaa.png
%{_datadir}/icons/hicolor/*/apps/napster.png
%{_datadir}/icons/hicolor/*/apps/openft.png
%{_datadir}/icons/hicolor/*/apps/soulseek.png

%changelog
* Thu Feb 25 2004 Dries Verachtert <dries@ulyssis.org> 0.9.2-3
- moved the apollon menu entry to 'more internet applications'
  bug found by Sindre Pedersen Bjørda, thanks!

* Wed Feb 25 2004 Dries Verachtert <dries@ulyssis.org> 0.9.2-2
- removed the dependencies on gift plugins
  bug found by Sindre Pedersen Bjørda, thanks!

* Wed Feb 4 2004 Dries Verachtert <dries@ulyssis.org> 0.9.2-1
- update to version 0.9.2

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.9.1-2
- spec file cleanup
- other desktop file

* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.9.1-1
- first packaging for Fedora Core 1

