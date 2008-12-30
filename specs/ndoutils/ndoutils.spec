# $Id$
# Authority: cmr

Summary: Nagios plugin to store Nagios data in a relational database 
Name: ndoutils
Version: 1.4
Release: 0.beta7.1
License: GPL
Group: Applications/System
URL: http://www.nagios.org/

Source: http://dl.sf.net/sourceforge/nagios/ndoutils-%{version}b7.tar.gz
Source1: ndoutils-init
Source2: ndoutils-config
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel
BuildRequires: postgresql-devel
Requires: nagios >= 3.0.0
Requires: mysql
Requires: postgresql

%description
NDOUtils allows you to export current and historical data from one or more Nagios
instances to a MySQL database. Several community addons use this as one of their
data sources.

%prep
%setup -n ndoutils-%{version}b7

%build
%configure --with-mysql-lib="%{_libdir}/mysql/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/ndomod-3x.o %{buildroot}%{_libexecdir}/ndomod-3x.o
%{__install} -Dp -m0755 src/ndo2db-3x %{buildroot}%{_sbindir}/ndo2db-3x
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/init.d
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/nagios
%{__sed} -e 's*@CONFDIR@*%{_sysconfdir}/nagios*' -e 's*@SBINDIR@*%{_sbindir}*' %{SOURCE1} > %{buildroot}/%{_sysconfdir}/init.d/ndoutils
%{__sed} -e 's*@localstatedir@*%{_localstatedir}*' %{SOURCE2} > %{buildroot}/%{_sysconfdir}/nagios/ndo2db.cfg

%post
/sbin/chkconfig --add ndoutils

%preun
if [ $1 -eq 0 ]; then
    /sbin/service ndoutils stop &>/dev/null || :
    /sbin/chkconfig --del ndoutils
fi


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README REQUIREMENTS TODO UPGRADING config/*
%{_libexecdir}/ndomod-3x.o
%{_sbindir}/ndo2db-3x
%attr(755,root,root) %{_sysconfdir}/init.d/ndoutils
%{_sysconfdir}/nagios/ndo2db.cfg


%changelog
* Tue Dec 30 2008 Christoph Maser <cmr@financial.com> - 1.4-0.beta7.1
- Changed version String so it can be updated by a 1.4 final
- Added init-script
- Added config-file
- Added chkconfig actions  (%post,%preun)

* Thu Nov 06 2008 Christoph Maser <cmr@financial.com> - 1.4b7-0.beta7
- Initial package.
