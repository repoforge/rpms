# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Judd Vinet <jvinet$zeroflux,org>

# Distcc: 0

Summary: Port-knocking server
Name: knock
Version: 0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.zeroflux.org/knock/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.zeroflux.org/knock/knock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 

%description
knockd is a port-knock server. It listens to all traffic on an ethernet
interface, looking for special "knock" sequences of port-hits. A client
makes these port-hits by sending a TCP (or UDP) packet to a port on the
server. This port need not be open -- since knockd listens at the link-
layer level, it sees all traffic even if it's destined for a closed port.

When the server detects a specific sequence of port-hits, it runs a
command defined in its configuration file. This can be used to open up
holes in a firewall for quick access.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
