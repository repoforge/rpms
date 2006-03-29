# $Id$
# Authority: dries
# Upstream: Frank J. Tobin <ftobin$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name GnuPG-Interface

Summary: Perl interface to GnuPG
Name: perl-GnuPG-Interface
Version: 0.33
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GnuPG-Interface/

Source: http://search.cpan.org/CPAN/authors/id/F/FT/FTOBIN/GnuPG-Interface-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/GnuPG
%{perl_vendorlib}/auto/GnuPG

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Initial package.
