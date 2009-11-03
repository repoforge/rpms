# $Id$

# Authority: dag

%define _includedir %{_prefix}/include/freetds

Summary: Implementation of the Sybase/Microsoft TDS (Tabular DataStream) protocol
Name: freetds
Version: 0.62.1
Release: 0%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.freetds.org/

Source:	ftp://ftp.ibiblio.org/pub/Linux/ALPHA/freetds/stable/freetds-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: unixODBC-devel
Obsoletes: freetds-unixodbc <= %{version}, freetds-doc <= %{version}

%description
FreeTDS is a project to document and implement the TDS (Tabular
DataStream) protocol. TDS is used by Sybase and Microsoft for
client to database server communications. FreeTDS includes call
level interfaces for DB-Lib, CT-Lib, and ODBC.

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
%configure \
	--with-tdsver="4.2" \
	--enable-msdblib \
	--with-unixodbc="%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la
#%{__rm} -rf %{buildroot}%{_docdir}

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%doc doc/doc/freetds-*/reference/ doc/doc/freetds-*/userguide/ doc/images/
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/*.conf
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
### Redefined _includedir to be %{_includedir}/freetds/
%{_includedir}/

%changelog
* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.62.1-0
- Added --enable-msdblib configure option. (Dean Mumby)
- Updated to release 0.62.1.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.61-0
- Initial package. (using DAR)
