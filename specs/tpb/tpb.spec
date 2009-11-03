# $Id$
# Authority: dag
# Upstream: Markus Braun <markus,braun$krawel,de>


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Utility to enable the IBM ThinkPad(tm) special keys
Name: tpb
Version: 0.6.3
Release: 3.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/tpb/

Source: http://savannah.nongnu.org/download/tpb/tpb-%{version}.tar.gz
#Source1: tpbrc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, xosd-devel >= 2.0
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
This program enables the IBM Thinkpad(tm) special keys. It is possible to bind
a program to the ThinkPad button. It has a on-screen display (OSD) to show
volume, mute and brightness of the LCD.

%prep
%setup

%{__cat} <<EOF >tpb.xinit
#!/bin/sh
%{_bindir}/tpb -d
EOF

%{__perl} -pi.orig -e '
		s|^#(OSDCOLOR)(.+)|#$1$2\n$1\tGreen|;
		s|^#(OSDFONT)(.+)$|#$1$2\n$1 -adobe-helvetica-bold-r-*-*-*-240-*-*-*-*-*-*|;
		s|^#(OSDALIGN)(.+)|#$1$2\n$1\tCenter|;
		s|^#(OSDVERTICAL)(.+)|#$1$2\n$1\t60|;
	' doc/tpbrc

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}
%{__install} -Dp -m0755 doc/tpbrc %{buildroot}%{_sysconfdir}/tpbrc
%{__install} -Dp -m0755 tpb.xinit %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/tpb.sh

%{__install} -d -m0755 %{buildroot}/dev/
touch %{buildroot}/dev/nvram
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/udev/devices/
touch %{buildroot}%{_sysconfdir}/udev/devices/nvram

%post
if [ -e /dev/.devfsd ]; then
	if [ -x /usr/sbin/update-devfsd ]; then
		/usr/sbin/update-devfsd
	fi
else
	if [ ! -e /dev/nvram ]; then
		/dev/MAKEDEV nvram
		chmod 0644 /dev/nvram
		cp -avx /dev/nvram %{_sysconfdir}/udev/devices/nvram
	fi
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING CREDITS doc/callback_example.sh doc/nvram.txt doc/tpbrc README TODO
%doc %{_mandir}/man1/tpb.1*
%config(noreplace) %{_sysconfdir}/tpbrc
%config(noreplace) %{_sysconfdir}/X11/xinit/xinitrc.d/tpb.sh
%{_bindir}/tpb

%defattr(0644, root, root, 0755)
%ghost /dev/nvram
%ghost %{_sysconfdir}/udev/devices/nvram

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.3-3.2
- Rebuild for Fedora Core 5.

* Sun Mar 06 2005 Manfred Paul <manfred.paul@de.ibm.com> - 0.6.3-3
- Repair udev support.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.6.3-2
- Added udev support for FC3+. (Matthew Saltzman)

* Tue Aug 24 2004 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Fri Jun 11 2004 Dag Wieers <dag@wieers.com> - 0.6.2-2
- Fixed naming of tpb xinit file to tpb.sh for FC2. (Patrick C. F. Ernzer)

* Wed May 19 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Tue Jan 20 2004 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Don't replace config-files.

* Tue Aug 12 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Thu Apr 10 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Sun Apr 06 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Updated to release 0.5.0.

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 0.4.2-0
- Initial package. (using DAR)
- Included tpb.xinit. (Tim Verhoeven)
