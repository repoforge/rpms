# $Id$

# Authority: dag

%define rversion 1.1a

Summary: Print average throughput for a tcp connection
Name: tcpspray
Version: 1.1
Release: 0.a
License: Unknown
Group: Applications/Internet

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{name}.%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Print average throughput for a tcp connection.

%prep
%setup -n %{name}
%build
%{__make} %{?_smp_mflags} \
	LDFLAGS="-s"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 tcpspray %{buildroot}%{_bindir}
%{__install} -m0644 tcpspray.1 %{buildroot}%{_mandir}/man1/

%files
%defattr(-, root, root, 0755}
%doc %{_mandir}/man?/*
%{_bindir}/*

%clean
%{__rm} -rf %{buildroot}

%changelog
* Wed Nov 26 2003 Dag Wieers <dag@wieers.com> - 1.1-0.a
- Repackaged using DAR.

* Sun Jan 30 2000 Dag Wieers <dag@mind.be> - 1.1a-0
- Initial package.
