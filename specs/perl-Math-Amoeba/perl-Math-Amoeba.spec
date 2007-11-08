# $Id$
# Authority: dries
# Upstream: John A.R. Williams <J,A,R,Williams$aston,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Amoeba

Summary: Multidimensional Function Minimisation
Name: perl-Math-Amoeba
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Amoeba/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOM/Math-Amoeba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Multidimensional Function Minimisation.

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
%doc README
%doc %{_mandir}/man3/Math::Amoeba*
%{perl_vendorlib}/Math/Amoeba.pm

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Updated to release 0.02.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
