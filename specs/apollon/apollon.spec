# $Id$

# Authority: dries

Summary: a KDE filesharing client which uses gift.
Name: apollon
Version: 0.9.2
Release: 3
License: GPL
Group: Applications/Internet
URL: http://apollon.sf.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/apollon/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel, gift
Requires: kdelibs, gift

#(d) primscreenshot: http://apollon.sourceforge.net/apollon1.png
#(d) screenshotsurl: http://apollon.sourceforge.net/pictures.html
#(d) comment: nog geen opennap plugin

%description
A KDE filesharing client which uses gift.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
export DESTDIR=$RPM_BUILD_ROOT
make install-strip
rm ${DESTDIR}/usr/share/applnk/Applications/Apollon.desktop
mkdir -p ${DESTDIR}/usr/share/applications/
cat > ${DESTDIR}/usr/share/applications/Apollon.desktop <<EOF
[Desktop Entry]
Name=Apollon
Comment=File Sharing Client
Exec=apollon
Type=Application
Terminal=0
Icon=apollon
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root, 0755)
%doc README
%{_bindir}/apollon
/usr/lib/libapollon.la
/usr/lib/libapollon.so.0
/usr/lib/libapollon.so
/usr/lib/libapollon.so.0.0.1
/usr/share/applications/Apollon.desktop
/usr/share/apps/apollon/gift/OpenFT.conf.template
/usr/share/apps/apollon/gift/giftd.conf.template
/usr/share/apps/apollon/gift/nodes
/usr/share/apps/apollon/gift/ui.conf.template
/usr/share/doc/HTML/en/apollon/*
/usr/share/icons/crystalsvg/*/filesystems/folder_apollon.png
/usr/share/icons/hicolor/16x16/actions/gnutelladown.png
/usr/share/icons/hicolor/16x16/actions/gnutellaup.png
/usr/share/icons/hicolor/16x16/actions/kazaadown.png
/usr/share/icons/hicolor/16x16/actions/kazaaup.png
/usr/share/icons/hicolor/16x16/actions/napsterdown.png
/usr/share/icons/hicolor/16x16/actions/napsterup.png
/usr/share/icons/hicolor/16x16/actions/openftdown.png
/usr/share/icons/hicolor/16x16/actions/openftup.png
/usr/share/icons/hicolor/16x16/actions/soulseekdown.png
/usr/share/icons/hicolor/16x16/actions/soulseekup.png
/usr/share/icons/hicolor/*/apps/apollon.png
/usr/share/icons/hicolor/*/apps/gnutella.png
/usr/share/icons/hicolor/*/apps/kazaa.png
/usr/share/icons/hicolor/*/apps/napster.png
/usr/share/icons/hicolor/*/apps/openft.png
/usr/share/icons/hicolor/*/apps/soulseek.png
/usr/share/locale/*/LC_MESSAGES/apollon.mo

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

