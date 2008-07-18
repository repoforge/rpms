# $Id$
# Authority: dag

Summary: Fake chroot environment
Name: fakechroot
Version: 2.7
Release: 1
License: LGPL
Group: Development/Tools
URL: http://packages.debian.org/unstable/utils/fakechroot.html

Source: http://ftp.debian.org/debian/pool/main/f/fakechroot/fakechroot_%{version}.orig.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
fakechroot runs a command in an environment were is additionally
possible to use the chroot(8) call without root privileges. This is
useful for allowing users to create their own chrooted environment
with possibility to install another packages without need for root
privileges.

%prep
%setup

%{__perl} -pi -e 's|int readlink|ssize_t readlink|' src/libfakechroot.c
%{__chmod} -x scripts/ldd.fake scripts/restoremode.sh scripts/savemode.sh

%build
%configure \
	--disable-dependency-tracking \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE scripts/ldd.fake scripts/restoremode.sh scripts/savemode.sh
%doc %{_mandir}/man1/fakechroot.1.gz
%{_bindir}/fakechroot
%{_libdir}/fakechroot/
%exclude %{_libdir}/fakechroot/libfakechroot.la

%changelog
* Fri Jul 18 2008 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Tue May 08 2007 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Updated to release 2.6.

* Wed Mar 21 2007 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
