# $Id$

# Authority: dag

# Upstream: Leandro Pereira <leandro@linuxmag.com.br>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Displays information about your hardware and operating system
Name: hardinfo
Version: 0.3.6
Release: 0
License: GPL
Group: Applications/System
URL: http://alpha.linuxmag.com.br/~leandro/hardinfo/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://alpha.linuxmag.com.br/~leandro/hardinfo/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2-devel >= 2.0
Requires: pciutils

%description
HardInfo is a small application that displays information about your
hardware and operating system. Currently it knows about PCI, ISA PnP,
USB, IDE, SCSI, Serial and parallel port devices.

%prep
%setup

### FIXME: Use standard autotool paths.
%{__perl} -pi.orig -e '
		s|/usr/bin/|\$(bindir)/|;
		s|/usr/share/|\$(datadir)/|;
	' Makefile.in

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Hardware Information
Comment=%{summary}
Icon=gnome-settings.png
Exec=hardinfo
Terminal=false
Type=Application
Categories=Application;Utility;System;
EOF

%build
#configure
./configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Create directory as make install doesn't do that.
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/System/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/System/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
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
%if %{dfi}
	%{_datadir}/gnome/apps/System/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Fri Oct 31 2003 Dag Wieers <dag@wieers.com> - 0.3.6-0
- Updated to release 0.3.6.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.3.5-0
- Updated to release 0.3.5.

* Mon Jun 23 2003 Dag Wieers <dag@wieers.com> - 0.3.4-0
- Updated to release 0.3.4.

* Sat Jun 21 2003 Dag Wieers <dag@wieers.com> - 0.3.3-0
- Initial package. (using DAR)
