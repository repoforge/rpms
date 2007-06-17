# $Id$

# Authority: dries
# Upstream: Rafael R. Sevilla <sevillar$team,ph,inter,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Rijndael

Summary: Crypt::CBC compliant Rijndael encryption module
Name: perl-Crypt-Rijndael
Version: 0.05
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Rijndael/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Rijndael-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This is Crypt::Rijndael, an XS-based implementation of the newly-selected
Advanced Encryption Standard algorithm Rijndael, designed by Joan Daemen
and Vincent Rijmen.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc NEWS README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/Rijndael.pm
%{perl_vendorarch}/auto/Crypt/Rijndael

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
