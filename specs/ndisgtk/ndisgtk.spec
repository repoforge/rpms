# $Id$
# Authority: dag

Summary: Graphical front-end for ndiswrapper
Name: ndisgtk
Version: 0.8
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: https://launchpad.net/ndisgtk/

Source: http://jak-linux.org/projects/ndisgtk/ndisgtk-%{version}.tar.gz
Patch: ndisgtk-0.8-centos.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: intltool, kdebase >= 3.0.0, python-devel, pygtk2-devel
Requires: kdebase >= 3.0.0, python, pygtk2, ndiswrapper

%description
Ndisgtk is a graphical front-end for ndiswrapper, which gives users an easy
way to install the Windows wireless drivers.

%prep
%setup
%patch0 -p0

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
%{_datadir}/icons/ndisgtk.png
%{_datadir}/icons/ndisgtk-error.png
%{_datadir}/ndisgtk/
%{_datadir}/pixmaps/ndisgtk.xpm
%{_sbindir}/ndisgtk

%changelog
* Mon Dec 03 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
