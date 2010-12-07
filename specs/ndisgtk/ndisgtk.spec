# $Id$
# Authority: dag

Summary: Graphical front-end for ndiswrapper
Name: ndisgtk
Version: 0.8.5
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: https://launchpad.net/ndisgtk/

Source: http://jak-linux.org/projects/ndisgtk/ndisgtk-%{version}.tar.gz
Patch0: ndisgtk-0.8-centos.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: intltool
BuildRequires: pygtk2-devel
BuildRequires: python-devel
Requires: ndiswrapper-utils
Requires: pygtk2
Requires: python

%description
Ndisgtk is a graphical front-end for ndiswrapper, which gives users an easy
way to install the Windows wireless drivers.

%prep
%setup
#patch0 -p0

%{__cat} <<EOF >ndisgtk.desktop.in
[Desktop Entry]
_Name=Windows Wireless Drivers
_Comment=Install windows wireless drivers using ndiswrapper
Exec=ndisgtk
Icon=ndisgtk.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;SystemSetup;
EOF

%{__cat} <<EOF >ndisgtk.console
USER=root
PROGRAM=%{_sbindir}/ndisgtk
SESSION=true
EOF

%{__cat} <<EOF >ndisgtk.pam
#%PAM-1.0
auth       sufficient   /lib/security/pam_rootok.so
auth       sufficient   /lib/security/pam_timestamp.so
auth       required     /lib/security/pam_stack.so service=system-auth
session    required     /lib/security/pam_permit.so
session    optional     /lib/security/pam_timestamp.so
session    optional     /lib/security/pam_xauth.so
account    required     /lib/security/pam_permit.so
EOF

%build
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -dp -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/ndisgtk

%{__install} -Dp -m0644 ndisgtk.8 %{buildroot}%{_mandir}/man8/ndisgtk.8
%{__install} -Dp -m0644 ndisgtk.console %{buildroot}%{_sysconfdir}/security/console.apps/ndisgtk
%{__install} -Dp -m0644 ndisgtk.pam %{buildroot}%{_sysconfdir}/pam.d/ndisgtk

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/applications/ndisgtk-kde.desktop

%post
update-desktop-database -q || :
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &> /dev/null || :

%postun
update-desktop-database -q || :
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc NEWS
%doc %{_mandir}/man8/ndisgtk.8*
%config %{_sysconfdir}/pam.d/ndisgtk
%config %{_sysconfdir}/security/console.apps/ndisgtk
%{_bindir}/ndisgtk
%{_datadir}/applications/ndisgtk.desktop
%{_datadir}/icons/hicolor/48x48/apps/ndisgtk-error.png
%{_datadir}/icons/hicolor/48x48/apps/ndisgtk.png
%{_datadir}/ndisgtk/
%{_datadir}/pixmaps/ndisgtk.xpm
%{_sbindir}/ndisgtk

%changelog
* Sat Dec 04 2010 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Mon Dec 03 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
