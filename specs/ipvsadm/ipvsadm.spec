# $Id$
# Authority: dag

%define _sbindir /sbin

Summary: Utility to administer the Linux Virtual Server
Name: ipvsadm
Version: 1.21
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.LinuxVirtualServer.org/

Source: http://www.LinuxVirtualServer.org/software/ipvsadm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Conflicts: piranha <= 0.4.14

%description
ipvsadm is a utility to administer the IP Virtual Server services
offered by the Linux kernel augmented with the IP Virtual Server patch.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BUILD_ROOT="%{buildroot}" \
	MANDIR="%{_mandir}" \
	INIT="%{buildroot}%{_initrddir}"

%post
/sbin/chkconfig --add ipvsadm

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del ipvsadm
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%config %{_initrddir}/*
%{_sbindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.21-0.2
- Rebuild for Fedora Core 5.

* Fri Jun 07 2003 Dag Wieers <dag@wieers.com> - 1.21-0
- Initial package. (using DAR)
