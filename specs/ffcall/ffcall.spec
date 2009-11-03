# $Id$
# Authority: dries
# Upstream: Bruno Haible <bruno$clisp,org>

Summary: Foreign function call libraries
Name: ffcall
Version: 1.10
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.haible.de/bruno/packages-ffcall.html

Source: http://www.haible.de/bruno/gnu/ffcall-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.
* avcall - calling C functions with variable arguments
* vacall - C functions accepting variable argument prototypes
* trampoline - closures as first-class C functions
* callback - closures with variable arguments as first-class C functions
             (a reentrant combination of vacall and trampoline)

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: ffcall = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}
%{__install} -d -m0755 %{buildroot}%{_docdir}/ffcal-%{real_version}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc */*.html
%doc %{_mandir}/man3/*
%{_includedir}/*.h
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%exclude %{_datadir}/html/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1.2
- Rebuild for Fedora Core 5.

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Thu Jun 10 2004 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 1.8-5.d
- Cosmetic cleanup.

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8d-4
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.8d-3
- further spec file cleanup

* Tue Nov 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8d-2
- added the html files
- cleanup
- fix the 'Requires:'

* Mon Nov 10 2003 Dries Verachtert <dries@ulyssis.org> 1.8d-1
- first packaging for Fedora Core 1
