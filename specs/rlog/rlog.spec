# $Id$
# Authority: dag

Summary: Runtime Logging for C++
Name: rlog
Version: 1.3.7
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.arg0.net/rlog

Source: http://rlog.googlecode.com/files/rlog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: doxygen, tetex-latex

%description
RLog provides a flexible message logging facility for C++ programs and
libraries.  It is meant to be fast enough to leave in production code.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-static \
    --disable-valgrind
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/rlog/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_libdir}/librlog.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/html/ docs/latex/refman.pdf
%{_includedir}/rlog/
%{_libdir}/librlog.so
%{_libdir}/pkgconfig/librlog.pc
%exclude %{_libdir}/librlog.la

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.7-1
- Initial package. (using DAR)
