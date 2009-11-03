# $Id$
# Authority: dag
# Upstream: Erik Grinaker <erikg$codepoet,no>
# Upstream: <revelation-list$oss,codepoet,no>

Summary: Password manager
Name: revelation
Version: 0.3.4
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://oss.codepoet.no/revelation/

Source: ftp://oss.codepoet.no/revelation/revelation-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.0, python-crypto >= 1.9, python-devel
Requires: python >= 2.0, python-crypto >= 1.9, gnome-python2-canvas, gnome-python2-gconf

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

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%config %{_sysconfdir}/gconf/schemas/revelation.schemas
%{_bindir}/revelation
%{_libdir}/python*/site-packages/revelation/
%{_datadir}/applications/revelation.desktop
%{_datadir}/pixmaps/revelation.png
%{_datadir}/revelation/

%changelog
* Tue Sep 28 2004 Dag Wieers <dag@wieers.com> - 0.3.4-1
- Updated to release 0.3.4.

* Mon Aug 30 2004 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Updated to release 0.3.3.

* Mon Aug 09 2004 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Updated to release 0.3.2.
- Updated to release 0.3.1.

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 0.3.0-3
- Install schema.

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
