
# $Id$

# Authority: dries

Summary: C++ library for rapid development of database applications
Summary(nl): C++ library om snel database applicaties te ontwikkelen
Name: hk_classes
Version: 0.6.3
Release: 1
License: GPL
Group: Development/Libraries
URL: http://hk-classes.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/hk-classes/hk_classes-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, gcc-c++, postgresql-devel, mysql-devel, unixODBC-devel, python, python-devel

%description
hk_classes is C++ library which allows rapid development of database
applications with all features a modern database application should have
like forms an reports. hk_classes is database and GUI independent.

%description -l nl
hk_classes is een C++ library waarmee snel database toepassingen ontwikkeld
kunnen worden met alle eigenschappen van een modere database applicatie
zoals formulieren en rapporten. hk_classes is onafhankelijk van de GUI en de
database.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall
# echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
# export DESTDIR=$RPM_BUILD_ROOT
# {__make} install-strip

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING NEWS 
%{_bindir}/hk_actionquery
%{_bindir}/hk_exportcsv
%{_bindir}/hk_exporthtml
%{_bindir}/hk_exportxml
%{_bindir}/hk_importcsv
%{_bindir}/hk_report
%{_includedir}/hk_classes/*.h
%{_libdir}/hk_classes/drivers/libhk_mysqldriver.la
%{_libdir}/hk_classes/drivers/libhk_mysqldriver.so.3.0.4
%{_libdir}/hk_classes/drivers/libhk_odbcdriver.la
%{_libdir}/hk_classes/drivers/libhk_odbcdriver.so.0.0.0
%{_libdir}/hk_classes/drivers/libhk_postgresdriver.la
%{_libdir}/hk_classes/drivers/libhk_postgresdriver.so.0.0.1
%{_libdir}/hk_classes/drivers/libhk_mysqldriver.so.3
%{_libdir}/hk_classes/drivers/libhk_mysqldriver.so
%{_libdir}/hk_classes/drivers/libhk_postgresdriver.so.0
%{_libdir}/hk_classes/drivers/libhk_postgresdriver.so
%{_libdir}/hk_classes/drivers/libhk_odbcdriver.so.0
%{_libdir}/hk_classes/drivers/libhk_odbcdriver.so
%{_libdir}/hk_classes/libhk_classes.la
%{_libdir}/hk_classes/libhk_classes.so.5.0.1
%{_libdir}/hk_classes/libhk_classes.so.5
%{_libdir}/hk_classes/libhk_classes.so
%{_libdir}/python2.2/site-packages/_hk_classes.so
%{_libdir}/python2.2/site-packages/hk_classes.py
%{_libdir}/python2.2/site-packages/hk_classes.pyc
%{_datadir}/man/man1/hk_actionquery.1man.gz
%{_datadir}/man/man1/hk_exportcsv.1man.gz
%{_datadir}/man/man1/hk_exporthtml.1man.gz
%{_datadir}/man/man1/hk_exportxml.1man.gz
%{_datadir}/man/man1/hk_importcsv.1man.gz
%{_datadir}/man/man1/hk_report.1man.gz

%changelog
* Tue Dec 30 2003 Dries Verachtert <dries@ulyssis.org> 0.6.2a-1
- first packaging for Fedora Core 1
