# $Id: $

# Authority: dries

Summary: Ultima Online emulator
Name: lonewolf
Version: cvs20040503
Release: 1
License: GPL
Group: Applications/Internet
URL: http://home1.tiscalinet.de/aduke/main2/news2.htm
Source: lonewolf-%{version}.tar.bz2
Source1: lwscripts-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
LoneWolf is a free open source emulator for the Ultima Online server. It
allows you to play UO on a single machine, in a LAN or on the internet.

LoneWolf was derived from Wolfpack 12.6, which was derived from UOX-pi,
which in turn was derived from UOX3 V69.xx, which in turn ....Well,
everything started with Cironian who created the first emulator back in
1997.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README

%changelog
* Tue Mar 30 2004 Dries Verachtert 13.0.9-1
- initial packaging
