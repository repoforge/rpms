# $Id$
# Authority: dries
# Upstream: Frank J. Tobin <ftobin$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GnuPG-Interface

Summary: Perl interface to GnuPG
Name: perl-GnuPG-Interface
Version: 0.42
Release: 2%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GnuPG-Interface/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/GnuPG-Interface-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gnupg
BuildRequires: perl
BuildRequires: which
BuildRequires: perl(Any::Moose)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Any::Moose)
Requires: perl(Class::MethodMaker)
Requires: gnupg

%filter_from_requires /^perl*/d
%filter_setup

%description
GnuPG::Interface and its associated modules are designed to provide an
object-oriented method for interacting with GnuPG, being able to perform
functions such as but not limited to encrypting, signing, decryption,
verification, and key-listing parsing.

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
%doc COPYING ChangeLog MANIFEST META.yml NEWS README SIGNATURE THANKS
%doc %{_mandir}/man3/GnuPG::*.3pm*
%{perl_vendorlib}/GnuPG/
#%dir %{perl_vendorlib}/auto/GnuPG/
#%{perl_vendorlib}/auto/GnuPG/Interface/

%changelog
* Wed Jul 28 2010 Steve Huff <shuff@vecna.org> - 0.42-2
- Captured missing Any::Moose dependency.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.42-1
- Updated to version 0.42.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.36-1
- Updated to release 0.36.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Initial package.
