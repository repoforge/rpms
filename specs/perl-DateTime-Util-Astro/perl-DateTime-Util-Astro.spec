# $Id$

# Authority: dries
# Upstream: Daisuke Maki <dmaki@cpan.org>

%define real_name DateTime-Util-Astro
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Astronomical Calendar Calculations
Name: perl-DateTime-Util-Astro
Version: 0.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Util-Astro/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/DateTime-Util-Astro-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl

%description
This module contains functions for astronomical calendar calculations.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Util/Astro/*.pm

%changelog
* Sun Dec 05 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
