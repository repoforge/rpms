# $Id$

# Authority: dag

# Upstream: Gaël Roualland <gael.roualland@iname.com>

Summary: Interface statistics.
Name: ifstat
Version: 1.0
Release: 0
License: GPL
Group: System Environment/Base
URL: http://gael.roualland.free.fr/ifstat/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://gael.roualland.free.fr/ifstat/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%{?rhel3:BuildRequires: net-snmp-devel}
%{?rh90:BuildRequires: net-snmp-devel}
%{?rh80:BuildRequires: net-snmp-devel}
%{?rh73:BuildRequires: ucd-snmp-devel}
%{?rhel21:BuildRequires: ucd-snmp-devel}
%{?rh62:BuildRequires: ucd-snmp-devel}

%description
ifstat(1) is a little tool to report interface activity like vmstat/iostat do.
In addition, ifstat can poll remote hosts through SNMP if you have the ucd-snmp
library. It will also be used for localhost if no other known method works (You
need to have snmpd running for this though).

%prep
%setup

%build
%configure \
	--enable-optim
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING HISTORY README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
