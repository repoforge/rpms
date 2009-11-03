# $Id$
# Authority: dries
# Upstream: Matthew Byng-Maddick <mbm+cpan$colondot,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Blowfish_PP

Summary: Blowfish encryption algorithm implemented purely in Perl
Name: perl-Crypt-Blowfish_PP
Version: 1.12
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Blowfish_PP/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Blowfish_PP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Blowfish is a published algorithm written by Bruce Schneier
(http://www.counterpane.com/). Unlike IDEA or DES etc. there are no patent
implications in using this algorithm.

It uses anywhere between a 64 bit and a 448 bit key. The transform itself is
fast and operates on a 64 bit block, and most of the calculation time is in
initialising the context with the key data.

The _PP name comes from the fact that this implementation is Pure Perl, and
will not have any compatibility problems.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/Blowfish_PP.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.

