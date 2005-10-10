# $Id$
# Authority: dries
# Upstream: pabloy$pcpool,mathematik,uni-freiburg,de

Summary: Handle C strings in a safe way
Name: sstrings
Version: 1.0.4
Release: 1
License: GPL
Group: Development/Libraries
URL: http://pcpool.mathematik.uni-freiburg.de/~pabloy/projects/sstrings/

Source: http://pcpool.mathematik.uni-freiburg.de/~pabloy/projects/sstrings/sstrings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake, autoconf, gcc-c++

%description
Safe Strings is a small C library that handles C strings in a safe way. 
The functions of this library look at the necessary space for the operations 
and try to reserve that space (with malloc or realloc). The functions only 
begin working with their tasks when the memory allocation is successful.

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
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Thu Jul 21 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Update to release 1.0.4.

* Tue Jul 12 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Initial package.
