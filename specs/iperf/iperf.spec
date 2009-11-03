# $Id$
# Authority: dag
# Upstream: <iperf-users$dast,nlanr,net>

Summary: Tool for measuring TCP and UDP bandwidth performance
Name: iperf
Version: 2.0.4
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
#URL: http://dast.nlanr.net/Projects/Iperf/
URL: http://iperf.sourceforge.net/

#Source: http://dast.nlanr.net/Projects/Iperf2.0/iperf-%{version}.tar.gz
Source: http://dl.sf.net/iperf/iperf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libstdc++-devel

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning
of various parameters and UDP characteristics. Iperf reports bandwidth,
delay jitter, datagram loss.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall -C src INSTALL_DIR="%{buildroot}%{_bindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*.gif doc/*.html README
%{_bindir}/iperf

%changelog
* Mon Apr 28 2008 Dag Wieers <dag@wieers.com> - 2.0.4-1
- Updated to release 2.0.4.
- Removed patch from Ingo Molnar, accepted upstream.

* Thu Sep 27 2007 Dag Wieers <dag@wieers.com> - 2.0.2-2
- Added Ingo Molnar's noyield patch.

* Sun Sep 18 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.2-1
- Updated to release 2.0.2.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Updated to release 2.0.1.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 1.7.0-1
- Initial package. (using DAR)
