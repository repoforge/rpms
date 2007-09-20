# $Id$
# Authority: dries
# Upstream: Salvador Fandi&#241;o Garc&#237;a <salva$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-FANN

Summary: Wapper for the Fast Artificial Neural Network library
Name: perl-AI-FANN
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-FANN/

Source: http://search.cpan.org//CPAN/authors/id/S/SA/SALVA/AI-FANN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, fann-devel, perl(ExtUtils::MakeMaker)

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/AI/
%{perl_vendorarch}/AI/FANN.pm
%dir %{perl_vendorarch}/auto/AI/
%{perl_vendorarch}/auto/AI/FANN/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
