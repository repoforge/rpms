# $Id$
# Authority: dag

Summary: Simple TCP benchmarking utility
Name: gensink
Version: 4.1
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://jes.home.cern.ch/jes/gensink/

Source: http://home.cern.ch/~jes/gensink-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
gensink consists of a pair of utilities that measure the performance of
a TCP connection between two hosts.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 gen4 %{buildroot}%{_sbindir}/gen4
%{__install} -Dp -m0755 sink4 %{buildroot}%{_sbindir}/sink4
%{__install} -Dp -m0755 tub4 %{buildroot}%{_sbindir}/tub4

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_sbindir}/gen4
%{_sbindir}/sink4
%{_sbindir}/tub4

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.1-0.2
- Rebuild for Fedora Core 5.

* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 4.1-0
- Initial package. (using DAR)
