# $Id$
# Authority: dag
# Upstream: Gustavo Niemeyer <niemeyer$conectiva,com>

%{?el3:%define _without_gui 1}

# ExclusiveDist: fc3 el4

### Testing for EL3
##Tag: test

%{?dist: %{expand: %%define %dist 1}}
%{!?dist: %define fc3 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_abi %(%{__python} -c 'import sys; print ".".join(sys.version.split(".")[:2])')
%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')

Summary: Next generation package handling tool
Name: smart
Version: 0.29.2
Release: 2
License: GPL
Group: Applications/System
URL: http://www.smartpm.org/

Source: http://linux-br.conectiva.com.br/~niemeyer/smart/files/smart-%{version}.tar.bz2
Patch0: smart-0.29.2-x86_64-rpmhelper.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: popt, rpm-devel >= 4.2.1, python-devel
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
%ifarch x86_64
%patch -p0 -b .rpmhelper
%endif

%{__perl} -pi.orig -e 's|(get_python_lib\()\)|${1}1)|g' setup.py
%{__perl} -pi.orig -e 's|int32_t lkey|long lkey|g' python/rpmts-py.c

%{?fc3:name="Fedora Core"; version="3"; path="fedora"}
%{?fc2:name="Fedora Core"; version="2"; path="fedora"}
%{?fc1:name="Fedora Core"; version="1"; path="fedora"}

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
priority = 10
EOF

%{__cat} <<EOF >os.channel
### URL: http://fedora.redhat.com/
[os]
name = OS packages from Red Hat for $name $version (%{_arch})
baseurl = http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/core
type = rpm-md
priority = 10
EOF

%{__cat} <<EOF >updates.channel
### URL: http://fedora.redhat.com/
[updates]
name = Updated packages from Red Hat for $name $version (%{_arch})
baseurl = http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/updates
type = rpm-md
priority = 10
EOF

%{__cat} <<EOF >dag.channel
### URL: http://dag.wieers.com/apt/
[dag]
name = RPMforge.net: Various packages from Dag RPM Repository for $name $version (%{_arch})
baseurl = http://apt.sw.be/$path/$version/en/%{_arch}/dag
type = rpm-md
priority = 10
EOF

%{__cat} <<EOF >freshrpms.channel
### URL: http://freshrpms.net/
[freshrpms]
name = RPMforge.net: Various packages from FreshRPMS.net for $name $version (%{_arch})
baseurl = http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/freshrpms
type = rpm-md
priority = 10
EOF

%{__cat} <<EOF >planetccrma.channel
### URL: http://ccrma.stanford.edu/planetccrma/software/
[planetcrrma]
name = RPMforge.net: Various packages from Planet CCRMA for $name $version (%{_arch})
baseurl = http://ccrma.stanford.edu/planetccrma/apt/$path/$version/%{_arch}
components = planetccrma planetcore
type = apt-rpm
priority = 10
disabled = true
EOF

%{__cat} <<EOF >dries.channel
### URL: http://dries.studentenweb.org/ayo/
[dries]
name = RPMforge.net: Various packages from Dries RPM Repository for $name $version (%{_arch})
baseurl = http://apt.sw.be/dries/$path/fc$version/%{_arch}/dries/RPMS
type = rpm-md
priority = 10
EOF

%{__cat} <<EOF >newrpms.channel
### URL: http://newrpms.sunsite.dk/
[newrpms]
name = Various packages from NewRPMS for $name $version (%{_arch})
baseurl = http://newrpms.sunsite.dk/apt/redhat/en/%{_arch}/fc$version
type = rpm-md
priority = 0
EOF

%{__cat} <<EOF >atrpms.channel
### URL: http://atrpms.net/
[atrpms]
name = Various packages from ATrpms for $name $version (%{_arch})
baseurl = http://apt.physik.fu-berlin.de/$path/$version/en/%{_arch}/at-testing
type = rpm-md
priority = -10
EOF

%{__cat} <<EOF >jpackage.channel
### URL: http://jpackage.org/
[jpackage]
name = Java packages from JPackage.org for $name $version (%{_arch})
baseurl = http://mirrors.sunsite.dk/jpackage/1.6/$path-$version/free
type = rpm-md
priority = 0
disabled = true
EOF

%{__cat} <<EOF >jpackage-generic.channel
### URL: http://jpackage.org/
[jpackage-generic]
name = Java packages from JPackage.org for all distributions
baseurl = http://mirrors.sunsite.dk/jpackage/1.6/generic/free
type = rpm-md
priority = 0
disabled = true
EOF

%{__cat} <<EOF >biorpms.channel
### URL: http://apt.bea.ki.se/
[biorpms]
name = Bioinformatic packages from BIOrpms for $name $version (%{_arch})
baseurl = http://apt.bea.ki.se/biorpms/$path/linux/$version/%{_arch}/biorpms
type = rpm-md
priority = 0
disabled = true
EOF

%{__cat} <<EOF >kde-redhat.channel
### URL: http://kde-redhat.sourceforge.net/
[kde-redhat]
name = KDE packages from the kde-redhat project for $name $version (%{_arch})
baseurl = http://apt.kde-redhat.org/apt/kde-redhat/$version/stable
type = rpm-md
priority = -5
disabled = true
EOF

%{__cat} <<EOF >kde-redhat-all.channel
### URL: http://kde-redhat.sourceforge.net/
[kde-redhat-all]
name = KDE packages from the kde-redhat project for all distributions
baseurl = http://apt.kde-redhat.org/apt/kde-redhat/all/stable
type = rpm-md
priority = -5
disabled = true
EOF

%{__cat} <<EOF >nrpms.channel
### URL: http://www.nrpms.net/
[nrpms]
name = Various packages from Nrpms for $name $version (%{_arch})
baseurl = http://yum.nrpms.net/$path-$version-%{_arch}/production
type = rpm-md
priority = -10
disabled = true
EOF

%{__cat} <<EOF >mozilla-seamonkey.channel
### URL: http://mozilla.org/
[mozilla-seamonkey]
name = Mozilla packages from Mozilla SeaMonkey for $name $version (%{_arch})
baseurl = http://ftp.mozilla.org/pub/mozilla.org/mozilla/yum/SeaMonkey/releases/current/redhat/$version
type = rpm-md
priority = -10
disabled = true
EOF

%{__cat} <<EOF >livna.channel
### URL: http://rpm.livna.org/
[livna]
name = Incompatible packages from Livna.org for $name $version (%{_arch})
baseurl = http://rpm.livna.org/$path/$version/%{_arch}/RPMS.stable
type = rpm-md 
priority = -100
disabled = true
EOF

%{__cat} <<EOF >fedora.us.channel
### URL: http://fedora.us/
[fedora.us]
name = Incompatible packages from Fedora.us for $name $version (%{_arch})
baseurl = http://download.fedora.us/fedora/$path/$version/%{_arch}/RPMS.extras
type = rpm-md
priority = -100
disabled = true
EOF

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
cd contrib/rpmhelper
%{__python} setup.py build
cd -
%endif

%install
%{__rm} -rf %{buildroot}

%{__python} setup.py install --root="%{buildroot}"

%{!?_without_gui:%{__make} install -C contrib/ksmarttray DESTDIR="%{buildroot}"}

%ifarch x86_64
cd contrib/rpmhelper
%{__python} setup.py install --root="%{buildroot}"
cd -
%endif

%find_lang %{name}

%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/smart-gui

%{__install} -Dp -m0644 distro.py %{buildroot}%{_prefix}/lib/smart/distro.py
%{__install} -Dp -m4755 contrib/smart-update/smart-update %{buildroot}%{_bindir}/smart-update
#%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{python_dir}/smart/plugins/channelsync.py

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/smart/channels/
%{__cp} -av *.channel %{buildroot}%{_sysconfdir}/smart/channels/

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
* Mon Mar 14 2005 Dag Wieers <dag@wieers.com> - 0.29.2-3
- Removed kernel-doc from distro.py. (Ralf Ertzinger)

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
