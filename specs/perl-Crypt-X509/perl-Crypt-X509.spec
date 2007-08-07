# $Id$
# Authority: dries
# Upstream: Alexander Jung <alexander,w,jung$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-X509

Summary: Object oriented X.509 certificate parser
Name: perl-Crypt-X509
Version: 0.21
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-X509/

Source: http://search.cpan.org/CPAN/authors/id/A/AJ/AJUNG/Crypt-X509-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Crypt::X509 is an object oriented X.509 certificate parser with numerous
methods for directly extracting information from certificates.

%prep
%setup -n %{real_name}

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
%doc %{_mandir}/man3/Crypt::X509.3pm*
%{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/X509.pm

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.

