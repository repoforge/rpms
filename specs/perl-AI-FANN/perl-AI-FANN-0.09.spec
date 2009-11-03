# $Id$
# Authority: dries
# Upstream: Salvador Fandiño García <salva$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-FANN

Summary: Wapper for the Fast Artificial Neural Network library
Name: perl-AI-FANN
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-FANN/

Source: http://www.cpan.org/modules/by-module/AI/AI-FANN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fann-devel
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides a Perl wrapper for the FANN library
(http://fann.sf.net).

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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README samples/
%doc %{_mandir}/man3/AI::FANN.3pm*
%dir %{perl_vendorarch}/AI/
%{perl_vendorarch}/AI/FANN.pm
%dir %{perl_vendorarch}/auto/AI/
%{perl_vendorarch}/auto/AI/FANN/

%changelog
* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
