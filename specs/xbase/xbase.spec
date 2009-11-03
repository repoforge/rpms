# $Id$
# Authority: dag
# Upstream: Derry Bryson <xbase$techass,com>
# Upstream: <xdb-devel$lists,sf,net>

Summary: Xbase dBase database file library
Name: xbase
Version: 2.0.0
Release: 0.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://linux.techass.com/projects/xdb/

Source: http://dl.sf.net/xdb/xbase-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libtool, gcc-c++

%description
Library for accessing dBase .dbf, .ndx, .dbt, and Clipper .ntx files.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%{__libtoolize} --force
%configure \
	--enable-static
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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/checkndx
%{_bindir}/copydbf
%{_bindir}/dbfutil1
%{_bindir}/dbfxtrct
%{_bindir}/deletall
%{_bindir}/dumphdr
%{_bindir}/dumprecs
%{_bindir}/packdbf
%{_bindir}/reindex
%{_bindir}/undelall
%{_bindir}/zap
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/html/ docs/latex/
%{_bindir}/xbase-config
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/xbase/
#%{_includedir}/xdb/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-0.2
- Rebuild for Fedora Core 5.

* Fri Sep 12 2003 Dag Wieers <dag@wieers.com> - 2.0.0-0
- Initial package. (using DAR)
