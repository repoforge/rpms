# $Id$

# Authority: dag

Summary: Useful things common to building gnome packages
Name: gnome-common
Version: 1.2.4
Release: 0
License: GPL
Group: Development/Tools
URL: http://developer.gnome.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-common/1.2/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: pkgconfig

%description
This package contains sample files that should be used to develop pretty much
every GNOME application.

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

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/aclocal/*

%changelog
* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 1.2.4-0
- Initial package. (using DAR)
