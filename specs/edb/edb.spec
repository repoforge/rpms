# $Id$
# Authority: dag
# Upstream:

Summary: Enlightenment database access library.
Name: edb
Version: 1.0.3
Release: 1.2%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://enlightenment.org/pages/edb.html

Source: http://dl.sf.net/enlightenment/edb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Edb is a simple, clean, high-level db access/storage library.

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
%doc AUTHORS COPYING README src/LICENSE
%{_bindir}/edb_*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/edb-config
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1.2
- Rebuild for Fedora Core 5.

* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Cosmetic fixes.

* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Initial package. (using DAR)
