# $Id$

# Authority: dries
# Upstream: 

Summary: KDE filesharing client which uses gift
Name: apollon
%{?fc2:Version: 0.9.3.2}
%{?fc2:%define real_version 0.9.3}
%{?fc1:Version: 0.9.2}
%{?fc1:%define real_version 0.9.2}
Release: 1
License: GPL
Group: Applications/Internet
URL: http://apollon.sf.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/apollon/%{name}-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel, gift
%{?fc2:BuildRequires: selinux}
Requires: kdelibs, gift

# Screenshot: http://apollon.sourceforge.net/apollon1.png
# ScreenshotURL: http://apollon.sourceforge.net/pictures.html

%description
Apollon is a KDE filesharing client which uses gift.

%prep
%setup -n apollon-%{real_version}

%build
. /etc/profile.d/qt.sh
for i in $(find . -type f | egrep '\.ui'); do sed -i 's/version="3.2"/version="3.1"/g;' $i; done
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall
rm %{buildroot}/usr/share/applnk/Applications/Apollon.desktop
mkdir -p %{buildroot}/usr/share/applications/
cat > %{buildroot}/usr/share/applications/Apollon.desktop <<EOF
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
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root, 0755)
%doc README
%{_bindir}/apollon
%{_libdir}/libapollon.la
%{_libdir}/libapollon.so.0
%{_libdir}/libapollon.so
%{_libdir}/libapollon.so.0.0.1
%{_datadir}/applications/Apollon.desktop
%{_datadir}/apps/apollon/gift/OpenFT.conf.template
%{_datadir}/apps/apollon/gift/giftd.conf.template
%{_datadir}/apps/apollon/gift/nodes
%{_datadir}/apps/apollon/gift/ui.conf.template
%{_datadir}/doc/HTML/en/apollon/*
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
%{_datadir}/locale/*/LC_MESSAGES/apollon.mo

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

