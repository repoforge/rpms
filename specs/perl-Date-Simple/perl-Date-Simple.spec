# $Id$
# Authority: dries
# Upstream: Yves <yves$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Simple

Summary: Simple date object
Name: perl-Date-Simple
Version: 3.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Simple/

Source: http://www.cpan.org/modules/by-module/Date/Date-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Dates are complex enough without times and timezones. This module may be
used to create simple date objects.

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
%doc ChangeLog README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Date/
%{perl_vendorarch}/Date/Simple/
%{perl_vendorarch}/Date/Simple.pm
%dir %{perl_vendorarch}/auto/Date/
%{perl_vendorarch}/auto/Date/Simple/

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 3.03-1
- Updated to version 3.03.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 3.02-1
- Initial package.
