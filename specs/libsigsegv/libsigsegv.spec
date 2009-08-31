# $Id$
# Authority: dries
# Upstream: Bruno Haible <bruno$clisp,org>

Summary: Library which handles page faults
Name: libsigsegv
Version: 2.7
Release: 1
License: GPL
Group: Development/Libraries
URL: http://sourceforge.net/projects/libsigsegv/

Source: http://ftp.gnu.org/gnu/libsigsegv/libsigsegv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
GNU libsigsegv is a library for handling page faults. A page fault occurs
when a program tries to access a region of memory that is currently not
available. Catching and handling a page fault is a useful technique for
implementing garbage collectors, stack overflow handlers, persistent
databases, and distributed shared memory.

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
%configure --enable-shared --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libsigsegv.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/sigsegv.h
%{_libdir}/libsigsegv.so
%exclude %{_libdir}/*.la

%changelog
* Mon Aug 31 2009 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Wed Nov 14 2007 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Updated to release 2.5.

* Wed Dec 27 2006 Dries Verachtert <dries@ulyssis.org> - 2.4-1
- Updated to release 2.4.

* Sat Apr 29 2006 Dries Verachtert <dries@ulyssis.org> - 2.3-1
- Updated to release 2.3.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Initial package.
