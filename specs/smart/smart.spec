# $Id$
# Authority: dag
# Upstream: Gustavo Niemeyer <niemeyer$conectiva,com>

# ExclusiveDist: fc3 fc4 el4

%{?dist: %{expand: %%define %dist 1}}
%{!?dist: %define fc4 1}

%{?el4:%define _without_channels 1}
%{?el3:%define _without_gui 1}

%define desktop_vendor rpmforge

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_abi %(%{__python} -c 'import sys; print ".".join(sys.version.split(".")[:2])')
%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')

Summary: Next generation package handling tool
Name: smart
Version: 0.37
Release: 11
License: GPL
Group: Applications/System
URL: http://www.smartpm.org/

Source: http://linux-br.conectiva.com.br/~niemeyer/smart/files/smart-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: popt, rpm-devel >= 4.2.1, python-devel, rpm-python
%{!?_without_gui:BuildRequires: gcc-c++, kdelibs-devel, qt-devel, pygtk2-devel >= 2.3.94}
# *** KDE requires autoconf 2.52, 2.53 or 2.54
# *** KDE requires automake 1.6.1 or newer
BuildRequires: autoconf, automake

### python-abi is not defined on older dists (eg. EL3)
#Requires: python-abi = %{python_abi}
Requires: python = %{python_version}

%description
Smart Package Manager is a next generation package handling tool.

%package gui
Summary: Graphical interface to smart
Group: Applications/System
Requires: smart = %{version}
Requires: pygtk2 >= 2.3.94

%description gui
A graphical interface to smart.

%package update
Summary: Allows execution of 'smart update' by normal users (suid)
Group: Applications/System
Requires: smart = %{version}

%description update
Allows execution of 'smart update' by normal users through a
special suid command.

%package -n ksmarttray
Summary: KDE tray program for watching updates with Smart Package Manager
Group: Applications/System
Requires: smart-update = %{version}

%description -n ksmarttray
KDE tray program for watching updates with Smart Package Manager.

%prep
%setup

%{__cat} <<EOF >distro.py
pkgconf.setFlag("multi-version", "kernel")
pkgconf.setFlag("multi-version", "kernel-smp")
EOF

%{__cat} <<EOF >smart-gui.sh
#!/bin/sh
exec %{_bindir}/smart --gui $@
EOF

%{__cat} <<EOF >rpm-db.channel
[rpm-db]
name = RPM Database on this system
type = rpm-sys
EOF

%if %{!?_without_channels:1}0
%{?fc4:name='Fedora Core'; version='4'}
%{?fc3:name='Fedora Core'; version='3'}

%{__cat} <<EOF >os.channel
### URL: http://fedora.redhat.com/
[os]
name = OS packages from Red Hat for $name $version - %{_arch}
baseurl = http://ayo.freshrpms.net/fedora/linux/$version/%{_arch}/core
type = rpm-md
EOF

%{__cat} <<EOF >updates.channel
### URL: http://fedora.redhat.com/
[updates]
name = Updated packages from Red Hat for $name $version - %{_arch}
baseurl = http://ayo.freshrpms.net/fedora/linux/$version/%{_arch}/updates
type = rpm-md
EOF
%endif

%{__cat} <<EOF >smart-gui.console
USER=root
PROGRAM=%{_sbindir}/smart-gui
SESSION=true
EOF

%{__cat} <<EOF >smart-gui.desktop
[Desktop Entry]
Name=Smart Package Manager
Comment=Install packages from various sources
Icon=smart.png
Exec=smart-gui
Type=Application
Terminal=false
StartupNotify=true
Categories=GNOME;Application;SystemSetup;
EOF

%{__cat} <<EOF >smart-gui.pam
#%PAM-1.0
auth       sufficient	/lib/security/pam_rootok.so
auth       sufficient	/lib/security/pam_timestamp.so
auth       required	/lib/security/pam_stack.so service=system-auth
session    required	/lib/security/pam_permit.so
session    optional	/lib/security/pam_timestamp.so
session    optional	/lib/security/pam_xauth.so
account    required	/lib/security/pam_permit.so
EOF

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

%if %{!?_without_gui:1}0
cd contrib/ksmarttray
%{__make} -f admin/Makefile.common
%configure
%{__make}
cd -
%endif

%{__make} -C contrib/smart-update

%ifarch x86_64
cd contrib/rpmhelper/
%{__python} setup.py build
cd -
%endif

%install
%{__rm} -rf %{buildroot}

%{__python} setup.py install --root="%{buildroot}"

%{!?_without_gui:%{__make} install -C contrib/ksmarttray DESTDIR="%{buildroot}"}

%ifarch x86_64
cd contrib/rpmhelper/
%{__python} setup.py install --root="%{buildroot}"
cd -
%endif

%find_lang %{name}

%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/smart-gui

%{__install} -Dp -m0644 distro.py %{buildroot}%{_prefix}/lib/smart/distro.py
%{__install} -Dp -m4755 contrib/smart-update/smart-update %{buildroot}%{_bindir}/smart-update
#%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{python_dir}/smart/plugins/channelsync.py

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/smart/channels/
%{__cp} -apv *.channel %{buildroot}%{_sysconfdir}/smart/channels/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/smart/

%if %{!?_without_gui:1}0
%{__install} -Dp -m0755 smart-gui.sh %{buildroot}%{_sbindir}/smart-gui
%{__install} -Dp -m0644 smart-gui.console %{buildroot}%{_sysconfdir}/security/console.apps/smart-gui
%{__install} -Dp -m0644 smart-gui.pam %{buildroot}%{_sysconfdir}/pam.d/smart-gui
%{__install} -Dp -m0644 smart/interfaces/images/smart.png %{buildroot}%{_datadir}/pixmaps/smart.png

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 smart-gui.desktop %{buildroot}%{_datadir}/gnome/apps/System/smart.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--dir %{buildroot}%{_datadir}/applications \
		--add-category X-Red-Hat-Base              \
		smart-gui.desktop
%endif
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc HACKING IDEAS LICENSE README TODO doc/*
%config %{_prefix}/lib/smart/distro.py
%dir %{_prefix}/lib/smart/
%config(noreplace) %{_sysconfdir}/smart/channels/
%{_bindir}/smart
%{python_sitearch}/smart/
%exclude %{python_sitearch}/smart/interfaces/gtk/
%{_localstatedir}/lib/smart/
%ifarch x86_64
%{python_sitearch}/rpmhelper.so
%endif

%if %{!?_without_gui:1}0
%files gui
%defattr(-, root, root, 0755)
%{_sysconfdir}/pam.d/smart-gui
%{_bindir}/smart-gui
%{_sbindir}/smart-gui
%{_sysconfdir}/security/console.apps/smart-gui
%dir %{python_sitearch}/smart/
%dir %{python_sitearch}/smart/interfaces/
%{python_sitearch}/smart/interfaces/gtk/
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-smart-gui.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/System/smart-gui.desktop}
%{_datadir}/pixmaps/smart.png
%endif

%files update
%defattr(4755, root, root, 0755)
%{_bindir}/smart-update

%if %{!?_without_gui:1}0
%files -n ksmarttray
%defattr(-, root, root, 0755)
%{_bindir}/ksmarttray
%{_datadir}/apps/ksmarttray/
%endif

%changelog
* Fri Aug 19 2005 Dag Wieers <dag@wieers.com> - 0.37-1
- Updated to release 0.37.

* Thu Jul 14 2005 Dag Wieers <dag@wieers.com> - 0.36-1
- Updated to release 0.36.

* Tue Jun 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-2
- Added tags for fc4.

* Mon May 30 2005 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 0.30.2-1
- Updated to release 0.30.2.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 0.30-1
- Removed kernel-doc from distro.py. (Ralf Ertzinger)
- Updated to release 0.30.

* Wed Mar 09 2005 Dag Wieers <dag@wieers.com> - 0.29.2-2
- Included rpmhelper patch for x86_64 problem. (RHbz 146477)

* Mon Mar 07 2005 Dag Wieers <dag@wieers.com> - 0.29.2-1
- Updated to release 0.29.2.

* Fri Mar 04 2005 Dag Wieers <dag@wieers.com> - 0.29.1-1
- Updated to release 0.29.1.

* Wed Feb 16 2005 Dag Wieers <dag@wieers.com> - 0.28-3
- Correct the location for distro.py on x86_64. (Edward Rudd)

* Thu Dec 09 2004 Dag Wieers <dag@wieers.com> - 0.28-2
- Disabled a few repositories to speed up Smart by default.
- Fix for x86_64. (Gustavo Niemeyer)

* Thu Dec 09 2004 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Tue Dec 07 2004 Dag Wieers <dag@wieers.com> - 0.27.1-3
- Added jpackage-generic channel. (Thomas Moschny)

* Sun Dec 05 2004 Dag Wieers <dag@wieers.com> - 0.27.1-2
- Added smart-gui console-helper so users can start smart.

* Sat Dec 04 2004 Dag Wieers <dag@wieers.com> - 0.27.1-1
- Initial package. (using DAR)
