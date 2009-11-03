# $Id$
# Authority: dries
# Upstream: William Herrera <whererra$lynxview,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-MD5-M4p

Summary: Perl interface to a variant of the MD5 algorithm
Name: perl-Digest-MD5-M4p
Version: 0.01
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-MD5-M4p/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-MD5-M4p-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
he Digest::MD5 module is cloned from the Digest::MD5 module to support a
variant  Apple iTunes implementation of the MD5 algorithm. If you don't know
why this is so, don't bother with this module! It is incompatible with RSA
and RFC standards!


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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Digest/
%dir %{perl_vendorarch}/Digest/MD5/
%{perl_vendorarch}/Digest/MD5/M4p.pm
%dir %{perl_vendorarch}/auto/Digest/
%dir %{perl_vendorarch}/auto/Digest/MD5/
%{perl_vendorarch}/auto/Digest/MD5/M4p

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
