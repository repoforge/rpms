# $Id$
# Authority: dag

Summary: Extract data compressed with PKWARE Data Compression Library
Name: dynamite
Version: 0.1
Release: 2%{?dist}
License: MIT
Group: Applications/Archiving
URL: http://www.synce.org/index.php/Dynamite

Source: http://dl.sf.net/synce/dynamite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Dynamite is a tool and library for decompressing data compressed with PKWARE
Data Compression Library and it was created from the specification provided
by a post in the comp.compression newsgroup.

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
%configure \
	--program-prefix="%{?_program_prefix}" \
	--disable-static \
	--disable-rpath
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_bindir}/dynamite
%{_libdir}/libdynamite.so.*

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/aclocal/dynamite.m4
%{_includedir}/libdynamite.h
%exclude %{_libdir}/libdynamite.la
%{_libdir}/libdynamite.so

%changelog
* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 0.1-2
- Fixed group.

* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
