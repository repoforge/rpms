# $Id$
# Authority: dries
# Upstream: Fabrice Bellard <fabrice,bellard$free,fr>

Summary: Tiny C Compiler
Name: tcc
Version: 0.9.24
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://bellard.org/tcc/

Source: http://download.savannah.nongnu.org/releases/tinycc/tcc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
TCC (Tiny C Compiler) is small, fast, unlimited, and safe. You can compile and 
execute C code everywhere (e.g., on rescue disks). It generates optimized x86 
code, and can compile, assemble, and link several times faster than 'gcc -O0'. 
Any C dynamic library can be used directly. It includes an optional memory and 
bounds checker, and bounds-checked code can be mixed freely with standard code. 
C script is also supported--just add '#!/usr/bin/tcc' at the first line of your 
C source, and execute it directly from the command line.

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
%makeinstall tccdir="%{buildroot}%{_libdir}/tcc" docdir="%{buildroot}%{_datadir}/doc/tcc"
%{__mv} %{buildroot}%{_datadir}/doc/tcc rpm-docs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO rpm-docs/*
%doc %{_mandir}/man1/tcc.1*
%{_bindir}/tcc
%{_libdir}/tcc/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libtcc.h
%{_libdir}/libtcc.a

%changelog
* Fri Jul 18 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.24-1
- Updated to release 0.9.24.

* Thu Jun 07 2007 Dag Wieers <dag@wieers.com> - 0.9.23-3
- Fix license tag. (Ronny Fischer)

* Sun Jan 21 2007 Dag Wieers <dag@wieers.com> - 0.9.23-2
- Fix group tag.

* Sun Jan 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.23-1
- Initial package.
