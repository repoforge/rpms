# $Id$
# Authority: dries
# Upstream: Frank J. Tobin <ftobin$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name GnuPG-Interface

Summary: Perl interface to GnuPG
Name: perl-GnuPG-Interface
Version: 0.35
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GnuPG-Interface/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/GnuPG-Interface-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl(Class::MethodMaker)

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*.3*
%{perl_vendorlib}/GnuPG/
%{perl_vendorlib}/auto/GnuPG/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Initial package.
