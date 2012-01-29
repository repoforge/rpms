Name: libmaa
Version: 1.3.1
Release: 1%{?dist}

Summary: General purpose data structures and functions
License: LGPLv2
Group: System/Libraries

Url: http://sourceforge.net/projects/dict/
Source: http://prdownloads.sf.net/dict/%{name}-%{version}.tar.gz
Packager: Aleksey Cheusov <vle@gmx.net>

BuildRequires: libtool

%description
The LIBMAA library provides many low-level data structures which are
helpful for writing compilers, including hash tables, sets, lists,
debugging support, and memory management.  Although LIBMAA was
designed and implemented as a foundation for the Khepera
Transformation System, the data structures are generally applicable to
a wide range of programming problems.
The memory management routines are especially helpful for improving the
performance of memory-intensive applications.

%package devel
Summary: Development files of libmaa
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
The LIBMAA library provides many low-level data structures which are
helpful for writing compilers, including hash tables, sets, lists,
debugging support, and memory management.  Although LIBMAA was
designed and implemented as a foundation for the Khepera
Transformation System, the data structures are generally applicable to
a wide range of programming problems.
The memory management routines are especially helpful for improving the
performance of memory-intensive applications.

This package contains development files of libmaa.

%package devel-doc
Summary: Documentation for libmaa
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
The LIBMAA library provides many low-level data structures which are
helpful for writing compilers, including hash tables, sets, lists,
debugging support, and memory management.  Although LIBMAA was
designed and implemented as a foundation for the Khepera
Transformation System, the data structures are generally applicable to
a wide range of programming problems.
The memory management routines are especially helpful for improving the
performance of memory-intensive applications.

This package contains development documentation for libmaa.

%prep
%setup

%build
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=$RPM_BUILD_ROOT install
install -d %{buildroot}%{_docdir}/%{name}
install -p -m644 doc/*.ps %{buildroot}%{_docdir}/%{name}

%files
%doc COPYING* ChangeLog NEWS README
%_libdir/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la

%files devel-doc
%{_docdir}/%{name}

%changelog
* Mon Jan 02 2012 Aleksey Cheusov <vle@gmx.net> 1.3.1-1
- adapted for repoforge

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- NMU: 1.3.1 (gcc-4.6 ready)

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0
- Disabled devel-static package

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Rebuilt for soname set-versions

* Mon Jun 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

