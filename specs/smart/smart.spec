# $Id$
# Authority: dag
# Upstream: Gustavo Niemeyer <niemeyer@conectiva.com>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

### FIXME: Can't use python_dir because smart install does not seem to obey/follow it fallback to python_version.
%define python_dir %(python -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_version %(python2 -c 'import sys; print sys.version[:3]')

Summary: Next generation package handling tool
Name: smart
Version: 0.27.1
Release: 1
License: GPL
Group: Applications/System
URL: http://www.smartpm.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://linux-br.conectiva.com.br/~niemeyer/smart/files/smart-%{version}.tar.bz2
#Source: http://smart.conectiva.com.br/files/smart-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: popt, rpm-devel >= 4.2.1, python-devel
BuildRequires: kdelibs-devel, qt-devel
Requires: python, pygtk2 >= 2.3.94

%description
Smart Package Manager is a next generation package handling tool.

%package update
Summary: Allows execution of 'smart update' by normal users (suid)
Group: Applications/System
Requires: smart = %{version}-%{release}

%description update
Allows execution of 'smart update' by normal users through a
special suid command.

%package -n ksmarttray
Summary: KDE tray program for watching updates with Smart Package Manager
Group: Applications/System
Requires: smart-update = %{version}-%{release}

%description -n ksmarttray
KDE tray program for watching updates with Smart Package Manager.

%description -n ksmarttray
Programa tray do KDE para verificar atualizações com o Smart Package Manager.

%prep
%setup

%{?fc3:name="Fedora Core"; version="3"; path="fedora"}
%{?fc2:name="Fedora Core"; version="2"; path="fedora"}
%{?fc1:name="Fedora Core"; version="1"; path="fedora"}

%{__cat} <<EOF >distro.py
sysconf.set(("channels", "rpm-db"), {
	"alias": "rpm-db",
	"type": "rpm-sys",
	"name": "RPM Database",
	"priority": 10,
})

sysconf.set(("channels", "os"), {
	"alias": "%{dist}-os",
	"type": "rpm-md",
	"name": "$name $version",
	"baseurl": "http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/core/",
	"priority": 10,
})

sysconf.set(("channels", "updates"), {
	"alias": "%{dist}-updates",
	"type": "rpm-md",
	"name": "$name $version Updates",
	"baseurl": "http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/updates/",
	"priority": 10,
})

sysconf.set(("channels", "mirrors"), {
	"alias": "%{dist}-mirrors",
	"type": "up2date-mirrors",
	"name": "$name $version (Mirrors Channel)",
	"url": "http://fedora.redhat.com/download/up2date-mirrors/fedora-core-$version",
})

sysconf.set(("channels", "mirrors-updates"), {
	"alias": "%{dist}-mirrors-updates",
	"type": "up2date-mirrors",
	"name": "$name $version Updates (Mirrors Channel)",
	"url": "http://fedora.redhat.com/download/up2date-mirrors/updates-released-fc$version",
})

sysconf.set(("channels", "repo-dag"), {
	"alias": "repo-%{dist}-dag",
	"type": "rpm-md",
	"name": "Various packages from RPMforge.net (dag) for $name $version",
	"baseurl": "http://apt.sw.be/$path/$version/en/%{_arch}/dag",
	"priority": 10,
})

sysconf.set(("channels", "repo-freshrpms"), {
	"alias": "repo-%{dist}-freshrpms",
	"type": "rpm-md",
	"name": "Varios packages from RPMforge.net (freshrpms) for $name $version",
	"baseurl": "http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/freshrpms",
	"priority": 10,
})

sysconf.set(("channels", "repo-dries"), {
	"alias": "repo-%{dist}-dries",
	"type": "rpm-md",
	"name": "Various packages from RPMforge.net (dries) for $name $version",
	"baseurl": "http://apt.sw.be/dries/$path/fc$version/%{_arch}/dries/RPMS",
	"priority": 10,
})

sysconf.set(("channels", "repo-jpackage"), {
	"alias": "repo-%{dist}-jpackage",
	"type": "rpm-md",
	"name": "Java packages from JPackage.org for $name $version",
	"baseurl": "http://mirrors.sunsite.dk/jpackage/1.6/fedora-3/free/",
	"priority": 0,
	"disabled": "true"
})

sysconf.set(("channels", "repo-newrpms"), {
	"alias": "repo-%{dist}-newrpms",
	"type": "rpm-md",
	"name": "Various packages from NewRPMS for $name $version",
	"baseurl": "http://newrpms.sunsite.dk/apt/redhat/en/%{_arch}/fc$version",
	"priority": -5,
})

sysconf.set(("channels", "repo-kde-redhat"), {
	"alias": "repo-%{dist}-kde-redhat",
	"type": "rpm-md",
	"name": "KDE packages from the kde-redhat project for $name $version",
	"baseurl": "http://apt.kde-redhat.org/apt/kde-redhat/$version/stable",
	"priority": -5,
	"disabled": "true"
})

sysconf.set(("channels", "repo-kde-redhat-all"), {
	"alias": "repo-%{dist}-kde-redhat-all",
	"type": "rpm-md",
	"name": "KDE (nodist) packages from the kde-redhat project for $name $version",
	"baseurl": "http://apt.kde-redhat.org/apt/kde-redhat/all/stable",
	"priority": -5,
	"disabled": "true"
})

sysconf.set(("channels", "repo-atrpms"), {
	"alias": "repo-%{dist}-atrpms",
	"type": "rpm-md",
	"name": "Various packages from ATrpms for $name $version",
	"baseurl": "http://apt.physik.fu-berlin.de/$path/$version/en/%{_arch}/at-testing",
	"priority": -10,
	"disabled": "true",
})

for type in ["", "doc", "smp" ]:
	if type:
		kernel = "kernel-%s" % type
	else:
		kernel = "kernel"
	pkgconf.setFlag("multi-version", kernel)
EOF

%{__cat} <<EOF >smart.console
USER=root
PROGRAM=%{_sbindir}/smart
SESSION=true
EOF

%{__cat} <<EOF >smart.desktop
[Desktop Entry]
Name=Smart Package Manager
Comment=Install packages from various sources
Icon=smart.png
Exec=smart --gui
Type=Application
Terminal=false
StartupNotify=true
Categories=GNOME;Application;SystemSetup;
EOF

%{__cat} <<EOF >smart.pam
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
env CFLAGS="%{optflags}" python setup.py build

pushd contrib/ksmarttray
%{__make} -f admin/Makefile.common
%configure
%{__make}
popd

%{__make} -C contrib/smart-update

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--root="%{buildroot}"

%{__make} install -C "contrib/ksmarttray" \
	DESTDIR="%{buildroot}"

%find_lang %{name}

%{__install} -D -m0755 %{buildroot}%{_bindir}/smart %{buildroot}%{_sbindir}/smart
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/smart

%{__install} -D -m0644 distro.py %{buildroot}%{_libdir}/smart/distro.py
#%{__install} -D -m0755 %{SOURCE1} %{buildroot}%{python_dir}/smart/backends/rpm/rpmmodule.so
%{__install} -D -m4755 contrib/smart-update/smart-update %{buildroot}%{_bindir}/smart-update
%{__install} -D -m0644 smart.console %{buildroot}%{_sysconfdir}/security/console.apps/smart
%{__install} -D -m0644 smart.pam %{buildroot}%{_sysconfdir}/pam.d/smart
%{__install} -D -m0644 smart/interfaces/images/smart.png %{buildroot}%{_datadir}/pixmaps/smart.png

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 smart.desktop %{buildroot}%{_datadir}/gnome/apps/System/smart.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--dir %{buildroot}%{_datadir}/applications \
		--add-category X-Red-Hat-Base              \
		smart.desktop
%endif


%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc HACKING IDEAS LICENSE README TODO
%config %{_libdir}/smart/distro.py
%dir %{_libdir}/smart/
%{_sysconfdir}/security/console.apps/smart
%{_sysconfdir}/pam.d/smart
%{_bindir}/smart
%{_sbindir}/smart
%{python_dir}/smart/
%{_libdir}/python%{python_version}/site-packages/smart/
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-smart.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/System/smart.desktop}
%{_datadir}/pixmaps/smart.png

%files update
%defattr(4755, root, root, 0755)
%{_bindir}/smart-update

%files -n ksmarttray
%defattr(-, root, root, 0755)
%{_bindir}/ksmarttray
%{_datadir}/apps/ksmarttray/

%changelog
* Sat Dec 04 2004 Dag Wieers <dag@wieers.com> - 0.27.1-1
- Initial package. (using DAR)
