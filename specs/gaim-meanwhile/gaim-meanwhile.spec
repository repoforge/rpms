# $Id$
# Authority: dag
# Upstream: Christopher O'Brien <siege$preoccupied,net>

Summary: Lotus Sametime Community Client plugin for Gaim
Name: gaim-meanwhile
Version: 0.81
Release: 1
License: GPL
Group: Applications/Internet
URL: http://meanwhile.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/meanwhile/gaim-meanwhile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: gaim >= %{version}, meanwhile >= 0.3
Obsoletes: meanwhile-gaim <= %{version}

%description
Lotus Sametime Community Client plugin for Gaim

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/gaim/libmwgaim.so
%exclude %{_libdir}/gaim/libmwgaim.a
%exclude %{_libdir}/gaim/libmwgaim.la
%{_datadir}/pixmaps/gaim/

%changelog
* Mon Aug 16 2004 Dag Wieers <dag@wieers.com> - 0.81-1
- Updated to releas 0.81.

* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated to releas 0.80.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 0.79-1
- Updated to releas 0.79.

* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.78-1
- Initial package. (using DAR)
