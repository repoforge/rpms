# $Id$
# Authority: dries
# Screenshot: http://psi.affinix.com/gfx/screenshots/iceram-roster.png
# ScreenshotURL: http://psi.affinix.com/?page=screenshots

%define desktop_vendor rpmforge
%define tls_plugin     qca-tls-1.0
%define qtdir          %(echo ${QTDIR})

Summary: Client application for the Jabber network
Name: psi
Version: 0.9.2
Release: 1
License: GPL
Group: Applications/Communications
URL: http://psi.affinix.com/
Source0: http://dl.sf.net/psi/psi-%{version}.tar.bz2
Source1: http://psi.affinix.com/beta/%{tls_plugin}.tar.bz2
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
BuildRequires: XFree86-devel, kdelibs-devel, openssl-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Obsoletes: psi-iconsets < 0.9.1

%description
Psi is a client program for the Jabber messaging network. It supports
multiple accounts, group chat, Unicode and SSL encryption.


%package languagepack
Summary: Translations for the Psi jabber client
Group: Applications/Communications
Requires: %{name} = %{version}

%description languagepack
This package contains the necessairy files for using the jabber client Psi
in other languages than English.


%prep
%setup -a 1

%build
# It's not an autoconf generated script...
# The PWD thing is an ugly hack since relative paths mess everything up...
./configure \
    --prefix="${PWD}/src%{_prefix}" \
    --bindir="${PWD}/src%{_bindir}" \
    --libdir="${PWD}/src%{_datadir}/%{name}"
%{__perl} -pi.orig -e "s|${PWD}||g" Makefile
%{__make} %{?_smp_mflags}

# Transport Layer Security plugin
# Again, impossible to get the prefix right easily (see install below)...
pushd %{tls_plugin}
    ./configure
    %{__make}
popd


%install
%{__rm} -rf %{buildroot}

# That trailing "/" is mandatory because of "$(INSTALL_ROOT)usr" type of lines
%{__make} install INSTALL_ROOT="%{buildroot}/"

# Transport Layer Security plugin
%{__install} -D -m 0755 %{tls_plugin}/libqca-tls.so \
    %{buildroot}%{qtdir}/plugins/crypto/libqca-tls.so

# Install the pixmap for the menu entry
%{__install} -D -m 0644 iconsets/system/default/icon_32.png \
    %{buildroot}%{_datadir}/pixmaps/psi.png

# Install an enhanced menu entry (supplied psi.desktop is sparse)
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Psi Jabber Client
Comment=Connect and chat on the Jabber network
Icon=psi.png
Exec=psi -caption "%%c" %%i %%m
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Network;
StartupNotify=true
EOF

%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -D -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Internet/%{name}.desktop
%endif
 
# Install the languagepack files
%{__install} -m 0644 \
    %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} \
    %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} \
    %{SOURCE30} %{SOURCE31} %{SOURCE32} \
    %{buildroot}%{_datadir}/psi


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%{_bindir}/psi
%exclude %{_datadir}/psi/COPYING
%exclude %{_datadir}/psi/README
%exclude %{_datadir}/psi/*.qm
%{_datadir}/psi
%{qtdir}/plugins/crypto/libqca-tls.so
%{_datadir}/pixmaps/psi.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{?_without_freedesktop:%{_sysconfdir}/X11/applnk/Internet/%{name}.desktop}

%files languagepack
%lang(ca) %{_datadir}/%{name}/psi_ca.qm
%lang(cs) %{_datadir}/%{name}/psi_cs.qm
%lang(de) %{_datadir}/%{name}/psi_de.qm
%lang(el) %{_datadir}/%{name}/psi_el.qm
%lang(es) %{_datadir}/%{name}/psi_es.qm
%lang(fr) %{_datadir}/%{name}/psi_fr.qm
%lang(it) %{_datadir}/%{name}/psi_it.qm
%lang(mk) %{_datadir}/%{name}/psi_mk.qm
%lang(nl) %{_datadir}/%{name}/psi_nl.qm
%lang(pl) %{_datadir}/%{name}/psi_pl.qm
%lang(se) %{_datadir}/%{name}/psi_se.qm
%lang(sk) %{_datadir}/%{name}/psi_sk.qm
%lang(zh) %{_datadir}/%{name}/psi_zh.qm


%changelog
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

