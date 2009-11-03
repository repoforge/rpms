# $Id$
# Authority: dag

Summary: ISO 9660 Rock Ridge Filesystem Manipulator
Name: xorriso
%define real_version 0.4.2
Version: 0.4.2.pl01
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://scdbackup.sourceforge.net/xorriso_eng.html

Source: http://scdbackup.sourceforge.net/xorriso-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: ncurses-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel

%description
xorriso is a program which maps file objects from POSIX compliant filesystems
into Rock Ridge enhanced ISO 9660 filesystems and allows session-wise
manipulation of such filesystems. It can load the management information of
existing ISO images and it writes the session results to optical media or to
filesystem objects.

A special property of xorriso is that it needs neither an external ISO 9660
formatter program nor an external burn program for CD or DVD but rather
incorporates the libraries of libburnia-project.org.

%prep
%setup -n %{name}-%{real_version}

%build
%configure \
    --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CONTRIBUTORS COPYING COPYRIGHT README
%doc %{_mandir}/man1/xorriso.1*
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorrisofs
#exclude %{_libdir}/pkgconfig/xorriso.pc

%changelog
* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 0.4.2.pl01-1
- Updated to release 0.4.2.pl01.

* Thu Sep 10 2009 Dag Wieers <dag@wieers.com> - 0.4.2.pl00-1
- Updated to release 0.4.2.pl00.

* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 0.4.0.pl01-1
- Updated to release 0.4.0.pl01.

* Sat Jul 04 2009 Dag Wieers <dag@wieers.com> - 0.4.0.pl00-1
- Updated to release 0.4.0.pl00.

* Mon Apr 20 2009 Dag Wieers <dag@wieers.com> - 0.3.8.pl00-1
- Updated to release 0.3.8.pl00.

* Sun Mar 22 2009 Dag Wieers <dag@wieers.com> - 0.3.6.pl00-1
- Updated to release 0.3.6.pl00.

* Mon Mar 02 2009 Dag Wieers <dag@wieers.com> - 0.3.4.pl00-1
- Updated to release 0.3.4.pl00.

* Mon Feb 02 2009 Dag Wieers <dag@wieers.com> - 0.3.2.pl01-1
- Updated to release 0.3.2.pl01.

* Tue Jan 06 2009 Dag Wieers <dag@wieers.com> - 0.3.2.pl00-1
- Updated to release 0.3.2.pl00.

* Tue Dec 02 2008 Dag Wieers <dag@wieers.com> - 0.3.0.pl00-1
- Updated to release 0.3.0.pl00.

* Sat Nov 22 2008 Dag Wieers <dag@wieers.com> - 0.2.8.pl01-1
- Updated to release 0.2.8.pl01.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.2.6.pl01-1
- Initial package. (using DAR)
