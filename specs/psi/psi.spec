# $Id$

# Authority: dries
# Screenshot: http://psi.affinix.com/gfx/screenshots/iceram-roster.png
# ScreenshotURL: http://psi.affinix.com/?page=screenshots

# NeedsCleanup

%{?fc2:%define qt_version_dir 3.3}
%{?fc1:%define qt_version_dir 3.1}

Summary: Qt program for connecting to the Jabber messaging network
Name: psi
Version: 0.9.1
Release: 2
License: GPL
Group: Applications/Communications
URL: http://psi.affinix.com/

Source: http://dl.sf.net/psi/psi-%{version}.tar.bz2
Source50: http://psi.affinix.com/beta/qca-tls-1.0.tar.bz2

Source20: psi_ca.qm
Source21: psi_cs.qm
Source22: psi_de.qm
Source23: psi_el.qm
Source24: psi_es.qm
Source25: psi_fr.qm
Source26: psi_it.qm
Source27: psi_mk.qm
Source28: psi_nl.qm
Source29: psi_pl.qm
Source30: psi_se.qm
Source31: psi_sk.qm
Source32: psi_zh.qm


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: psi-iconsets

BuildRequires: gcc, make, gcc-c++, XFree86-devel, qt-devel, openssl, openssl-devel
Requires: qt, openssl

%description
Psi is a client program for the Jabber messaging network. It supports
multiple accounts, group chat, Unicode and encryption with SSL.

%prep
%setup

%build
# psi doesn't use normal autoconf scripts
. /etc/profile.d/qt.sh
export KDEDIR=/usr
./configure --prefix=/usr 
make

# ssl plugin
tar -xjvf %{SOURCE50}
(cd qca-tls-1.0; ./configure; make)

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
export KDEDIR=/usr
test -d "${RPM_BUILD_ROOT}/usr/share/psi/" || mkdir -p "${RPM_BUILD_ROOT}/usr/share/psi/"
#no images? cp -f -pR "image" "${RPM_BUILD_ROOT}/usr/share/psi/"
cp -f -pR "iconsets" "${RPM_BUILD_ROOT}/usr/share/psi/"
cp -f -pR "sound" "${RPM_BUILD_ROOT}/usr/share/psi/"
cp -f -pR "certs" "${RPM_BUILD_ROOT}/usr/share/psi/"
#cp -f -p "README" "${RPM_BUILD_ROOT}/usr/share/psi/"
#cp -f -p "COPYING" "${RPM_BUILD_ROOT}/usr/share/psi/"
test -d "${RPM_BUILD_ROOT}/usr/bin/" || mkdir -p "${RPM_BUILD_ROOT}/usr/bin/"
cp -f "psi" "${RPM_BUILD_ROOT}/usr/bin/psi"
strip "${RPM_BUILD_ROOT}/usr/bin/psi"
mkdir -p ${RPM_BUILD_ROOT}/usr/share/applnk/Internet/
cp psi.desktop ${RPM_BUILD_ROOT}/usr/share/applnk/Internet/

mkdir -p "${RPM_BUILD_ROOT}/usr/share/icons/hicolor/16x16/apps/"
cp -f -p iconsets/system/default/icon_16.png ${RPM_BUILD_ROOT}/usr/share/icons/hicolor/16x16/apps/psi.png
mkdir -p "${RPM_BUILD_ROOT}/usr/share/icons/hicolor/32x32/apps/"
cp -f -p iconsets/system/default/icon_32.png ${RPM_BUILD_ROOT}/usr/share/icons/hicolor/32x32/apps/psi.png
mkdir -p "${RPM_BUILD_ROOT}/usr/share/icons/hicolor/48x48/apps/"
cp -f -p iconsets/system/default/icon_48.png ${RPM_BUILD_ROOT}/usr/share/icons/hicolor/48x48/apps/psi.png
 

cp %{SOURCE20} ${DESTDIR}/usr/share/psi
cp %{SOURCE21} ${DESTDIR}/usr/share/psi
cp %{SOURCE22} ${DESTDIR}/usr/share/psi
cp %{SOURCE23} ${DESTDIR}/usr/share/psi
cp %{SOURCE24} ${DESTDIR}/usr/share/psi
cp %{SOURCE25} ${DESTDIR}/usr/share/psi
cp %{SOURCE26} ${DESTDIR}/usr/share/psi
cp %{SOURCE27} ${DESTDIR}/usr/share/psi
cp %{SOURCE28} ${DESTDIR}/usr/share/psi
cp %{SOURCE29} ${DESTDIR}/usr/share/psi
cp %{SOURCE30} ${DESTDIR}/usr/share/psi
cp %{SOURCE31} ${DESTDIR}/usr/share/psi
cp %{SOURCE32} ${DESTDIR}/usr/share/psi

# ssl plugin
mkdir -p ${DESTDIR}/usr/lib/qt-%{qt_version_dir}/plugins/crypto/
cp -f "qca-tls-1.0/libqca-tls.so" "${DESTDIR}/usr/lib/qt-%{qt_version_dir}/plugins/crypto/libqca-tls.so"
strip --strip-unneeded "${DESTDIR}/usr/lib/qt-%{qt_version_dir}/plugins/crypto/libqca-tls.so"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%package languagepack
Summary: translations of the jabber client Psi
Group: Applications/Communications
Requires: psi = %{version}-%{release}

%description languagepack
This package contains the necessairy files for using the jabber client Psi
in other languages then English.

%files
%defattr(-,root,root,0755)
%doc README COPYING TODO
%{_bindir}/psi
%{_datadir}/psi/certs
%{_datadir}/psi/sound
%{_libdir}/qt-*/plugins/crypto/libqca-tls.so
%{_datadir}/icons/hicolor/*/apps/psi.png
%{_datadir}/applnk/Internet/psi.desktop
%{_datadir}/psi/iconsets

%files languagepack
/usr/share/psi/psi_*.qm

%changelog
* Thu May 27 2004 Dries Verachtert <dries@ulyssis.org> 0.9.1-2
- small changes in spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 0.9.1-1
- great, i finish uploading the 0.9 rpms to the webserver and 0.9.1 is
released (spike tells so on irc). Ok upgrade..
- add ssl plugin
- all the iconsets seems to be contained within the 0.9.1 now

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 0.9-2
- further packaging, added iconsets and language packs

* Thu Jan 1 2004 Dries Verachtert <dries@ulyssis.org> 0.9-1
- first packaging for Fedora Core 1
