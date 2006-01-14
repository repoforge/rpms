# $Id$
# Authority: dries
# Upstream: dprotti$users,sourceforge,net

Summary: Composable Memory Transactions Library
Name: libcmt
Version: 0.0.5
Release: 1
License: LGPL
Group: Developments/Libraries
URL: http://libcmt.sourceforge.net

Source: http://dl.sf.net/libcmt/libcmt-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, glib2-devel, gcc-c++

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

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libcmt.so

%files devel
%{_includedir}/gtransaction.h
%{_libdir}/libcmt.a
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/libcmt.pc

%changelog
* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.5-1
- Updated to release 0.0.5.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.4-1
- Updated to release 0.0.4.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.3-1
- Updated to release 0.0.3.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.2-1
- Initial package.
