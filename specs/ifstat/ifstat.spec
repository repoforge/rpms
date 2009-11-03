# $Id$
# Authority: dag
# Upstream: Gaël Roualland <gael,roualland$iname,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_net_snmp 1}
%{?el2:%define _without_net_snmp 1}
%{?rh6:%define _without_net_snmp 1}

Summary: Interface statistics
Name: ifstat
Version: 1.1
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://gael.roualland.free.fr/ifstat/

Source: http://gael.roualland.free.fr/ifstat/ifstat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_net_snmp:BuildRequires: net-snmp-devel}
%{?_without_net_snmp:BuildRequires: ucd-snmp-devel}

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
%doc %{_mandir}/man1/ifstat.1*
%{_bindir}/ifstat

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 14 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
