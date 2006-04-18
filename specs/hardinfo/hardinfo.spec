# $Id$
# Authority: dag
# Upstream: Leandro Pereira <leandro$linuxmag,com,br>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Displays information about your hardware and operating system
Name: hardinfo
Version: 0.4
Release: 1.2
License: GPL
Group: Applications/System
URL: http://alpha.linuxmag.com.br/~leandro/hardinfo/

Source: http://download.berlios.de/hardinfo/hardinfo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.6
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: pciutils

%description
HardInfo is a small application that displays information about your
hardware and operating system. Currently it knows about PCI, ISA PnP,
USB, IDE, SCSI, Serial and parallel port devices.

%prep
%setup

### FIXME: Use standard autotool paths.
#%{__perl} -pi.orig -e '
#		s|/usr/bin/|\$(bindir)/|;
#		s|/usr/share/|\$(datadir)/|;
#	' Makefile.in

%{__cat} <<EOF >hardinfo.desktop
[Desktop Entry]
Name=Hardware Information
Comment=Display information about your hardware and operating system
Icon=gnome-settings.png
Exec=hardinfo
Terminal=false
Type=Application
Categories=Application;Utility;System;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Create directory as make install doesn't do that.
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 hardinfo.desktop %{buildroot}%{_datadir}/gnome/apps/System/hardinfo.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog
%{_bindir}/*
%{_datadir}/hardinfo/
%if %{?_without_freedesktop:1}0
	%{_datadir}/gnome/apps/System/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1.2
- Rebuild for Fedora Core 5.

* Thu Feb 02 2006 Dag Wieers <dag@wieers.com> - 0.4-0
- Updated to release 0.4.

* Fri Oct 31 2003 Dag Wieers <dag@wieers.com> - 0.3.6-0
- Updated to release 0.3.6.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.3.5-0
- Updated to release 0.3.5.

* Mon Jun 23 2003 Dag Wieers <dag@wieers.com> - 0.3.4-0
- Updated to release 0.3.4.

* Sat Jun 21 2003 Dag Wieers <dag@wieers.com> - 0.3.3-0
- Initial package. (using DAR)
