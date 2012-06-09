# $Id$
# Authority: dag
# Upstream: <freetds$lists,ibiblio,org>

%define _includedir %{_prefix}/include/freetds

Summary: Implementation of the Sybase/Microsoft TDS (Tabular DataStream) protocol
Name: freetds
Version: 0.91
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.freetds.org/

Source:	ftp://ftp.ibiblio.org/pub/Linux/ALPHA/freetds/stable/freetds-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: gnutls-devel
BuildRequires: libtool
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
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
	--disable-dependency-tracking \
	--enable-msdblib \
	--with-gnutls \
	--with-openssl \
	--with-tdsver="4.2" \
	--with-unixodbc="%{_prefix}" \
	--enable-sybase-compat
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
%doc AUTHORS BUGS ChangeLog COPYING* INSTALL NEWS README TODO
%doc doc/*.html doc/*.sgml doc/*.txt samples/
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/*.conf
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc samples/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
### Redefined _includedir to be %{_includedir}/freetds/
%{_includedir}/

%changelog
* Sat Jun 09 2012 David Hrbáč <david@hrbac.cz> - 0.91-1
- new upstream release

* Thu Dec 09 2010 Steve Huff <shuff@vecna.org> - 0.82-1
- Updated to release 0.82 (thanks Dave Miller!)
- Captured some missing dependencies.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.63-1
- Updated to release 0.63.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.62.3-1
- Updated to release 0.62.3.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 0.61.2-0
- Added --enable-msdblib configure option. (Dean Mumby)
- Updated to release 0.61.2.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.61-0
- Initial package. (using DAR)
