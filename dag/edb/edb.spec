# Authority: freshrpms
Summary: Enlightenment DataBase access library.
Name: edb
Version: 1.0.3
Release: 0
License: BSD
Group: System Environment/Libraries
URL: http://enlightenment.org/pages/edb.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Edb is a simple, clean, high-level db access/storage library.

%package devel
Summary: Header files and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}.

%prep
%setup

%build
CFLAGS="%{optflags}" ./configure \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--datadir=%{_datadir}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README src/LICENSE
%{_bindir}/edb_*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/edb-config
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
#exclude %{_libdir}/*.la

%changelog
* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Initial package. (using DAR)
