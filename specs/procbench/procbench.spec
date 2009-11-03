# $Id$
# Authority: dag
# Upstream: 

Summary: CPU benchmark and information tool
Name: procbench
Version: 0.7.3a
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://procbench.sourceforge.net/

Source: http://dl.sf.net/procbench/procbench-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
procbench is a multiplatform information tool and CPU benchmark for x86
processors. It tests memory transfer and math capabilities of your x86
processor. Pb_g++ and Pb_gcc programs are also included. They gets the
best GCC optimisation parameters for that CPU (linux only).

%prep
%setup

%build
#%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%{_bindir}/pb_g++
%{_bindir}/pb_gcc
%{_bindir}/procbench
%{_datadir}/procbench/

%changelog
* Sun Sep 23 2007 Dag Wieers <dag@wieers.com> - 0.7.3a-1
- Initial package. (using DAR)
