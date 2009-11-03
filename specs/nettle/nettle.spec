# $Id$

# Authority: dries
# Upstream:

Summary: Cryptographic library
Name: nettle
Version: 1.12
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.lysator.liu.se/~nisse/nettle/

Source: http://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: m4, openssl-devel, gmp-devel

%description
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: in crypto toolkits for object-oriented languages (C++,
Python, Pike, etc.), in applications like LSH or GNUPG, or even in kernel
space. In most contexts, you need more than the basic cryptographic
algorithms; you also need some way to keep track of available algorithms and
their properties and variants. You often have some algorithm selection
process, often dictated by a protocol you want to implement. And as the
requirements of applications differ in subtle and not so subtle ways, an API
that fits one application well can be a pain to use in a different context,
which is why there are so many different cryptographic libraries around.
Nettle tries to avoid this problem by doing one thing, the low-level crypto
stuff, and providing a simple but general interface to it. In particular,
Nettle doesn't do algorithm selection. It doesn't do memory allocation. It
doesn't do any I/O. The idea is that one can build several application- and
context-specific interfaces on top of Nettle and share the code, testcases,
benchmarks, documentation, etc.

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
%configure --enable-shared
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/nettle/*.h
%{_libdir}/*.a
%{_datadir}/info/nettle.info.gz
%{_libdir}/*.so

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-2.2
- Rebuild for Fedora Core 5.

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Fix ownership of devel package.

* Tue Jun 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
