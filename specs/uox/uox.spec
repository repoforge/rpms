# $Id: $

# Authority: dries
# Upstream:

Summary: Ultima online server
Name: uox
Version: 0.97.6.9r
%define mozilla_version 1.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.uox3.org/

Source: http://www.uox3.org/files/uox3-source.zip
Source1: ftp://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla%{mozilla_version}/src/mozilla-source-%{mozilla_version}.tar.bz2
Source2: http://www.xoduz.org/files/uox3/uox3.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dos2unix, autoconf, automake, gcc-c++, unzip

%description
UOX3 stands for Ultima Offline eXperiment(remake 3). It is a server emulator
for OSI's Ultima Online Server, originally created by Marcus Rating. This
server emulator enables you to create your own server and play on it either
locally, over modem, LAN or the internet at least 32 people at a time.

%prep
%setup -c

%build
tar xjvf %{SOURCE1} mozilla/js
cd ./mozilla/js/src/fdlibm;
gcc -c -DXP_UNIX *.c
cd ..
gcc -o jscpucfg jscpucfg.c ; ./jscpucfg >  jsautocfg.h
gcc -c -DXP_UNIX *.c ; ar -r js32.a *.o fdlibm/*.o
cp js32.a ../../../
cd ../../../
dos2unix Makefile.am
aclocal
automake --add-missing --copy || echo automake --add-missing --copy gives a warning
autoconf
automake || echo automake gives a warning
chmod +x configure
%configure --enable-debug
dos2unix Makefile
dos2unix depcomp
%{__make} INCLUDES=-I/usr/include/mozilla-1.6/js %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share
cp uox3 %{buildroot}/usr/bin
cd %{buildroot}/usr/share
unzip %{SOURCE2}
mv UOX3 uox3

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog.txt COPYING INSTALLINSTALL NEWS README README.Linux readme.txt
%{_bindir}/uox3

%changelog
* Fri Apr 30 2004 Dries Verachtert <dries@ulyssis.org> 0.97.6.9r-1
- initial package
