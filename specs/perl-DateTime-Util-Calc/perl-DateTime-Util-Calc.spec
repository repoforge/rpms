# $Id$

# Authority: dries
# Upstream: Daisuke Maki <dmaki$cpan,org>

%define real_name DateTime-Util-Calc
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: DateTime calculation utilities 
Name: perl-DateTime-Util-Calc
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Util-Calc/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/DateTime-Util-Calc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build, perl-Math-BigInt-GMP
BuildRequires: perl(Math::Round), perl(DateTime)

%description
A perl module with additional DateTime calculation utilities.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Util/Calc.pm

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Initial package.
