# $Id$
# Authority: dag
# Upstream: Roland Stigge <stigge$antcom,de>
# Upstream: <gtick-devel$nongnu,org>

%define desktop_vendor rpmforge

Summary: Metronome application
Name: gtick
Version: 0.4.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.antcom.de/gtick/

Source: http://www.antcom.de/gtick/download/gtick-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf >= 2.57, pkgconfig, gtk2-devel, glib2-devel
BuildRequires: desktop-file-utils

%description
gtick is a small metronome application written for Linux and UN*X supporting
different meters (2/4, 3/4, 4/4) and speeds ranging from 30 to 250 bpm. It
utilizes GTK+ and OSS (ALSA compatible).

%prep
%setup

%{__cat} <<EOF >gtick.desktop
[Desktop Entry]
Name=Gtick Metronome
Comment=
Icon=gnome-multimedia.png
Exec=gtick
Terminal=false
Type=Application
Categories=GNOME;Application;AudioVideo;
StartupNotify=true
EOF

%build
#%{__autoconf}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/NOTES NEWS README THANKS TODO
%doc %{_mandir}/man1/gtick.1*
%{_bindir}/gtick
%{_datadir}/applications/%{desktop_vendor}-gtick.desktop

%changelog
* Sat May 31 2008 Dries Verachtert <dries@ulyssis.org> - 0.4.2-1
- Updated to release 0.4.2.

* Sun Aug 19 2007 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Tue May 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.15-1
- Updated to release 0.3.15.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.3.14-1
- Updated to release 0.3.14.

* Mon Feb 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.13-1
- Updated to release 0.3.13.

* Sat Oct 28 2006 Dag Wieers <dag@wieers.com> - 0.3.12-1
- Updated to release 0.3.12.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 0.3.11-1
- Updated to release 0.3.11.

* Fri May 19 2006 Dag Wieers <dag@wieers.com> - 0.3.10-1
- Updated to release 0.3.10.

* Sun Mar 19 2006 Dag Wieers <dag@wieers.com> - 0.3.9-1
- Updated to release 0.3.9.

* Tue Mar 07 2006 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Updated to release 0.3.8.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Updated to release 0.3.7.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Updated to release 0.3.5.

* Wed Jun 16 2004 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Updated to release 0.3.2.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Updated to release 0.3.1.

* Wed Mar 03 2004 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Updated to release 0.3.0.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.2.14-0
- Updated to release 0.2.14.

* Mon Dec 29 2003 Dag Wieers <dag@wieers.com> - 0.2.12-0
- Updated to release 0.2.12.

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 0.2.11-0
- Updated to release 0.2.11.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.2.8-0
- Updated to release 0.2.8.

* Sat Nov 01 2003 Dag Wieers <dag@wieers.com> - 0.2.7-0
- Updated to release 0.2.7.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 0.2.6-0
- Updated to release 0.2.6.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 0.2.5-0
- Updated to release 0.2.5.

* Wed Sep 10 2003 Dag Wieers <dag@wieers.com> - 0.2.4-0
- Updated to release 0.2.4.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 0.2.3-0
- Updated to release 0.2.3.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 0.2.2-0
- Updated to release 0.2.2.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
