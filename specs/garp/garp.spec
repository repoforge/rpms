# $Id$

# Authority: dag

# Upstream: Ulrik De Bie <ulrik@mind.be>

Summary: Check unused IP addresses and automagically assign them.
Name: garp
Version: 0.7.2
Release: 1
License: GPL
Group: System Environment/Base
URL: http://garp.3va.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://garp.3va.net/down/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Garp is a Gratuitous ARP implementation. Garp can be used to check
for unused IP addresses and automagically (and randomly) assign
unused IP addresses (from a given IP range).

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man8
%{__install} -m0755 garp %{buildroot}%{_sbindir}
%{__install} -m0644 garp.8 %{buildroot}%{_mandir}/man8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_sbindir}/garp
%{_mandir}/man?/*

%changelog 
* Thu May 01 2003 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Changed URL: and Source: to http://garp.3va.net/

* Sun Nov 21 1999 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Updated to release 0.7.2.
- Changed URL: and Source: to http://mind.be/software/garp/

* Fri Nov 19 1999 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Mon Nov 15 1999 Ulrik De Bie <ulrik@mind.be>
- Initial release.
