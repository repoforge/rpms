# $Id$
# Authority: dag
# Upstream: Erik Grinaker <erikg@wired-networks.net>
# Upstream: <revelation-devel@oss.wired-networks.net>

Summary: Password manager
Name: revelation
Version: 0.3.0
Release: 2
License: GPL
Group: Applications/Productivity
URL: http://oss.wired-networks.net/revelation/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://oss.wired-networks.net/revelation/revelation-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.0, python-crypto >= 1.9
Requires: python-crypto >= 1.9, gnome-python2-canvas, gnome-python2-gconf

%description
Revelation is a password manager. It organizes accounts in
a tree structure, and stores them as AES-encrypted XML files.

%prep
%setup

%build
python2 setup.py build

%install
%{__rm} -rf %{buildroot}
python2 setup.py install \
	--root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/python*/site-packages/revelation/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/revelation/

%changelog
* Thu Apr 08 2004 Dag Wieers <dag@wieers.com> - 0.3.0-2
- Added gnome-python2-gconf dependency. (Erik Grinaker)

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Updated to release 0.3.0.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Cosmetic rebuild for Group-tag and BuildArch-tag.

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Updated to release 0.2.1.

* Sun Feb 22 2004 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Updated to release 0.2.0.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 0.1.2-0
- Updated to release 0.1.2.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.1.1-0
- Initial Package. (using DAR)
