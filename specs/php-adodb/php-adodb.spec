# $Id$
# Authority: dag

%define real_name adodb

Summary: Portable Database Library for PHP
Name: php-adodb
%define real_version 481
Version: 4.81
Release: 1%{?dist}
License: BSD or LGPL
Group: Development/Languages
URL: http://adodb.sourceforge.net/

Source: http://dl.sourceforge.net/adodb/adodb%{real_version}.tgz
#Source: http://phplens.com/lens/dl/adodb%{real_version}.tgz
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
%{__install} -p -m0644 *.php *.dtd %{buildroot}%{_localstatedir}/www/adodb/
%{__install} -p -m0644 datadict/*.php %{buildroot}%{_localstatedir}/www/adodb/datadict/
%{__install} -p -m0644 drivers/*.php %{buildroot}%{_localstatedir}/www/adodb/drivers/
%{__install} -p -m0644 lang/*.php %{buildroot}%{_localstatedir}/www/adodb/lang/
%{__install} -p -m0644 perf/*.php %{buildroot}%{_localstatedir}/www/adodb/perf/
%{__install} -p -m0644 session/*.php %{buildroot}%{_localstatedir}/www/adodb/session/
%{__install} -p -m0644 tests/*.php %{buildroot}%{_localstatedir}/www/adodb/tests/
%{__install} -p -m0644 xsl/*.xsl %{buildroot}%{_localstatedir}/www/adodb/xsl/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt cute_icons_for_site/ docs/*.htm tests/
%{_localstatedir}/www/adodb/

%changelog
* Mon May 08 2006 Dag Wieers <dag@wieers.com> - 4.81-1
- Updated to release 4.81.

* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 4.65-1
- Updated to release 4.65. (Richard Cochius)

* Sat Feb 12 2005 Dag Wieers <dag@wieers.com> - 4.60-1
- Updated to release 4.60.

* Fri Nov 05 2004 Dag Wieers <dag@wieers.com> - 4.52-1
- Updated to release 4.52.

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
