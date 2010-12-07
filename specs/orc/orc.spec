# $Id$
# Authority: dag

Summary: The Oil Run-time Compiler
Name: orc
Version: 0.4.11
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://code.entropywave.com/projects/orc/

Source0: http://code.entropywave.com/download/orc/orc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk-doc
BuildRequires: libtool

%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package doc
Summary: Documentation for Orc
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for Orc.

%package devel
Summary: Development files and static libraries for Orc
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-compiler
Requires: pkgconfig

%description devel
This package contains the files needed to build packages that depend
on orc.

%package compiler
Summary: Orc compiler
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description compiler
The Orc compiler, to produce optimized code.

%prep
%setup
autoreconf -vif

%build
%configure \
    --disable-static \
    --enable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/orc/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_libdir}/liborc-0.4.so.*
%{_libdir}/liborc-test-0.4.so.*

%files doc
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/orc/

%files devel
%defattr(-, root, root, 0755)
%doc examples/*.c
%{_includedir}/orc-0.4/
%{_libdir}/liborc-0.4.so
%{_libdir}/liborc-test-0.4.so
%{_libdir}/pkgconfig/orc-0.4.pc
%{_bindir}/orc-bugreport
%exclude %{_libdir}/liborc-0.4.la
%exclude %{_libdir}/liborc-test-0.4.la

%files compiler
%defattr(-, root, root, 0755)
%{_bindir}/orcc

%changelog
* Sat Dec 04 2010 Dag Wieers <dag@wieers.com> - 0.4.11-1
- Initial package. (based on fedora)
