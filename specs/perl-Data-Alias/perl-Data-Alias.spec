# $Id$
# Authority: dries
# Upstream: Matthijs van Duin <xmath$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Alias

Summary: Comprehensive set of aliasing operations
Name: perl-Data-Alias
Version: 1.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Alias/

Source: http://www.cpan.org/modules/by-module/Data/Data-Alias-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.1

%description
Comprehensive set of aliasing operations.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Data::Alias.3pm*
%dir %{perl_vendorarch}/Data/
%{perl_vendorarch}/Data/Alias.pm
%dir %{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/auto/Data/Alias/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
