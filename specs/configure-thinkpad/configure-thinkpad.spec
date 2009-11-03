# $Id$
# Authority: dag
# Upstream: <wang$ai,mit,edu>

Summary: Graphical ThinkPad configuration utility
Name: configure-thinkpad
Version: 0.9
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://tpctl.sourceforge.net/configure-thinkpad.html

Source: http://dl.sf.net/tpctl/configure-thinkpad-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.0, gettext, desktop-file-utils
Requires: tpctl, usermode >= 1.36

%description
configure-thinkpad is a ThinkPad configuration utility.

%prep
%setup

%{__cat} <<EOF >configure-thinkpad.desktop
[Desktop Entry]
Name=ThinkPad
Comment=Edit your ThinkPad configuration
Icon=configure-thinkpad.png
Exec=configure-thinkpad
Type=Application
Terminal=false
Encoding=UTF-8
StartupNotify=true
Categories=GNOME;Application;Settings;HardwareSettings;System;SystemSetup;
EOF

%{__cat} <<EOF >configure-thinkpad.consolehelper
USER=root
PROGRAM=%{_sbindir}/configure-thinkpad
SESSION=true
EOF

%{__cat} <<EOF >configure-thinkpad.pam
#%PAM-1.0
auth       sufficient   pam_rootok.so
auth       sufficient   pam_timestamp.so
auth       required     pam_stack.so service=system-auth
session    required     pam_permit.so
session    optional     pam_xauth.so
session    optional     pam_timestamp.so
account    required     pam_permit.so
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0644 pixmaps/gnome-laptop.png %{buildroot}%{_datadir}/pixmaps/configure-thinkpad.png
%{__install} -Dp -m0644 configure-thinkpad.pam %{buildroot}%{_sysconfdir}/pam.d/configure-thinkpad
%{__install} -Dp -m0644 configure-thinkpad.consolehelper %{buildroot}%{_sysconfdir}/security/console.apps/configure-thinkpad

%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__mv} -f %{buildroot}%{_bindir}/configure-thinkpad %{buildroot}%{_sbindir}
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/configure-thinkpad

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/configure-thinkpad.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%config %{_sysconfdir}/pam.d/configure-thinkpad
%config %{_sysconfdir}/security/console.apps/configure-thinkpad
%{_bindir}/configure-thinkpad
%{_sbindir}/configure-thinkpad
%{_datadir}/applications/gnome-configure-thinkpad.desktop
%{_datadir}/pixmaps/configure-thinkpad.png
%{_datadir}/pixmaps/configure-thinkpad/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-1.2
- Rebuild for Fedora Core 5.

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Tue Oct 05 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Sun Jul 25 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Mon Jun 07 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Added improved desktop file.
- Updated to release 0.2.

* Sat Jan 03 2004 Dag Wieers <dag@wieers.com> - 0.1-1
- Added consolehelper support.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
