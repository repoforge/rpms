# $Id$
# Authority: dries
# Upstream: Struan Donald <struan$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Validator-HTML-W3C

Summary: Access the W3Cs online HTML validator
Name: perl-WebService-Validator-HTML-W3C
Version: 0.19
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Validator-HTML-W3C/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STRUAN/WebService-Validator-HTML-W3C-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Access the W3Cs online HTML validator.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/WebService::Validator::HTML::W3C*
%{perl_vendorlib}/WebService/Validator/HTML/W3C.pm
%{perl_vendorlib}/WebService/Validator/HTML/W3C/
%dir %{perl_vendorlib}/WebService/Validator/HTML/
%dir %{perl_vendorlib}/WebService/Validator/

%changelog
* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
