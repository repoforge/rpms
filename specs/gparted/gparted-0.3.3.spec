# $Id$
# Authority: dag

%{?el5:%define _without_hallock 1}
%{?el4:%define _without_hallock 1}
%{?el3:%define _without_hallock 1}

Summary: Gnome Partition Editor
Name: gparted
Version: 0.3.3
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://gparted.sourceforge.net/

Source: http://dl.sf.net/sourceforge/gparted/gparted-%{version}.tar.bz2
Patch0: gparted-dont-lock-hal.patch
Patch1: gparted-devices.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: e2fsprogs-devel
BuildRequires: gettext
BuildRequires: gtkmm24-devel
BuildRequires: parted-devel 
BuildRequires: perl(XML::Parser) 

%{!?_without_hallock:Requires: hal >= 0.5.9}

%description
GParted stands for Gnome Partition Editor and is a graphical frontend to
libparted. Among other features it supports creating, resizing, moving
and copying of partitions. Also several (optional) filesystem tools provide
support for filesystems not included in libparted. These optional packages
will be detected at runtime and don't require a rebuild of GParted

%prep
%setup
%patch0 -p0 -b .hal
%patch1 -p0 -b .devs

%if %{?_without_hallock:1}0
%{__cat} <<EOF >run-gparted
%{_sbindir}/gparted
EOF
%else
%{__cat} <<EOF >run-gparted
#!/bin/bash
%{_bindir}/hal-lock --interface org.freedesktop.Hal.Device.Storage  --exclusive --run %{_sbindir}/gparted
EOF
%endif

%{__cat} <<EOF >gparted.pam
#%PAM-1.0
auth       sufficient   pam_rootok.so
auth       sufficient   pam_timestamp.so
auth       include      system-auth
session	   required     pam_permit.so
session	   optional     pam_xauth.so
session	   optional     pam_timestamp.so
account	   required     pam_permit.so
EOF

%{__cat} <<EOF >gparted.console-apps
USER=root
PROGRAM=%{_bindir}/run-gparted
SESSION=true
EOF

%build
%configure
%{__make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Create a helper script to launch gparted using hal-lock
%{__install} -Dp -m0755 run-gparted %{buildroot}%{_bindir}/run-gparted

### consolehelper stuff
%{__install} -Dp -m0755 %{buildroot}%{_bindir}/gparted %{buildroot}%{_sbindir}/gparted
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/gparted

%{__install} -Dp -m0644 gparted.console-apps %{buildroot}%{_sysconfdir}/security/console.apps/gparted
%{__install} -Dp -m0644 gparted.pam %{buildroot}%{_sysconfdir}/pam.d/gparted

%preun
if [ $1 -ge 0 ]; then
    if [ -a %{_datadir}/hal/fdi/policy/gparted-disable-automount.fdi ]; then
        %{__rm} -rf %{_datadir}/hal/fdi/policy/gparted-disable-automount.fdi
    fi
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%config(noreplace) %{_sysconfdir}/pam.d/gparted
%config(noreplace) %{_sysconfdir}/security/console.apps/gparted
%{_bindir}/gparted
%{_bindir}/run-gparted
%{_datadir}/applications/gparted.desktop
%{_datadir}/pixmaps/gparted.png
%{_sbindir}/gparted

%changelog
* Wed Sep 19 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.3-2
- Only use hal-lock on recent distributions.

* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Added Fedora patches.
- Initial package. (using DAR)
