# $Id$
# Authority: dries

# Screenshot: http://psi-im.org/gfx/screenshots//0.9.3/lin_0-9-3_roster.png
# ScreenshotURL: http://psi-im.org/screenshots

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Client application for the Jabber network
Name: psi
Version: 0.10
Release: 4%{?dist}
License: GPL
Group: Applications/Communications
URL: http://psi-im.org/
Source0: http://dl.sf.net/psi/psi-%{version}.tar.bz2
# Source20: psi_ca.qm
Source21: psi_cs.qm
Source22: psi_de.qm
Source23: psi_el.qm
Source24: psi_es.qm
Source25: psi_fr.qm
# Source26: psi_it.qm
Source27: psi_mk.qm
Source28: psi_nl.qm
Source29: psi_pl.qm
# Source30: psi_se.qm
Source31: psi_sk.qm
Source32: psi_zh.qm
Source33: psi_et.qm
Source34: psi_vi.qm
Source35: psi_ru.qm
Patch0: psi-0.9.2-strip.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, openssl-devel, gcc-c++, zlib-devel, qca-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Obsoletes: psi-iconsets <= %{version}-%{release} 0.9.1

%description
Psi is a client program for the Jabber messaging network. It supports
multiple accounts, group chat, Unicode and SSL encryption.

%package languagepack
Summary: Translations for the Psi jabber client
Group: Applications/Communications
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-i18n <= %{version}-%{release}
Provides: %{name}-i18n = %{version}-%{release}

%description languagepack
This package contains the necessary files for using the jabber client Psi
in other languages than English.

%prep
%setup
%patch0 -p1 -b .strip

#%{__cat} <<EOF >psi.desktop
#[Desktop Entry]
#Name=Psi Jabber Client
#Comment=Connect and chat on the Jabber network
#Icon=psi.png
#Exec=psi -caption "%%c" %%i %%m
#Terminal=false
#Type=Application
#Encoding=UTF-8
#StartupNotify=true
#Categories=Application;Network;
#EOF

%build
source %{_sysconfdir}/profile.d/qt.sh
./configure \
        --prefix="%{_prefix}" \
        --bindir="%{_bindir}" \
        --datadir="%{_datadir}"\
        --qtdir="$QTDIR"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh

%{__make} install INSTALL_ROOT="%{buildroot}"

# Install the pixmap for the menu entry
%{__install} -Dp -m0644 iconsets/system/default/icon_32.png \
    %{buildroot}%{_datadir}/pixmaps/psi.png

#### Cleanup buildroot
#%{__rm} -f %{buildroot}%{_datadir}/applnk/Internet/psi.desktop \
#		%{buildroot}%{_datadir}/icons/hicolor/*/apps/psi.png

#%if %{!?_without_freedesktop:1}0
#%{__mkdir_p} %{buildroot}%{_datadir}/applications
#desktop-file-install \
#    --vendor %{desktop_vendor} \
#    --dir %{buildroot}%{_datadir}/applications \
#    psi.desktop
#%else
#%{__install} -Dp -m0644 psi.desktop \
#    %{buildroot}%{_sysconfdir}/X11/applnk/Internet/psi.desktop
#%endif

# Install the languagepack files
%{__install} -p -m0644 \
    %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} \
    %{SOURCE25} %{SOURCE27} %{SOURCE28} %{SOURCE29} \
    %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} \
    %{buildroot}%{_datadir}/psi/

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%{_bindir}/psi
%{_datadir}/psi/
%{_datadir}/pixmaps/psi.png
%{_datadir}/applications/psi.desktop
%{_datadir}/icons/hicolor/*/apps/psi.png
#%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-psi.desktop}
#%{?_without_freedesktop:%{_sysconfdir}/X11/applnk/Internet/psi.desktop}
%exclude %{_datadir}/psi/COPYING
%exclude %{_datadir}/psi/README
%exclude %{_datadir}/psi/*.qm

%files languagepack
%defattr(-, root, root, 0755)
# %lang(ca) %{_datadir}/psi/psi_ca.qm
%lang(cs) %{_datadir}/psi/psi_cs.qm
%lang(de) %{_datadir}/psi/psi_de.qm
%lang(el) %{_datadir}/psi/psi_el.qm
%lang(es) %{_datadir}/psi/psi_es.qm
%lang(fr) %{_datadir}/psi/psi_fr.qm
# %lang(it) %{_datadir}/psi/psi_it.qm
%lang(mk) %{_datadir}/psi/psi_mk.qm
%lang(nl) %{_datadir}/psi/psi_nl.qm
%lang(pl) %{_datadir}/psi/psi_pl.qm
# %lang(se) %{_datadir}/psi/psi_se.qm
%lang(sk) %{_datadir}/psi/psi_sk.qm
%lang(zh) %{_datadir}/psi/psi_zh.qm
%lang(et) %{_datadir}/psi/psi_et.qm
%lang(vi) %{_datadir}/psi/psi_vi.qm
%lang(ru) %{_datadir}/psi/psi_ru.qm

%changelog
* Wed Jun 06 2007 Dag Wieers <dag@wieers.coM> - 0.10-4
- Removed qca build into seperate qca package.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-3
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sat Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-2
- Fixed the url, thanks to Hal Rottenberg.

* Wed Jan 11 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Thu Jan 20 2005 Derek Atkins <warlord@mit.edu> 0.9.3-2
- Changes for QCA 1.0 support.

* Sun Jan 09 2005 Dries Verachtert <dries@ulyssis.org> 0.9.3-1
- Updated to release 0.9.3.

* Mon Jun 14 2004 Matthias Saou <http://freshrpms.net> 0.9.2-3
- Real fix for mach builds.

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> 0.9.2-2
- fix so iconsets and language files work again

* Fri Jun 11 2004 Matthias Saou <http://freshrpms.net> 0.9.2-1
- Update to 0.9.2 (not the language files yet, not available for now).
- Major spec file cleanup, leaning towards a rewrite :-).

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

