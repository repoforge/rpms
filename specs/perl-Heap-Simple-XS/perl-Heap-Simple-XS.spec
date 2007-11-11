# $Id$
# Authority: dries
# Upstream: Ton Hospel <cpan$ton,iguana,be>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Heap-Simple-XS

Summary: XS implementation of Heap::Simple
Name: perl-Heap-Simple-XS
Version: 0.09
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Heap-Simple-XS/

Source: http://www.cpan.org/modules/by-module/Heap/Heap-Simple-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides an XS implementation of the interface described in Heap::Simple.

%prep
%setup -n %{real_name}-%{version}

%build
echo | CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Heap/
%dir %{perl_vendorarch}/Heap/Simple/
%{perl_vendorarch}/Heap/Simple/XS.pm
%dir %{perl_vendorarch}/auto/Heap/
%dir %{perl_vendorarch}/auto/Heap/Simple/
%{perl_vendorarch}/auto/Heap/Simple/XS/

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
