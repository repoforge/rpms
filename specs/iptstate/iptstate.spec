# $Id$
# Authority: dag

# ExcludeDist: el4

Summary: Display IP Tables state table information in a "top"-like interface
Name: iptstate
Version: 1.4
Release: 1.2
License: zlib License
Group: Applications/System
URL: http://www.phildev.net/iptstate/

Source: http://www.phildev.net/iptstate/iptstate-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, gcc-c++

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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Wed Sep 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
