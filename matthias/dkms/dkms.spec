# Authority: dag

Summary: Dynamic Kernel Module Support.
Name: dkms
Version: 0.31.04
Release: 0
Group: System Environment/Kernel
License: GPL
URL: http://www.lerhaupt.com/linux.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.lerhaupt.com/dkms/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#BuildRequires: 

%description
DKMS stands for Dynamic Kernel Module Support. It is designed to create
a framework where kernel dependant module source can reside so that it
is very easy to rebuild modules as you upgrade kernels. This will allow
Linux vendors to provide driver drops without having to wait for new
kernel releases while also taking out the guesswork for customers
attempting to recompile modules for new kernels. 

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_sysconfdir} \
			%{buildroot}%{_localstatedir}/dkms \
			%{buildroot}%{_mandir}/man8
%{__install} -m0755 dkms %{buildroot}%{_sbindir}
%{__install} -m0644 dkms_framework.conf %{buildroot}%{_sysconfdir}
%{__install} -m0644 dkms.8.gz %{buildroot}%{_mandir}/man8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING sample.spec
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/*
%{_sbindir}/*
%{_localstatedir}/dkms/

%changelog
* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.31.04-0
- Initial package. (using DAR)
