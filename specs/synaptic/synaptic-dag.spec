# $Id$
# Authority: matthias
# Upstream: Daniel Paarmann <daniel$paarmann,net>

Summary: Graphical package management program using apt
Name: synaptic
Version: 0.48.2
Release: 2
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/synaptic/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/synaptic/synaptic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apt-devel >= 0.5.4, rpm-devel >= 4.0, gtk2-devel, libglade2-devel >= 2.0
BuildRequires: libstdc++-devel, docbook-utils, gettext
BuildRequires: scrollkeeper, xmlto

%description
Synaptic (previously known as raptor) is a graphical package management
program for apt. It provides the same features as the apt-get command line 
utility with a GUI front-end based on Gtk+

%prep
%setup

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

%{__cat} <<EOF >synaptic.desktop
[Desktop Entry]
Name=Synaptic Package Manager
Comment=Graphical package management program using apt
Icon=synaptic.png
Exec=synaptic
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;SystemSetup;
EOF

%build
%configure 
%{__make} %{?_smp_mflags}

%install
%{__rm} -fr %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f %{_bindir}/consolehelper %{buildroot}%{_bindir}/synaptic

%{__install} -D -m0644 pixmaps/synaptic_48x48.png %{buildroot}%{_datadir}/pixmaps/synaptic.png
%{__install} -D -m0644 synaptic.apps %{buildroot}%{_sysconfdir}/security/console.apps/synaptic
%{__install} -D -m0644 synaptic.pam %{buildroot}%{_sysconfdir}/pam.d/synaptic

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor "gnome"              \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	synaptic.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_sysconfdir}/X11/sysconfig/synaptic.desktop \
		%{buildroot}%{_datadir}/applications/synaptic.desktop

%post
%{_bindir}/scrollkeeper-update -q || :

%postun
%{_bindir}/scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/synaptic/
%config %{_sysconfdir}/pam.d/*
%config %{_sysconfdir}/security/console.apps/*
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/applications/*.desktop
#%{_datadir}/control-center-2.0/capplets/*.desktop
%{_datadir}/omf/synaptic/
%{_datadir}/pixmaps/*.png
%{_datadir}/synaptic/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Mon Apr 19 2004 Dag Wieers <dag@wieers.com> - 0.48.2-2
- Removed second desktop-file.

* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 0.47-1
- Updated to release 0.47.

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
