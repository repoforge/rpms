# $Id: _template.spec 1587 2004-07-18 22:05:05Z dag $
# Authority: dag

# ExclusiveDist: fc2

%define _sbindir /sbin
%define real_version 0.0.3-2

Summary: Userspace control program for the arptables network filter
Name: arptables
Version: 0.0.3.2
Release: 1
Group: System Environment/Base
License: GPL
URL: http://ebtables.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ebtables/arptables-v%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:  kernel-source >= 2.6.0
Requires: kernel >= 2.6.0

%description
The arptables utility controls the arpfilter network packet
filtering code in the Linux kernel. You do not need this program
for normal network firewalling. If you need to manually control
which arp requests and/or replies this machine accepts and sends,
you should install this package.

%prep
%setup -n %{name}-v%{real_version}

%build
%{__make} %{?_smp_mflags} \
	COPT_FLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0644 arptables.8 %{buildroot}%{_mandir}/man8/arptables.8
%{__install} -D -m0755 arptables %{buildroot}%{_sbindir}/arptables

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/arptables.8*
%{_sbindir}/arptables

%changelog
* Thu Jul 22 2004 Dag Wieers <dag@wieers.com> - 0.0.3.2-1
- Initial package. (using DAR)
