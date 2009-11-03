# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

Summary: Displays access point information in a useful manner
Name: dwscan
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://dag.wieers.com/home-made/dwscan/

Source: http://dag.wieers.com/home-made/dwscan/dwscan-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: /usr/bin/python2
Requires: python >= 2.0, python-wifi >= 0.3

%description
Dwscan displays access point information in a useful manner.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO WISHLIST
%{_sbindir}/dwscan

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Updated to release 0.2.

* Mon Jul 10 2006 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
