# $Id$
# Authority: dries
# Upstream: Jos&#233; Alves de Castro <cog$cpan,org>

%define debug_package %{nil}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Ngram

Summary: Ngram analysis of text
Name: perl-Text-Ngram
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Ngram/

Source: http://search.cpan.org/CPAN/authors/id/A/AM/AMBS/Text/Text-Ngram-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Ngram analysis of text.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/Ngram.pm
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/Ngram/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
