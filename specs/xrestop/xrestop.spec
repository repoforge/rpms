# $Id$

# Authority: dag

Summary: X resource monitor
Name: xrestop
Version: 0.2
Release: 0
License: GPL
Group: Applications/System
URL: http://www.freedesktop.org/Software/xrestop/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://freedesktop.org/Software/xrestop/xrestop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel ncurses-devel

%description
A utility to monitor the usage of resources within the X Server, and
display them in a manner similar to top.

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
%doc AUTHORS ChangeLog COPYING NEWS README 
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Wed Dec 24 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
