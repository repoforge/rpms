# $Id$

# Authority: dag

Summary: Wireless sniffer for 802.11 wireless networks.
Name: airtraf
Version: 1.1
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.elixar.com/products/airtraf.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.elixar.com/airtraf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


#BuildRequires: 

%description
AirTraf is a wireless sniffer that can detect and determine exactly what
is being transmitted over 802.11 wireless networks. This open-source
program tracks and identifies legitimate and rogue access points, keeps
performance statistics on a by-user and by-protocol basis, measures the
signal strength of network components, and more.

%prep
%setup

### FIXME: Remove interactive read from Makefile during install
#{__perl} -pi.orig -e 's|^\t\@read|#\t\@read|' src/Makefile

%build
%{__make} %{?_smp_mflags} -C src

%install
%{__rm} -rf %{buildroot}
#makeinstall -C src \
#	INSTALL_DIR="%{buildroot}%{_bindir}"
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 src/airtraf %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Authors COMPATIBILITY COPYING docs/*
%{_bindir}/*

%changelog
* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Updated to release 1.1.
- Initial package. (using DAR)
