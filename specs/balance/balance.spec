# Authority: dag

Summary: TCP load-balancing proxy server.
Name: balance
Version: 3.11
Release: 0
License: GPL
Group: Applications/Internet
URL: http://balance.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/balance/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Balance is a simple but powerful generic tcp proxy with round robin
load balancing and failover mechanisms. Its behaviour can be controlled
at runtime using a simple command line syntax. 

%prep
%setup 

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"
	
%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man1
%{__install} -d -m1777 %{buildroot}%{_localstatedir}/run/balance/
%{__install} -m0755 balance %{buildroot}%{_sbindir}
%{__install} -m0644 balance.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_localstatedir}/run/balance/

%changelog
* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 3.11-0
- Updated to release 3.11.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 3.6-0
- Initial package. (using DAR)
