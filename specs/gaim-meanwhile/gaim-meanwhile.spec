# $Id: _template.spec 765 2004-05-20 17:33:53Z dag $
# Authority: dag
# Upstream: Christopher O'Brien <siege@preoccupied.net>

%define real_name meanwhile-gaim

Summary: Lotus Sametime Community Client plugin for Gaim
Name: gaim-meanwhile
Version: 0.79
Release: 1
License: GPL
Group: Applications/Internet
URL: http://meanwhile.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/meanwhile/meanwhile-gaim-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Obsoletes: meanwhile-gaim <= %{version}
Requires: gaim, meanwhile >= 0.3

%description
Lotus Sametime Community Client plugin for Gaim

%prep
%setup -n %{real_name}-%{version}

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
%{_libdir}/gaim/*.so
%exclude %{_libdir}/gaim/*.a
%exclude %{_libdir}/gaim/*.la
%{_datadir}/pixmaps/gaim/

%changelog
* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 0.79-1
- Updated to releas 0.79.

* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.78-1
- Initial package. (using DAR)
