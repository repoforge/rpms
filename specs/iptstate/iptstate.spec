# $Id$
# Authority: axel

Summary: Display IP Tables state table information in a "top"-like interface
Name: iptstate
Version: 1.3
Release: 0
License: zlib License
Group: Applications/System
URL: http://iptstate.phildev.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://iptstate.phildev.net/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: ncurses-devel

%description
IP Tables State (iptstate) was originally written to
impliment the "state top" feature of IP Filter.
"State top" displays the states held by your stateful 
firewall in a "top"-like manner.

%prep
%setup

%{__perl} -pi.orig -e 's|^(CXXFLAGS .*)$|$1 %{optflags}|' Makefile

%build
%{__make} %{?_smp_mflags} \
	CXXFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changelog CONTRIB LICENSE README WISHLIST
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
