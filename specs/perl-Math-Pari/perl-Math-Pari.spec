# $Id$
# Authority: dries
# Upstream: Ilya Zakharevich <cpan$ilyaz,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Pari
%define pari_version 2.1.7

Summary: Perl interface to PARI
Name: perl-Math-Pari
Version: 2.010702
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Pari/

Source0: http://search.cpan.org/CPAN/authors/id/I/IL/ILYAZ/modules/Math-Pari-%{version}.tar.gz
Source1: http://pari.math.u-bordeaux.fr/pub/pari/unix/pari-%{pari_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-Module-Build
### FIXME: Make it build with external pre-build pari package
#Buildrequires: pari-devel

%description
Math::Pari is the PERL interface to the PARI part of GP/PARI (version 2.*).
More info can be found at http://www.parigp-home.de/

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" LIBPARI="-L/usr/lib -lpari" pari_tgz="%{SOURCE1}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/Pari*
%{perl_vendorarch}/Math/libPARI*
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/Pari/Pari.*

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.010702-1
- Updated to release 2.010702.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.010700-1
- Updated to release 2.010700.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 2.010601-1
- Initial package.
