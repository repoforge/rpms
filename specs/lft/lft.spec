# $Id$

# Authority: dag

# Upstream: <lft-bugs@mainnerve.com>

Summary: Alternative traceroute tool for network (reverse) engineers.
Name: lft
Version: 2.2
Release: 0
License: MainNerve Public License
Group: Applications/Internet
URL: http://www.mainnerve.com/lft/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://mainnerve.com/lft/%{name}-%{version}.tar.gz
#Patch: %{name}-install.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libpcap
Obsoletes: fft

%description
LFT, short for Layer Four Traceroute, is a sort of 'traceroute' that
often works much faster (than the commonly-used Van Jacobson method) and
goes through many configurations of packet-filter based firewalls. More
importantly, LFT implements numerous other features including AS number
lookups, loose source routing, netblock name lookups, et al.

%prep
%setup
#%patch0 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man8"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README TODO lft-manpage.html
%doc %{_mandir}/man8/*
%attr(4755, -, -) %{_bindir}/*

%changelog
* Thu May 22 2003 Dag Wieers <dag@wieers.com> - 2.2-0
- Updated to release 2.2.

* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 2.1-0
- Initial package. (using DAR)
