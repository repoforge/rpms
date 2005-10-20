# $Id$
# Authority: dag
# Upstream: 

%define real_name rrdUtils

Summary: Utilities to deal with RRD files and graphs
Name: rrdutils
Version: 3.3
Release: 1
License: El Menda
Group: Applications/Databases

Source: ftp://ftp.rediris.es/rediris/software/rrdUtils/rrdUtils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: rrdUtils <= %{version}-%{release}
BuildArch: noarch
Requires: perl, rrdtool

%description
This is a set of tools intended to help creation and displaying of RRD
files. The RRD characteristics (data sources, consolidation functions)
and the graphs are described in a configuration file that we can use to
create new instances of a RRD, and to generate the graphs for them.

%prep
%setup -n %{real_name}

%build
%configure \
	--with-rrddir="%{_localstatedir}/lib/rrd"

%install
%{__rm} -rf %{buildroot}
%{__make} install install-snmp DESTDIR=%{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/rrd/conf/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc DESCRIPTION EXAMPLES examples.dir snmp-kit/table_db.patch ToDo
%{_bindir}/RRD*
%{_bindir}/*.sh
%{_libdir}/perl5/site_perl/RRDutils.pm
%{_localstatedir}/lib/rrd/

%changelog
* Sat Sep 25 2004 Dag Wieers <dag@wieers.com> - 3.3.5-1
- Initial package. (using DAR)
