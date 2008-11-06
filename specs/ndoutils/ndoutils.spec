# Tag: test 
# $Id$
# Authority: cmr
# Upstream: 

Summary: Nagios Database Object plugin to stora Nagios data in a relational Database 
Name: ndoutils
Version: 1.4b7
Release: 0beta7
License: GPL
Group: Applications/System
URL: http://www.nagios.org/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel
BuildRequires: postgresql-devel
Requires: nagios >= 3.0.0
Requires: mysql-libs
Requires: postgresql

%description
NDOUtils allows you to export current and historical data from one or more Nagios instances to a MySQL database. Several community addons use this as one of their data sources. 

%prep
%setup

%build
%configure --with-mysql-lib=%{_libdir}/mysql/
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libexecdir}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -m0755 src/ndomod-3x.o %{buildroot}%{_libexecdir}
%{__install} -m0755 src/ndo2db-3x %{buildroot}%{_sbindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libexecdir}/ndomod-3x.o
%{_sbindir}/ndo2db-3x
%doc Changelog README TODO UPGRADING REQUIREMENTS config/*


%changelog
* Thu Nov 06 2008 Christoph Maser <cmr@financial.com>
- Initial package. 

