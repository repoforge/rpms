# $Id$
# Authority: dries
# Upstream: Criswell <sam$progeny,com>

Summary: Bootstraps rpm-based systems
Name: rpmstrap
Version: 0.5.2
Release: 2%{?dist}
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
DESTDIR="%{buildroot}" LIBDIR="%{buildroot}%{_libdir}/rpmstrap" ./install.sh
%{__ln_s} -f %{_libdir}/rpmstrap/tools/compstool.py %{buildroot}%{_bindir}/compstool.py
%{__ln_s} -f %{_libdir}/rpmstrap/tools/progress_bar.py %{buildroot}%{_bindir}/progress_bar.py
%{__ln_s} -f %{_libdir}/rpmstrap/tools/rpm_get-arch.py %{buildroot}%{_bindir}/rpm_get-arch.py
%{__ln_s} -f %{_libdir}/rpmstrap/tools/rpm_get-update.py %{buildroot}%{_bindir}/rpm_get-update.py
%{__ln_s} -f %{_libdir}/rpmstrap/tools/rpm_migrate.sh %{buildroot}%{_bindir}/rpm_migrate.sh
%{__ln_s} -f %{_libdir}/rpmstrap/tools/rpm_refiner.py %{buildroot}%{_bindir}/rpm_refiner.py
%{__ln_s} -f %{_libdir}/rpmstrap/tools/rpm_solver.py %{buildroot}%{_bindir}/rpm_solver.py
%{__ln_s} -f %{_libdir}/rpmstrap/tools/rpmdiff.py %{buildroot}%{_bindir}/rpmdiff.py
%{__ln_s} -f %{_libdir}/rpmstrap/tools/rpmdiff_lib.py %{buildroot}%{_bindir}/rpmdiff_lib.py
%{__ln_s} -f %{_libdir}/rpmstrap/tools/suite_upgrader.py %{buildroot}%{_bindir}/suite_upgrader.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README TODO
%{_bindir}/compstool.py
%{_bindir}/progress_bar.py
%{_bindir}/rpm_get-arch.py
%{_bindir}/rpm_get-update.py
%{_bindir}/rpm_migrate.sh
%{_bindir}/rpm_refiner.py
%{_bindir}/rpm_solver.py
%{_bindir}/rpmdiff.py
%{_bindir}/rpmdiff_lib.py
%{_bindir}/rpmstrap
%{_bindir}/suite_upgrader.py
%{_libdir}/rpmstrap/

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 0.5.2-2
- Fixed group name.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1
- Updated to release 0.5.2.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
