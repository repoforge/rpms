# $Id$
# Authority: dag

### RHEL5.5 ships with samba3x and libtalloc-1.2.0
# ExcludeDist: el5

%define real_name talloc

Summary: The talloc library
Name: libtalloc
Version: 2.0.1
Release: 1%{?dist}
License: LGPLv3+
Group: System Environment/Libraries
URL: http://talloc.samba.org/

Source: http://samba.org/ftp/talloc/talloc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: docbook-style-xsl
BuildRequires: libxslt

%description
A library that implements a hierarchical allocator with destructors.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
./autogen.sh
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__ln_s} libtalloc.so.%{version} %{buildroot}%{_libdir}/libtalloc.so.2
%{__ln_s} libtalloc.so.%{version} %{buildroot}%{_libdir}/libtalloc.so

%{__rm} -rf %{buildroot}%{_datadir}/swig/
%{__rm} -rf %{buildroot}%{_libdir}/swig*/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/libtalloc.so.*
%exclude %{_libdir}/libtalloc.a

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/talloc.3*
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Sun Jun 13 2010 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Initial package. (using DAR)
