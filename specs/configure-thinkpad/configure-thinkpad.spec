# Authority: dag

Summary: Graphical ThinkPad configuration utility.
Name: configure-thinkpad
Version: 0.1
Release: 1
License: GPL
Group: System Environment/Base
URL: http://tpctl.sourceforge.net/configure-thinkpad.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.sf.net/tpctl/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libgnomeui-devel >= 2.0, gettext, desktop-file-utils
Requires: tpctl, usermode >= 1.36

%description
configure-thinkpad is a ThinkPad configuration utility.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=ThinkPad
Comment=Edit your ThinkPad configuration
Icon=configure-thinkpad/gnome-laptop.png
Exec=configure-thinkpad
Type=Application
Terminal=false
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
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/pam.d/ \
			%{buildroot}%{_sysconfdir}/security/console.apps/ \
			%{buildroot}%{_sbindir}
%{__install} -m0644 configure-thinkpad.pam %{buildroot}%{_sysconfdir}/pam.d/configure-thinkpad
%{__install} -m0644 configure-thinkpad.consolehelper %{buildroot}%{_sysconfdir}/security/console.apps/configure-thinkpad
%{__mv} -f %{buildroot}%{_bindir}/configure-thinkpad %{buildroot}%{_sbindir}
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/configure-thinkpad

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%config %{_sysconfdir}/pam.d/*
%config %{_sysconfdir}/security/console.apps/*
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/configure-thinkpad/

%changelog
* Sat Jan 03 2004 Dag Wieers <dag@wieers.com> - 0.1-1
- Added consolehelper support.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
