# $Id$
# Authority: dag

%define real_version 2004.07.30

Summary: I/O subsystem measurement and characterization tool
Name: iometer
Version: 0.0.20040730
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.iometer.org/

Source: http://dl.sf.net/iometer/iometer-%{real_version}.common-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
ExclusiveArch: i386 ppc

%description
Iometer is an I/O subsystem measurement and characterization tool for
single and clustered systems.

%prep
%setup -n %{name}-%{real_version}

%build
%{__make} %{?_smp_mflags} -C src -f Makefile-Linux.%{_arch} all

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/dynamo %{buildroot}%{_bindir}/dynamo

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG DEVGUIDE LICENSE README src/ccnt/ src/iomtr_kstat/
%{_bindir}/dynamo

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.20040730-1.2
- Rebuild for Fedora Core 5.

* Sat Aug 28 2004 Dag Wieers <dag@wieers.com> - 0.0.20040730-1
- Initial package. (using DAR)
