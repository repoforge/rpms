# $Id$

# Authority: dries
# Upstream: Daisuke Maki <dmaki@cpan.org>

%define real_name DateTime-Util-Astro
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Astronomical Calendar Calculations
Name: perl-DateTime-Util-Astro
Version: 0.06
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Util-Astro/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Util-Astro-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
This module contains functions for astronomical calendar calculations.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} \
	%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Util/Astro

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Sun Dec 05 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
