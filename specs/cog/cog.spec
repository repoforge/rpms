# $Id$
# Authority: dag
# Upstream: <maxximum@krakoa.dk>

%define _localstatedir %{_var}/lib

Summary: Advanced GNOME configuration editor
Name: cog
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/System
URL: http://www.krakoa.dk/linux-software.html#COG

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.krakoa.dk/progs/cog/cog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0.3, glib2-devel >= 2.0.1, GConf2-devel >= 1.1.11
BuildRequires: libxml2-devel >= 2.4.21

%description
COG is a GNOME configurator program. A program for editing advanced
GNOME settings in an easy way.

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/cog/

%changelog
* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Thu Jul 24 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.5.3-0
- Initial package. (using DAR)
