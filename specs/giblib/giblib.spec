# $Id$
# Authority: matthias

Summary: Simple library and a wrapper for imlib2
Name: giblib
Version: 1.2.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://linuxbrit.co.uk/giblib/
Source: http://linuxbrit.co.uk/downloads/giblib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, imlib2-devel, zlib-devel

%description
giblib is a utility library used by many of the applications from
linuxbrit.co.uk. It incorporates doubly linked lists, some string
functions, and a wrapper for imlib2. The wrapper does two things.
It gives you access to fontstyles, which can be loaded from files,
saved to files or defined dynamically through the API. It also,
and more importantly, wraps imlib2's context API.


%package devel
Summary: Static library and header files for giblib
Group: Development/Libraries
Requires: %{name} = %{version}, imlib2-devel, pkgconfig

%description devel
Install this package if you intend to develop using the giblib library.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{_prefix}/doc


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Sep  6 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1.2.3-4
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.2.3-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Feb 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.3.

* Wed Nov 13 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

