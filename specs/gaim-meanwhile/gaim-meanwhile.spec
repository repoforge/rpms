# $Id$
# Authority: dag
# Upstream: Christopher O'Brien <siege$preoccupied,net>

Summary: Lotus Sametime Community Client plugin for Gaim
Name: gaim-meanwhile
Version: 1.0.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://meanwhile.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/meanwhile/gaim-meanwhile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim >= %{version}, meanwhile-devel >= 0.3
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
%exclude %{_libdir}/gaim/libmwgaim.la
%{_datadir}/pixmaps/gaim/

%changelog
* Thu Nov 18 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Oct 31 2004 Dag Wieers <dag@wieers.com> - 1.0.1-2
- Build against gaim 1.0.2.

* Sun Oct 17 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Thu Sep 23 2004 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0 .

* Fri Aug 27 2004 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Mon Aug 16 2004 Dag Wieers <dag@wieers.com> - 0.81-1
- Updated to release 0.81.

* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated to release 0.80.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 0.79-1
- Updated to release 0.79.

* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.78-1
- Initial package. (using DAR)
