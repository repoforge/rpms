# Authority: dag

Summary: A simple TCP benchmarking utility.
Name: gensink
Version: 4.1
Release: 0
License: GPL
Group: Applications/Internet
URL: http://jes.home.cern.ch/jes/gensink/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://home.cern.ch/~jes/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
gensink consists of a pair of utilities that measure the performance of
a TCP connection between two hosts.

%prep
%setup 
 
%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} gen4 sink4 tub4 %{buildroot}%{_sbindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_sbindir}/*

%changelog
* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 4.1-0
- Initial package. (using DAR)
