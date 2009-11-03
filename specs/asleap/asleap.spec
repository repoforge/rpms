# $Id$
# Authority: dag
# Upstream: Joshua Wright <jwright$hasborg,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Recover weak LEAP and PPTP passwords
Name: asleap
Version: 1.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://asleap.sourceforge.net/

Source: http://dl.sf.net/asleap/asleap-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap >= 14:0.8
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
asleap is a tool to recover weak LEAP and PPTP passwords. asleap is the
product of the research of weaknesses in Cisco's proprietary LEAP protocol.

asleap can work directly from any wireless interface in RFMON mode and can
perform channel hopping.

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 asleap %{buildroot}%{_sbindir}/asleap
%{__install} -Dp -m0755 genkeys %{buildroot}%{_sbindir}/genkeys

%{__rm} -rf scripts/CVS/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING FEATURES INSTALL README THANKS TODO scripts/
%{_sbindir}/asleap
%{_sbindir}/genkeys

%changelog
* Tue Dec 21 2004 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
