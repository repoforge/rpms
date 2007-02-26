# $Id$
# Authority: dag
# Upstream: <lft$oppleman,com>

%{?dist: %{expand: %%define %dist 1}}

%{!?dist:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Alternative traceroute tool for network (reverse) engineers
Name: lft
Version: 2.5
Release: 1
License: MainNerve Public License
Group: Applications/Internet
URL: http://oppleman.com/lft/

Source: http://pwhois.org/dl/index.who?file=lft-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

Obsoletes: fft

%description
LFT, short for Layer Four Traceroute, is a sort of 'traceroute' that
often works much faster (than the commonly-used Van Jacobson method) and
goes through many configurations of packet-filter based firewalls. More
importantly, LFT implements numerous other features including AS number
lookups, loose source routing, netblock name lookups, et al.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	DESTDIR="%{buildroot}%{_bindir}" \
	MANDIR="%{buildroot}%{_mandir}/man8"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README TODO
%doc %{_mandir}/man8/lft.8*
%doc %{_mandir}/man8/whob.8*
%{_bindir}/whob
%defattr(4755, root, root, 0755)
%{_bindir}/lft

%changelog
* Sat Apr 29 2006 Dag Wieers <dag@wieers.com> - 2.5-1
- Updated to release 2.5.

* Fri Jan 14 2005 Dag Wieers <dag@wieers.com> - 2.3-1
- Updated to release 2.3.

* Thu May 22 2003 Dag Wieers <dag@wieers.com> - 2.2-0
- Updated to release 2.2.

* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 2.1-0
- Initial package. (using DAR)
