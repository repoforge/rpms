# $Id$

# Authority: dag

%define rversion 1.0

Summary: 68k Macintosh emulator
Name: BasiliskII
Version: 0.9.20020115
Release: 0
License: GPL
Group: Applications/Emulators
URL: http://www.uni-mainz.de/~bauec002/B2Main.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://iphcip1.physik.uni-mainz.de/~cbauer/BasiliskII_src_15012002.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk+-devel >= 1.2, esound-devel >= 0.2.8

%description
Basilisk II is an Open Source 68k Macintosh emulator. That is, it enables
you to run 68k MacOS software on you computer, even if you are using a
different operating system. However, you still need a copy of MacOS and
a Macintosh ROM image to use Basilisk II.

%prep
%setup -n %{name}-%{rversion}

%build
cd src/Unix
#{?rh80: export CC=gcc296; export CXX=g++296}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src/Unix
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README TECH TODO
%doc %{_mandir}/man1/*
%config %{_datadir}/BasiliskII/keycodes
%config %{_datadir}/BasiliskII/fbdevices
%{_bindir}/*

%changelog
* Sat Feb 15 2003 Dag Wieers <dag@wieers.com> - 0.8.20000130
- Initial package. (using DAR)
