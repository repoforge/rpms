# $Id$
# Authority: matthias

%{?el6:%undefine _with_mozilla}
%{?el6:%define mozilla xulrunner-devel nspr-devel}
%{?el6:%define _without_lirc 1}

%{?el5:%undefine _with_mozilla}
%{?el5:%define mozilla xulrunner-devel nspr-devel}

%{?el4:%define _with_mozilla 1}
%{?el4:%define _without_modxorg 1}
%{?el4:%define mozilla seamonkey-devel}

%{?el3:%define _with_mozilla 1}
%{?el3:%define _without_modxorg 1}
%{?el3:%define mozilla seamonkey-devel}

%define desktop_vendor rpmforge

Summary: Frontend for the xine multimedia library
Name: gxine
Version: 0.5.905
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://xinehq.de/

Source: http://dl.sf.net/xine/gxine-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: gtk2-devel >= 2.8
BuildRequires: js-devel
BuildRequires: xine-lib-devel >= 1.0.0
# This is checked at configure time :-( - Build fails as of 0.5.9
# gtkvideo.c:2004: error: 'priv' undeclared (first use in this function)
#Buildrequires: gnome-screensaver, dbus-glib-devel
%{!?_without_lirc:BuildRequires: lirc-devel}
%{?_with_mozilla:BuildRequires: %{mozilla}}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_modxorg:BuildRequires: libXaw-devel, libXtst-devel, libXinerama-devel, libXrandr-devel}

%description
xine is a fully-featured free audio/video player for unix-like systems which
uses libxine for audio/video decoding and playback. For more informations on
what formats are supported, please refer to the libxine documentation.
gxine is a gtk based gui for this xine-library alternate to xine-ui.

Available rpmbuild rebuild options :
--without : freedesktop

%prep
%setup

%{__perl} -pi.orig -e 's|(\@XTEST_LIBS\@)|$1 \@X_LIBS\@|g' Makefile.in */Makefile.in

%build
%configure \
    %{?_without_lirc:--disable-lirc} \
    --with-spidermonkey=%{_prefix} \
    --with-dbus \
    --with-logo-format="auto"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang gxine
%find_lang gxine.theme
# Have both translation sets of files included (is there a better way?)
%{__cat} gxine.theme.lang >> gxine.lang

%clean
%{__rm} -rf %{buildroot}

%files -f gxine.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_mandir}/man1/gxine*.1*
%doc %lang(de) %{_mandir}/de/man1/gxine*.1*
%doc %lang(es) %{_mandir}/es/man1/gxine*.1*
%dir %{_sysconfdir}/gxine/
%config(noreplace) %{_sysconfdir}/gxine/*
%{_bindir}/gxine*
#%{_datadir}/applications/%{desktop_vendor}-gxine.desktop
%{_datadir}/applications/gxine.desktop
#%{_datadir}/application-registry/gxine.applications
%{_datadir}/gxine/
%{_datadir}/icons/*/*/apps/gxine.png
%{_datadir}/pixmaps/gxine.png
%{_libdir}/gxine/
%exclude %{_libdir}/gxine/*.la

%changelog
* Wed Oct 03 2012 Denis Fateyev <denis@fateyev.com> - 0.5.905-2
- Library dependencies fix

* Mon Jan 11 2010 Dag Wieers <dag@wieers.com> - 0.5.905-1
- Updated to release 0.5.905.

* Thu Jul 09 2009 Dag Wieers <dag@wieers.com> - 0.5.904-1
- Updated to release 0.5.904.

* Fri Feb 02 2007 Dag Wieers <dag@wieers.com> - 0.5.11-1
- Updated to release 0.5.11.

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 0.5.10-1
- Update to 0.5.10.

* Mon Dec 18 2006 Matthias Saou <http://freshrpms.net/> 0.5.9-1
- Update to 0.5.9.

* Fri May 05 2006 Dag Wieers <dag@wieers.com> - 0.5.6-1
- Updated to release 0.5.6.

* Wed Mar 08 2006 Dag Wieers <dag@wieers.com> - 0.5.5-1
- Updated to release 0.5.5.

* Fri Jan 26 2006 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Updated to release 0.5.4.

* Sun Jan 01 2006 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Updated to release 0.5.3.

* Thu Dec 22 2005 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Sun Aug 01 2004 Dag Wieers <dag@wieers.com> - 0.3.3-3
- Added gxine.applications to application-registry.

* Mon Jun 07 2004 Dag Wieers <dag@wieers.com> - 0.3.3-3
- Added improved desktop file.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.3.3-2
- Rebuild for Fedora Core 1.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.3.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Mar 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.2.

* Sun Mar 16 2003 Matthias Saou <http://freshrpms.net/>
- Added freedesktop build option.

* Mon Mar 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Sun Mar  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.

* Tue Feb 25 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Converted desktop entry.

* Mon Dec 16 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- removed alle packman specific and added to gnome-xine cvs

* Sat Dec 07 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- Update to gxine 0.2

* Thu Dec 05 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- initial release

