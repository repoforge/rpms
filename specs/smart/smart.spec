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
	"name": "RPM Database on this system",
	"type": "rpm-sys",
	"priority": 10,
})

sysconf.set(("channels", "os"), {
	"name": "OS packages from Red Hat for $name $version",
	"baseurl": "http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/core/",
	"type": "rpm-md",
	"priority": 10,
})

sysconf.set(("channels", "updates"), {
	"name": "Updated packages from Red Hat for $name $version",
	"baseurl": "http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/updates/",
	"type": "rpm-md",
	"priority": 10,
})

sysconf.set(("channels", "repo-dag"), {
	"name": "Various packages from RPMforge.net (dag) for $name $version",
	"baseurl": "http://apt.sw.be/$path/$version/en/%{_arch}/dag",
	"type": "rpm-md",
	"priority": 10,
})

sysconf.set(("channels", "repo-freshrpms"), {
	"name": "Various packages from RPMforge.net (freshrpms) for $name $version",
	"baseurl": "http://ayo.freshrpms.net/$path/linux/$version/%{_arch}/freshrpms",
	"type": "rpm-md",
	"priority": 10,
})

sysconf.set(("channels", "repo-dries"), {
	"name": "Various packages from RPMforge.net (dries) for $name $version",
	"baseurl": "http://apt.sw.be/dries/$path/fc$version/%{_arch}/dries/RPMS",
	"type": "rpm-md",
	"priority": 10,
})

sysconf.set(("channels", "repo-planetccrma"), {
	"name": "Various packages from RPMforge.net (planetccrma) for $name $version",
	"baseurl": "rpm http://ccrma.stanford.edu/planetccrma/apt/$path/$version/%{_arch}",
	"components": "planetccrma planetcore",
	"type": "apt-rpm",
	"priority": 10,
	"disabled": "true",
})

sysconf.set(("channels", "repo-jpackage"), {
	"name": "Java packages from JPackage.org for $name $version",
	"baseurl": "http://mirrors.sunsite.dk/jpackage/1.6/$path-$version/free/",
	"type": "rpm-md",
	"priority": 0,
})

sysconf.set(("channels", "repo-newrpms"), {
	"name": "Various packages from NewRPMS for $name $version",
	"baseurl": "http://newrpms.sunsite.dk/apt/redhat/en/%{_arch}/fc$version",
	"type": "rpm-md",
	"priority": 0,
})

sysconf.set(("channels", "repo-biorpms"), {
	"name": "Bioinformatic packages from BIOrpms for $name $version",
	"baseurl": "http://apt.bea.ki.se/biorpms/$path/linux/$version/%{_arch}/biorpms",
	"type": "rpm-md",
	"priority": 0,
})

sysconf.set(("channels", "repo-kde-redhat"), {
	"name": "KDE packages from the kde-redhat project for $name $version",
	"baseurl": "http://apt.kde-redhat.org/apt/kde-redhat/$version/stable",
	"type": "rpm-md",
	"priority": -5,
})

sysconf.set(("channels", "repo-kde-redhat-all"), {
	"name": "KDE (nodist) packages from the kde-redhat project for $name $version",
	"baseurl": "http://apt.kde-redhat.org/apt/kde-redhat/all/stable",
	"type": "rpm-md",
	"priority": -5,
})

sysconf.set(("channels", "repo-nrpms"), {
	"name": "Various packages from Nrpms for $name $version",
	"baseurl": "http://yum.nrpms.net/$path-$version-%{_arch}/production",
	"type": "rpm-md",
	"priority": -10,
})

sysconf.set(("channels", "repo-atrpms"), {
	"name": "Various packages from ATrpms for $name $version",
	"baseurl": "http://apt.physik.fu-berlin.de/$path/$version/en/%{_arch}/at-testing",
	"type": "rpm-md",
	"priority": -10,
})

sysconf.set(("channels", "repo-livna"), {
	"name": "Incompatible packages from Livna.org for $name $version",
	"baseurl": "http://rpm.livna.org/fedora/$version/%{_arch}/RPMS.stable",
	"type": "rpm-md",
	"priority": -100,
})

sysconf.set(("channels", "repo-fedora.us"), {
	"name": "Incompatible packages from Fedora.us for $name $version",
	"baseurl": "http://download.fedora.us/fedora/$path/$version/%{_arch}/RPMS.extras/",
	"type": "rpm-md",
	"priority": -100,
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
