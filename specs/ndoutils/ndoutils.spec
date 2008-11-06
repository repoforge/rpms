# $Id$
# Authority: cmr

# Tag: test

Summary: Nagios plugin to store Nagios data in a relational database 
Name: ndoutils
Version: 1.4b7
Release: 0.beta7
License: GPL
Group: Applications/System
URL: http://www.nagios.org/

Source: http://dl.sf.net/sourceforge/nagios/ndoutils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel
BuildRequires: postgresql-devel
Requires: nagios >= 3.0.0
Requires: mysql-libs
Requires: postgresql

%description
NDOUtils allows you to export current and historical data from one or more Nagios
instances to a MySQL database. Several community addons use this as one of their
data sources.

%prep
%setup

%build
%configure --with-mysql-lib="%{_libdir}/mysql/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/ndomod-3x.o %{buildroot}%{_libexecdir}/ndomod-3x.o
%{__install} -Dp -m0755 src/ndo2db-3x %{buildroot}%{_sbindir}/ndo2db-3x

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README REQUIREMENTS TODO UPGRADING config/*
%{_libexecdir}/ndomod-3x.o
%{_sbindir}/ndo2db-3x

%changelog
* Thu Nov 06 2008 Christoph Maser <cmr@financial.com> - 1.4b7-0.beta7
- Initial package.
