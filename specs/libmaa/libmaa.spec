# $Id$
# Authority: dag

Summary: General purpose data structures and functions
Name: libmaa
Version: 1.3.1
Release: 1%{?dist}
License: LGPLv2
Group: System/Libraries
URL: http://sourceforge.net/projects/dict/

Source: http://prdownloads.sf.net/dict/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__make} install DESTDIR="%{buildroot}"

%files
%doc ChangeLog COPYING* NEWS README
%_libdir/libmaa.so.*

%files devel
%doc doc/*.ps
%{_libdir}/libmaa.so
%{_includedir}/maa.h
%exclude %{_libdir}/libmaa.a
%exclude %{_libdir}/libmaa.la

%changelog
* Mon Jan 02 2012 Aleksey Cheusov <vle@gmx.net> 1.3.1-1
- Adapted for Repoforge.

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
