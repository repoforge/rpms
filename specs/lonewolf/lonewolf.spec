# $Id$
# Authority: dries

%define real_version cvs20040503

Summary: Ultima Online emulator
Name: lonewolf
Version: 1.0
Release: 0.%{real_version}.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://home1.tiscalinet.de/aduke/main2/news2.htm

Source: lonewolf-%{version}-%{real_version}.tar.bz2
Source1: lwscripts-%{version}-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, ncurses-devel

%description
LoneWolf is a free open source emulator for the Ultima Online server. It
allows you to play UO on a single machine, in a LAN or on the internet.

LoneWolf was derived from Wolfpack 12.6, which was derived from UOX-pi,
which in turn was derived from UOX3 V69.xx, which in turn ....Well,
everything started with Cironian who created the first emulator back in
1997.

The server should be run as user 'lonewolf'.

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

%pre
useradd -d %{_datadir}/lonewolf/lwscripts -c "Lonewolf Ultima Online Server" lonewolf &>/dev/null || :

%postun
userdel lonewolf &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%{_bindir}/lonewolf
%exclude %{_datadir}/lonewolf/lwscripts/CVS
%exclude %{_datadir}/lonewolf/lwscripts/rewrite/CVS

%{_datadir}/lonewolf/lwscripts/ReadMe.txt
%{_datadir}/lonewolf/lwscripts/Script_Updates.txt
%{_datadir}/lonewolf/lwscripts/dummy.txt
%{_datadir}/lonewolf/lwscripts/install.html
%{_datadir}/lonewolf/lwscripts/shards_server.smp

%defattr(-, lonewolf, lonewolf, 0755)
%config(noreplace)  %{_datadir}/lonewolf/lwscripts/*.scp
%config(noreplace)  %{_datadir}/lonewolf/lwscripts/inscribe.gmp
%config(noreplace)  %{_datadir}/lonewolf/lwscripts/rewrite/*.scp
%config(noreplace)  %{_datadir}/lonewolf/lwscripts/sample-accounts.adm


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-0.%{real_version}.2
- Rebuild for Fedora Core 5.

* Tue Mar 30 2004 Dries Verachtert 13.0.9-1
- initial packaging
