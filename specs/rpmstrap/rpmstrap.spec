# $Id$
# Authority: dries
# Upstream: Criswell <sam$progeny,com>

Summary: Bootstraps rpm-based systems
Name: rpmstrap
Version: 0.5.2
Release: 2
License: GPL
Group: Development/Tools
URL: http://hackers.progeny.com/~sam/rpmstrap/

Source: http://hackers.progeny.com/~sam/rpmstrap/releases/rpmstrap-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Buildarch: noarch

%description
rpmstrap is a tool for bootstrapping a basic RPM-based system. It is inspired
by debootstrap, and allows you to build chroots and basic systems from RPM
sources.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
DESTDIR=%{buildroot} bash install.sh
%{__rm} -f %{buildroot}%{_bindir}/rpm_get-arch.py
%{__rm} -f %{buildroot}%{_bindir}/rpm_refiner.py
%{__rm} -f %{buildroot}%{_bindir}/rpm_solver.py
%{__ln_s} %{_libdir}/rpmstrap/tools/rpm_get-arch.py %{buildroot}%{_bindir}/rpm_get-arch.py
%{__ln_s} %{_libdir}/rpmstrap/tools/rpm_refiner.py %{buildroot}%{_bindir}/rpm_refiner.py
%{__ln_s} %{_libdir}/rpmstrap/tools/rpm_solver.py %{buildroot}%{_bindir}/rpm_solver.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README TODO
%{_bindir}/rpm_get-arch.py
%{_bindir}/rpm_refiner.py
%{_bindir}/rpm_solver.py
%{_bindir}/rpmstrap
%{_libdir}/rpmstrap
%{_bindir}/compstool.py
%{_bindir}/progress_bar.py
%{_bindir}/rpm_get-update.py
%{_bindir}/rpm_migrate.sh
%{_bindir}/rpmdiff.py
%{_bindir}/rpmdiff_lib.py
%{_bindir}/suite_upgrader.py

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 0.5.2-2
- Fixed group name.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1
- Updated to release 0.5.2.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
