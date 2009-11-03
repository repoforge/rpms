# $Id$

# Authority: dries

%define real_version 0.3-beta15

Summary: Display the temperature of harddisks
Name: hddtemp
Version: 0.3
Release: 0.beta15.1%{?dist}
License: GPL
Group: Applications/System
URL: http://coredump.free.fr/linux/hddtemp.php

Source: http://www.guzu.net/files/hddtemp-%{real_version}.tar.bz2
Source1: http://www.guzu.net/linux/hddtemp.db
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires:

%description
hddtemp is a small utility that gives you the temperature of your hard drive
by reading S.M.A.R.T. informations (for drives that support this feature).
Note: only recent hard drives have a temperature sensor.

%prep
%setup -n hddtemp-%{real_version}

%build
%configure --with-db-path=%{_datadir}/hddtemp/hddtemp.db
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/hddtemp/hddtemp.db
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_sbindir}/hddtemp
%{_datadir}/hddtemp

%changelog
* Sat Apr 28 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-0.beta15.1
- Updated to release 0.3-0.beta15.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-0.beta14.1.2
- Rebuild for Fedora Core 5.

* Sun Oct 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-0.beta14.1
- Update to release 0.3-0.beta14.

* Tue Mar 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-0.beta12.2
- Update of the hddtemp database.

* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.3-0.beta12
- Update to release 0.3-beta12.

* Tue Jul 27 2004 Dries Verachtert <dries@ulyssis.org> - 0.3-0.beta11
- Initial package.
