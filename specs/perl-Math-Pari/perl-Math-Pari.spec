# $Id$
# Authority: dries
# Upstream: Ilya Zakharevich <cpan$ilyaz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Pari
%define real_version 2.3.3

Summary: Perl interface to PARI
Name: perl-Math-Pari
Version: 2.010800
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Pari/

Source: http://www.cpan.org/modules/by-module/Math/Math-Pari-%{version}.tar.gz
Source1: http://pari.math.u-bordeaux.fr/pub/pari/unix/pari-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Module::Build)
### FIXME: Make it build with external pre-build pari package
#Buildrequires: pari-devel

%description
Math::Pari is the PERL interface to the PARI part of GP/PARI (version 2.*).
More info can be found at http://www.parigp-home.de/

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" LIBPARI="-L/usr/lib -lpari" pari_tgz="%{SOURCE1}"
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
%doc Changes INSTALL MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Math::Pari.3pm*
%doc %{_mandir}/man3/Math::PariInit.3pm*
%doc %{_mandir}/man3/Math::libPARI.3pm*
%doc %{_mandir}/man3/Math::libPARI.dumb.3pm*
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/Pari/
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/Pari.pm
%{perl_vendorarch}/Math/PariInit.pm
%{perl_vendorarch}/Math/libPARI.dumb.pod
%{perl_vendorarch}/Math/libPARI.pod

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.010800-1
- Updated to release 2.010800.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.010709-1
- Updated to release 2.010709.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 2.010706-1
- Updated to release 2.010706.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.010704-1
- Updated to release 2.010704.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.010702-1
- Updated to release 2.010702.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.010700-1
- Updated to release 2.010700.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 2.010601-1
- Initial package.
