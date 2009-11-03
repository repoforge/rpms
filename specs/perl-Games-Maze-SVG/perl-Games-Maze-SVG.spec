# $Id$
# Authority: dries
# Upstream: G. Wade Johnson <wade$anomaly,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Games-Maze-SVG

Summary: Converts mazes to SVG
Name: perl-Games-Maze-SVG
Version: 0.75
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Games-Maze-SVG/

Source: http://www.cpan.org/modules/by-module/Games/Games-Maze-SVG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is an extension to the Games::Maze module. Games::Maze::SVG
takes the mazes created by Games::Maze and converts them into an SVG
output. As an option, the SVG version of the maze can be made playable.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Games/Maze/SVG.pm
%{perl_vendorlib}/Games/Maze/SVG/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.75-1
- Updated to release 0.75.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.71-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.71-1
- Initial package.
