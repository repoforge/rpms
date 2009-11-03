# $Id$
# Authority: dries

# Upstream: Berke Durak <berke-dev$ouvaton,org>
# Screenshot: http://ara.alioth.debian.org/xara.png

Summary: Query the Debian package database
Name: ara
Version: 1.1.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Databases
URL: http://ara.alioth.debian.org/

Source: http://ara.alioth.debian.org/incoming/ara-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lablgtk, ocaml, gtk2-devel

%description
Ara is a command-line utility for querying the Debian package database. It
has a query syntax allowing you to search for boolean combinations of
regular expressions. It includes a simple syntax and line-editing. A
graphical interface, xara, is also provided.

This program can only be used for querying Debian packages, not for querying
for example Fedora Core, Red Hat or Aurora packages! You also need a file
/var/lib/dpkg/available which contains the list of all Debian packages.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Xara
Comment=Searches in the debian packages database
Exec=xara
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m 755 cli/ara %{buildroot}%{_bindir}/ara
%{__install} -Dp -m 644 doc/ara.1 %{buildroot}%{_mandir}/man1/ara.1
%{__install} -Dp -m 644 etc/ara.config %{buildroot}%{_sysconfdir}/ara.config
%{__install} -Dp -m 755 gui/xara %{buildroot}%{_bindir}/xara
%{__install} -Dp -m 644 doc/xara.1 %{buildroot}%{_mandir}/man1/xara.1
%{__install} -Dp -m 644 etc/xara.config %{buildroot}%{_sysconfdir}/xara.config


%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYING INSTALL TODO
%doc %{_mandir}/man?/*
%{_bindir}/ara
%{_bindir}/xara
%{_datadir}/applications/*.desktop
%{_sysconfdir}/*ara.config

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Sun Apr 03 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.9-1
- Updated to release 1.0.9.

* Wed Dec 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.8-1
- Updated to release 1.0.8.

* Thu Dec 09 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.7-1
- Initial package.
