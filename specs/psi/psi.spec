# $Id$

# Authority: dries

# NeedsCleanup

%define	_name		psi
%define	_version	0.9.1
%define _release	1.dries

Summary: Qt program for connecting to the Jabber messaging network
Summary(nl): Qt programma om te verbinden met het Jabber messaging netwerk

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Applications/Communications
URL: http://psi.affinix.com/
Source: http://dl.sf.net/psi/psi-0.9.1.tar.bz2
Source50: http://psi.affinix.com/beta/qca-tls-1.0.tar.bz2
Obsoletes: psi-iconsets

#Source1: aqualight.zip
#Source2: aquaploum.zip
#Source3: bluekeramik.zip
#Source4: businessblack.zip
#Source5: crystal.zip
#Source6: gabber.zip
#Source7: icq2.zip
#Source8: jilly.zip
#Source9: licq.zip
#Source10: mike.zip
#Source11: psi_dudes.zip
#Source12: smiley.zip
#Source13: thomas.zip
#Source14: beos.zip
#Source15: cosmic.zip

Source20: psi_pl.qm
Source21: psi_sr.qm
Source22: psi_fr.qm
Source23: psi_eo.qm
Source24: psi_sr@Latn.qm
Source25: psi_fi.qm
Source26: psi_cs.qm
Source27: psi_it.qm
Source28: psi_sk.qm
Source29: psi_el.qm
Source30: psi_ca.qm
Source31: psi_ptbr.qm
Source32: psi_se.qm
Source33: psi_ru.qm
Source34: psi_de.qm
Source35: psi_es.qm
Source36: psi_mk.qm
Source37: psi_nl.qm


BuildRequires: gcc, make, gcc-c++, XFree86-devel, qt-devel, openssl, openssl-devel
Requires: qt, openssl

#(d) primscreenshot: http://psi.affinix.com/gfx/screenshots/iceram-roster.png
#(d) screenshotsurl: http://psi.affinix.com/?page=screenshots
#(d) comment: 

%description
Psi is a client program for the Jabber messaging network. It supports
multiple accounts, group chat, Unicode and encryption with SSL.

%description -l nl
Psi is een client programma voor het Jabber messaging netwerk. Het
ondersteunt meerdere accounts, chatten met een groep, Unicode en encryptie
via SSL.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
# psi doesn't use normal autoconf scripts
. /etc/profile.d/qt.sh
export KDEDIR=/usr
./configure --prefix=/usr 
make
#mkdir iconsets/aqualight
#unzip -d iconsets/aqualight %{SOURCE1}
#mkdir iconsets/aquaploum
#unzip -d iconsets/aquaploum %{SOURCE2}
#mkdir iconsets/bluekeramik
#unzip -d iconsets/bluekeramik %{SOURCE3}
#mkdir iconsets/businessblack
#unzip -d iconsets/businessblack %{SOURCE4}
#mkdir iconsets/crystal
#unzip -d iconsets/crystal %{SOURCE5}
#mkdir iconsets/gabber
#unzip -d iconsets/gabber %{SOURCE6}
#mkdir iconsets/icq2
#unzip -d iconsets/icq2 %{SOURCE7}
#mkdir iconsets/jilly
#unzip -d iconsets/jilly %{SOURCE8}
#mkdir iconsets/licq
#unzip -d iconsets/licq %{SOURCE9}
#mkdir iconsets/mike
#unzip -d iconsets/mike %{SOURCE10}
#mkdir iconsets/psi_dudes
#unzip -d iconsets/psi_dudes %{SOURCE11}
#mkdir iconsets/smiley
#unzip -d iconsets/smiley %{SOURCE12}
#mkdir iconsets/thomas
#unzip -d iconsets/thomas %{SOURCE13}
#mkdir iconsets/beos
#unzip -d iconsets/beos %{SOURCE14}
#mkdir iconsets/cosmic
#unzip -d iconsets/cosmic %{SOURCE15}

# ssl plugin
tar -xjvf %{SOURCE50}
(cd qca-tls-1.0; ./configure; make)

%install
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
cp %{SOURCE33} ${DESTDIR}/usr/share/psi
cp %{SOURCE34} ${DESTDIR}/usr/share/psi
cp %{SOURCE35} ${DESTDIR}/usr/share/psi
cp %{SOURCE36} ${DESTDIR}/usr/share/psi
cp %{SOURCE37} ${DESTDIR}/usr/share/psi
 
# ssl plugin
mkdir -p ${DESTDIR}/usr/lib/qt-3.1/plugins/crypto/
cp -f "qca-tls-1.0/libqca-tls.so" "${DESTDIR}/usr/lib/qt-3.1/plugins/crypto/libqca-tls.so"
strip --strip-unneeded "${DESTDIR}/usr/lib/qt-3.1/plugins/crypto/libqca-tls.so"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig




#%package iconsets
#Summary: some additional iconsets for the jabber client Psi
#Summary(nl): enkele extra iconsets voor de jabber client Psi
#Group: Applications/Communications
#Requires: psi = %{version}-%{release}

#%description iconsets
#This package contains some additional iconsets for the jabber client Psi.

#%description iconsets -l nl
#Dit package bevat enkele extra iconsets voor de jabber client Psi.


%package languagepack
Summary: translations of the jabber client Psi
Summary(nl): vertalingen van de jabber client Psi
Group: Applications/Communications
Requires: psi = %{version}-%{release}

%description languagepack
This package contains the necessairy files for using the jabber client Psi
in other languages then English.

%description languagepack -l nl
Dit package bevat de nodige bestanden om de jabber client Psi te gebruiken
in andere talen dan Engels (o.a. Nederlands)

%files
%defattr(-,root,root)
%doc README COPYING TODO
/usr/bin/psi
/usr/share/psi/certs
#/usr/share/psi/image
/usr/share/psi/sound
#/usr/share/psi/iconsets/stellar
#/usr/share/psi/iconsets/thomas
/usr/lib/qt-3.1/plugins/crypto/libqca-tls.so
/usr/share/icons/hicolor/*/apps/psi.png
/usr/share/applnk/Internet/psi.desktop
/usr/share/psi/iconsets
#/usr/share/psi/iconsets/aqualight
#/usr/share/psi/iconsets/aquaploum
#/usr/share/psi/iconsets/beos
#/usr/share/psi/iconsets/bluekeramik
#/usr/share/psi/iconsets/businessblack
#/usr/share/psi/iconsets/cosmic
#/usr/share/psi/iconsets/crystal
#/usr/share/psi/iconsets/gabber
#/usr/share/psi/iconsets/icq2
#/usr/share/psi/iconsets/jilly
#/usr/share/psi/iconsets/licq
#/usr/share/psi/iconsets/lightbulb
#/usr/share/psi/iconsets/mike
#/usr/share/psi/iconsets/psi_dudes
#/usr/share/psi/iconsets/smiley

%files languagepack
/usr/share/psi/psi_*.qm

%changelog
* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 0.9.1-1.dries
- great, i finish uploading the 0.9 rpms to the webserver and 0.9.1 is
released (spike tells so on irc). Ok upgrade..
- add ssl plugin
- all the iconsets seems to be contained within the 0.9.1 now

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 0.9-2.dries
- further packaging, added iconsets and language packs

* Thu Jan 1 2004 Dries Verachtert <dries@ulyssis.org> 0.9-1.dries
- first packaging for Fedora Core 1
