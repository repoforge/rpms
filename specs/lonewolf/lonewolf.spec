# $Id: $

# Authority: dries
# Upstream: 

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

BuildRequires: gcc-c++, ncurses-devel

%description
LoneWolf is a free open source emulator for the Ultima Online server. It
allows you to play UO on a single machine, in a LAN or on the internet.

LoneWolf was derived from Wolfpack 12.6, which was derived from UOX-pi,
which in turn was derived from UOX3 V69.xx, which in turn ....Well,
everything started with Cironian who created the first emulator back in
1997.

%prep
%setup -n source_of_lonejoy/src

%build
sed -i 's/\-pipe/-Wall -ggdb -pipe/g;' Makefile
sed -i 's/\-L/-lncurses -ggdb -Wall -L/g;' Makefile
sed -i 's/HEADERS =/HEADERS = timers.h /g;' Makefile
sed -i 's/SOURCES =/SOURCES = timers.cpp /g;' Makefile
sed -i 's/OBJECTS =/OBJECTS = timers.o /g;' Makefile
%{__make} LDFLAGS="-lncurses -ggdb -Wall" %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp lonewolf %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/lonewolf
tar -C %{buildroot}/usr/share/lonewolf -xjvf %{SOURCE1}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/lonewolf

%changelog
* Tue Mar 30 2004 Dries Verachtert 13.0.9-1
- initial packaging
