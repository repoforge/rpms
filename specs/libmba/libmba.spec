# $Id$

# Authority: dries
# Upstream:

Summary: Library of generic C modules
Name: libmba
Version: 0.8.10
Release: 1.2%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.ioplex.com/~miallen/libmba/

Source: http://www.ioplex.com/~miallen/libmba/dl/libmba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires:

%description
The libmba package is a collection of mostly independent C modules
potentially useful to any project. There are the usual ADTs including a
linkedlist, hashmap, pool, stack, and varray, a flexible memory allocator,
CSV parser, path canonicalization routine, I18N text abstraction,
configuration file module, portible semaphores, condition variables and
more. The code is designed so that individual modules can be integrated into
existing codebases rather than requiring the user to commit to the entire
library. The code has no typedefs, few comments, and extensive man pages and
HTML documentation.

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
%doc %{_mandir}/man?/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mba
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.10-1.2
- Rebuild for Fedora Core 5.

* Wed Sep 1 2004 Dries Verachtert <dries@ulyssis.org> 0.8.10-1
- Updated to version 0.8.10.

* Wed Jun 2 2004 Dries Verachtert <dries@ulyssis.org> 0.8.9-2
- fixed the License tag (libmba uses the MIT license)
  Thanks Michael B Allen for reporting the problem!

* Sat May 23 2004 Dries Verachtert <dries@ulyssis.org> 0.8.9-1
- Initial package.

