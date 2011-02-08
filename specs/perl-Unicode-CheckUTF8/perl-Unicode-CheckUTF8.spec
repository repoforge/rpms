# $Id$
# Authority: dries
# Upstream: Brad Fitzpatrick <brad$danga,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-CheckUTF8

Summary: Check if a scalar is valid UTF-8
Name: perl-Unicode-CheckUTF8
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-CheckUTF8/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/Unicode-CheckUTF8-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can check if a scalar is valid UTF-8.

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
%doc CHANGES
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/CheckUTF8.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/CheckUTF8/

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.03-1
- Updated to version 1.03.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
