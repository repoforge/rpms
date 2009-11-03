# $Id$
# Authority: dries
# Upstream: dprotti$users,sourceforge,net

Summary: Composable Memory Transactions Library
Name: libcmt
Version: 0.1.0
Release: 3%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://libcmt.sourceforge.net

Source: http://dl.sf.net/libcmt/libcmt-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, pkgconfig, glib2-devel >= 2.4

%description
LibCMT (Composable Memory Transactions Library) implements a transactional
model of concurrency, where deadlock is not possible and transactions are
composable (small transactions can be glued together to form larger
transactions without extra effort). It is written as a Glib extension but
can be used with any thread library, not just GThread.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libcmt.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cmt/
%{_libdir}/libcmt.a
%exclude %{_libdir}/libcmt.la
%{_libdir}/pkgconfig/libcmt.pc
%{_libdir}/pkgconfig/libcmt-sharp.pc

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 0.1.0-3
- Fixed group name.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.0-2
- Files section fixed.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.0-1
- Updated to release 0.1.0.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.5-1
- Updated to release 0.0.5.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.4-1
- Updated to release 0.0.4.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.3-1
- Updated to release 0.0.3.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.2-1
- Initial package.
