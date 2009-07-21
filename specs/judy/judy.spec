# $Id$
# Authority: dries
# Upstream: Troy <heber$hp,com>

Summary: Library which provides fully dynamic arrays
Name: judy
Version: 1.0.5
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://judy.sourceforge.net/

Source: http://dl.sf.net/judy/Judy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Judy library provides fully dynamic arrays. These arrays may be indexed 
by a 32- or 64- bit word size, a null terminated string, or an array-of-bytes 
plus length. A dynamic array (sparsely populated) can also be thought of as a 
mapping function or associative memory. These arrays are both speed- and 
memory- efficient across a wide range of index set types (sequential, 
periodic, clustered, random). Their speed and memory usage are typically 
better than storage models such as skiplists, linked lists, binary, ternary, 
b-trees, or even hashing, and improves with very large data sets.

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
# FIXME: build fails with %{?_smp_mflags}
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README
%doc %{_mandir}/man3/J*.3*
%{_libdir}/libJudy.so.*

%files devel
%{_includedir}/Judy.h
%{_libdir}/libJudy.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Tue Jul 21 2009 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1
- Updated to releae 1.0.5.

* Wed Nov 14 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Initial package.
