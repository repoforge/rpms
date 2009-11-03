# $Id$
# Authority: dag
# Upstream: <linux-sparse$vger,kernel,org>

Summary: Semantic parser
Name: sparse
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://kernel.org/pub/linux/kernel/people/josh/sparse/

Source: http://kernel.org/pub/linux/kernel/people/josh/sparse/dist/sparse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Sparse, the semantic parser, provides a compiler frontend capable of parsing
most of ANSI C as well as many GCC extensions, and a collection of sample
compiler backends, including a static analyzer also called "sparse".

Sparse provides a set of annotations designed to convey semantic information
about types, such as what address space pointers point to, or what locks
a function acquires or releases.

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
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -Wwrite-strings -fPIC" \
	PREFIX="%{_prefix}" \
	BINDIR="%{_bindir}" \
	LIBDIR="%{_libdir}" \
	INCLUDEDIR="%{_includedir}" \
	PKGCONFIGDIR="%{_libdir}/pkgconfig"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__make} install DESTDIR="%{buildroot}" \
	PREFIX="%{_prefix}" \
	BINDIR="%{_bindir}" \
	LIBDIR="%{_libdir}" \
	INCLUDEDIR="%{_includedir}" \
	PKGCONFIGDIR="%{_libdir}/pkgconfig"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc FAQ LICENSE README
%{_bindir}/cgcc
%{_bindir}/sparse

%files devel
%defattr(-, root, root, 0755)
%doc LICENSE
%{_includedir}/sparse/
%{_libdir}/libsparse.a
%{_libdir}/pkgconfig/sparse.pc

%changelog
* Sun May 06 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Updated to release 0.2.

* Mon Nov 20 2006 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
