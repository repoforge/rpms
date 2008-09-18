# $Id$
# Authority: matthias

%{?el3:%define _without_gettextdevel 1}
%{?rh9:%define _without_gettextdevel 1}
%{?rh7:%define _without_gettextdevel 1}
%{?el2:%define _without_gettextdevel 1}

Summary: Client for ED2K Peer-to-Peer Networks based on eMule
Name: amule
Version: 2.2.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.amule.org/

Source0: http://download.berlios.de/amule/aMule-%{version}.tar.bz2
Source1: emule_logo.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: cryptopp
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: wxGTK-devel >= 2.6.0
BuildRequires: zlib-devel
%{!?_without_gettextdevel:BuildRequires: gettext-devel}

%description
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer Network.
It is originally based on eMule, the popular windows-only client for the
same network.

%prep
%setup -n aMule-%{version}%{?prever}

%build
%configure \
    --disable-rpath \
    --disable-debug \
    --enable-alc \
    --enable-alcc \
    --enable-amule-daemon \
    --enable-amulecmd \
    --enable-cas \
    --enable-utf8-systray \
    --enable-webserver \
    --enable-wxcas
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot} _docs
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}
# Move the docs back to be included with %%doc
%{__mv} %{buildroot}%{_defaultdocdir}/aMule-* _docs
# Fix encoding of the desktop entry
for file in %{buildroot}%{_datadir}/applications/*.desktop; do
    iconv -f ISO8859-1 -t UTF-8 -o tmp.desktop ${file}
    %{__mv} tmp.desktop ${file}
done
# Replace xpm icon with our png one
%{__rm} -f %{buildroot}%{_datadir}/pixmaps/amule.xpm
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/amule.png
%{__perl} -pi -e 's|amule.xpm|amule.png|g' \
    %{buildroot}%{_datadir}/applications/*.desktop

%post
update-desktop-database -q 2>/dev/null || :

%postun
update-desktop-database -q 2>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc _docs/*
%doc %{_mandir}/man1/*.1*
%lang(de) %{_mandir}/de/man1/*.1*
%lang(eu) %{_mandir}/eu/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(hu) %{_mandir}/hu/man1/*.1*
%{_bindir}/alc
%{_bindir}/alcc
%{_bindir}/amule
%{_bindir}/amulecmd
%{_bindir}/amuled
%{_bindir}/amuleweb
%{_bindir}/autostart-xas
%{_bindir}/cas
%{_bindir}/wxcas
%{_bindir}/ed2k
%{_libdir}/xchat/plugins/xas.pl
%{_datadir}/applications/alc.desktop
%{_datadir}/applications/amule.desktop
%{_datadir}/applications/wxcas.desktop
%{_datadir}/amule/
%{_datadir}/cas/
%{_datadir}/pixmaps/alc.xpm
%{_datadir}/pixmaps/amule.png
%{_datadir}/pixmaps/wxcas.xpm

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Wed May 30 2007 Matthias Saou <http://freshrpms.net/> 2.1.3-3
- Include patch to rebuild against wxGTK 2.8 (F7).

* Wed Nov 15 2006 Matthias Saou <http://freshrpms.net/> 2.1.3-2
- Remove all of the alternatives stuff.
- Replace the default (ugly) icon with a much nicer transparent png one.
  Haven't found any nicer replacement for alc.xpm, though.

* Mon Jun 12 2006 Matthias Saou <http://freshrpms.net/> 2.1.3-1
- Update to 2.1.3.

* Mon May 29 2006 Matthias Saou <http://freshrpms.net/> 2.1.2-1
- Update to 2.1.2.

* Sat Mar 18 2006 Matthias Saou <http://freshrpms.net/> 2.1.1-1
- Update to 2.1.1.

* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 2.1.0-1
- Update to 2.1.0.
- Add flex build requirement (optional, and FC4's version it too old anyway).
- Clean up no longer needed build requirements (many!).

* Mon Nov 28 2005 Matthias Saou <http://freshrpms.net/> 2.0.3-2
- Change build requirement s/wxGTK2/wxGTK/.

* Tue Aug  2 2005 Matthias Saou <http://freshrpms.net/> 2.0.3-1
- Update to 2.0.3.

* Wed May 18 2005 Matthias Saou <http://freshrpms.net/> 2.0.1-1
- Update to 2.0.1.
- Change gettext to gettext-devel, since autopoint is required.

* Wed May  4 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-1
- Update to 2.0.0 final.
- Add new man pages.
- Explicitly enable alc, as it no longer gets built otherwise.

* Wed Feb  2 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc8.3
- Really fix the UTF-8 alc.desktop problem... it was converted to stdout.

* Thu Jan 13 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc8.2
- Add update-desktop-database calls and convert desktop entry to UTF-8.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc8.1
- Update to 2.0.0rc8.

* Fri Nov 19 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc7.3
- Disable external cryptopp usage, it's a mess :-(

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc7.2
- Disable embedded crypto to use external cryptopp.
- Add gd-progs and gd-devel build dep for gdlib-config to be found.
- Enable UTF8 systray text.
- Enable alcc (aMule link creator for console).

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc7.1
- Update to 2.0.0rc7.

* Fri Jul 30 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc5.1
- Add "|| :" to alternatives calls to ignore error return codes.

* Wed Jul 21 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc5.1
- Update to 2.0.0rc5.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc4a.1
- Update to 2.0.0rc4a.

* Tue Jul 13 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc4.1
- Update to 2.0.0rc4.
- Add workaround for installed docs.

* Mon May  3 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc3.1
- Update to 2.0.0rc3.

* Tue Feb 17 2004 Matthias Saou <http://freshrpms.net/> 1.2.6-1.fr
- Update to 1.2.6.

* Tue Feb 10 2004 Matthias Saou <http://freshrpms.net/> 1.2.5-1.fr
- Update to 1.2.5.

* Mon Jan 12 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-2.fr
- Added alternatives support for the ed2k binary between amule and xmule.

* Sun Jan 11 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-1.fr
- Initial RPM package.

