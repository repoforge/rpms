# $Id$
# Authority: dag
# Upstream: Roland Stigge <stigge$antcom,de>
# Upstream: <gtick-devel$nongnu,org>

Summary: Metronome application
Name: gtick
Version: 0.3.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.antcom.de/gtick/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.antcom.de/gtick/download/gtick-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf >= 2.57

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
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO doc/NOTES
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop

%changelog
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
