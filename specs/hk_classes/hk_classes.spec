# $Id$
# Authority: dries
# Upstream: <bugreport$knoda,org>

Summary: C++ library for rapid development of database applications
Name: hk_classes
Version: 0.8.1
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://hk-classes.sourceforge.net/

Source: http://dl.sf.net/hk-classes/hk_classes-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
BuildRequires: postgresql-devel, mysql-devel
BuildRequires: unixODBC-devel, python
BuildRequires: python-devel, sqlite-devel, pkgconfig
BuildRequires: fontconfig-devel

%description
hk_classes is C++ library which allows rapid development of database
applications with all features a modern database application should have
like forms an reports. hk_classes is database and GUI independent.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%{_bindir}/hk_*
%{_includedir}/hk_classes/*.h
%{_libdir}/hk_classes/drivers/libhk_*driver.*
%{_libdir}/hk_classes/libhk_classes.*
%{_libdir}/python*/site-packages/_hk_classes.*
%{_libdir}/python*/site-packages/hk_classes.*
%{_datadir}/man/man1/hk_*

%changelog
* Thu Apr 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Updated to release 0.8.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Update to release 0.8.

* Sat Jun 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.4-1
- Update to release 0.7.4.

* Sat Mar 19 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1
- Update to release 0.7.3.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Update to release 0.7.2.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 0.7.1-1
- Update to version 0.7.1.

* Mon Jul 12 2004 Dries Verachtert <dries@ulyssis.org> 0.7-1
- Update to version 0.7.

* Tue Dec 30 2003 Dries Verachtert <dries@ulyssis.org> 0.6.2a-1
- first packaging.

