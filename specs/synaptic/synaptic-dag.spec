# Authority: atrpms
Summary: Graphical package management program using apt.
Name: synaptic
Version: 0.45
Release: 0
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/synaptic/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/synaptic/synaptic.pkg/%{version}/%{name}-%{version}.tar.gz
#Patch0: synaptic-0.36.1-sectver.patch
#Patch1: synaptic-0.36.1-candver.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: apt-devel >= 0.5.4, rpm-devel >= 4.0, gtk2-devel, libglade2-devel
BuildRequires: libstdc++-devel

%description
Synaptic (previously known as raptor) is a graphical package management
program for apt. It provides the same features as the apt-get command line 
utility with a GUI front-end based on Gtk+

%prep
%setup
#patch0 -b sectver
#%patch1 -b candver

%{__cat} <<EOF >synaptic.apps
USER=root
PROGRAM=%{_sbindir}/synaptic
SESSION=true
FALLBACK=false
EOF

%{__cat} <<EOF >synaptic.pam
#%PAM-1.0
auth	sufficient	/lib/security/pam_rootok.so
auth	sufficient	/lib/security/pam_timestamp.so
auth	required	/lib/security/pam_stack.so service=system-auth
session	required	/lib/security/pam_permit.so
session	optional	/lib/security/pam_xauth.so
session	optional	/lib/security/pam_timestamp.so
account	required	/lib/security/pam_permit.so
EOF

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Synaptic Package Manager
Comment=Graphical package management program using apt
Icon=%{_datadir}/%{name}/pixmaps/%{name}_48x48.png
Exec=synaptic
Terminal=false
Type=Application
Categories=GNOME;Application;SystemSetup;
EOF

%build
%configure 
%{__make} %{?_smp_mflags}

%install
%{__rm} -fr %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_sysconfdir}/security/console.apps/ \
			%{buildroot}%{_sysconfdir}/pam.d/ \
			%{buildroot}%{_datadir}/applications/

%{__ln_s} -f %{_bindir}/consolehelper %{buildroot}%{_bindir}/synaptic

%{__install} -m0644 synaptic.apps %{buildroot}%{_sysconfdir}/security/console.apps/synaptic
%{__install} -m0644 synaptic.pam %{buildroot}%{_sysconfdir}/pam.d/synaptic

desktop-file-install --vendor "gnome"              \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/gnome/
rm -f %{buildroot}%{_sysconfdir}/X11/sysconfig/synaptic.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/pam.d/*
%config %{_sysconfdir}/security/console.apps/*
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/control-center-2.0/capplets/*.desktop
%{_datadir}/synaptic/

%changelog
* Tue Nov 11 2003 Dag Wieers <dag@wieers.com> - 0.45-0
- Updated to release 0.45.

* Tue Jul 22 2003 Dag Wieers <dag@wieers.com> - 0.39-0
- Updated to release 0.39.

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 0.36-0
- Updated to release 0.36.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.35.1-0
- Updated to release 0.35.1.

* Thu Feb 27 2003 Dag Wieers <dag@wieers.com> - 0.32-0
- Updated to release 0.32.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.31-0
- Initial package. (using DAR)
