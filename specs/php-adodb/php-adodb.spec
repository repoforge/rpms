# $Id$
# Authority: dag
# Upstream:

%define real_name adodb
%define real_version 422

Summary: Portable Database Library for PHP
Name: php-adodb
Version: 4.22
Release: 1
License: BSD or LGPL
Group: Development/Languages
URL: http://php.weblogs.com/adodb/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://phplens.com/lens/dl/adodb%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: php >= 4.0.5
Requires: webserver, php >= 4.0.5
Obsoletes: adodb
Provides: adodb

%description
ADOdb stands for Active Data Objects Data Base. It currently support MySQL,
PostgreSQL, Interbase, Informix, Oracle, MS SQL 7, Foxpro, Access, ADO,
Sybase, DB2 and generic ODBC.

%prep
%setup -n %{real_name}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/adodb/{datadict,drivers,lang,perf,session,tests,xsl}/
%{__install} -m0644 *.php *.dtd %{buildroot}%{_localstatedir}/www/adodb/
%{__install} -m0644 datadict/*.php %{buildroot}%{_localstatedir}/www/adodb/datadict/
%{__install} -m0644 drivers/*.php %{buildroot}%{_localstatedir}/www/adodb/drivers/
%{__install} -m0644 lang/*.php %{buildroot}%{_localstatedir}/www/adodb/lang/
%{__install} -m0644 perf/*.php %{buildroot}%{_localstatedir}/www/adodb/perf/
%{__install} -m0644 session/*.php %{buildroot}%{_localstatedir}/www/adodb/session/
%{__install} -m0644 tests/*.php %{buildroot}%{_localstatedir}/www/adodb/tests/
%{__install} -m0644 xsl/*.xsl %{buildroot}%{_localstatedir}/www/adodb/xsl/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt cute_icons_for_site/ docs/*.htm tests/
%{_localstatedir}/www/adodb/

%changelog
* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 4.22-1
- Updated to release 4.22.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 4.21-1
- Updated to release 4.21.

* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 4.20-0
- Updated to release 4.20.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 3.70-0
- Updated to release 3.70.

* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 2.90-0
- Initial package. (using DAR)
