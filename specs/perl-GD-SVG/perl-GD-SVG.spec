# $Id$
# Authority: dries
# Upstream: Todd Harris <harris$cshl,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GD-SVG

Summary: Seamlessly enable SVG output from scripts written using GD
Name: perl-GD-SVG
Version: 0.32
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GD-SVG/

Source: http://www.cpan.org/modules/by-module/GD/GD-SVG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
GD::SVG seamlessly enables the scalable vector graphics (SVG) output
from scripts written using GD.  It accomplishes this by translating GD
functions into SVG functions.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/GD::SVG.3pm*
%dir %{perl_vendorlib}/GD/
#%{perl_vendorlib}/GD/SVG/
%{perl_vendorlib}/GD/SVG.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Updated to release 0.28.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Updated to release 0.27.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
