# $Id$
# Authority: dries
# Upstream: Tony Cook <tony$imager,perl,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Imager

Summary: Perl extension for Generating 24 bit Images
Name: perl-Imager
Version: 0.72
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Imager/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TONYC/Imager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libpng-devel
BuildRequires: pkgconfig
BuildRequires: freetype-devel
BuildRequires: libungif-devel
BuildRequires: libtiff-devel
BuildRequires: libjpeg-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
Perl extension for Generating 24 bit Images.

%prep
%setup -n %{real_name}-%{version}

%build
echo "y" | CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes Changes.old MANIFEST MANIFEST.SKIP META.yml README samples/
%doc %{_mandir}/man3/Imager.3pm*
%doc %{_mandir}/man3/Imager::*.3pm*
%{perl_vendorarch}/auto/Imager/
%{perl_vendorarch}/Imager/
%{perl_vendorarch}/Imager.pm

%changelog
* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 0.72-1
- Updated to version 0.72.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.69-1
- Updated to version 0.69.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.67-1
- Updated to version 0.67.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.65-1
- Updated to release 0.65.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.64-1
- Updated to release 0.64.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.61-1
- Updated to release 0.61.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.59-1
- Updated to release 0.59.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.49-1
- Updated to release 0.49.

* Wed Jan  4 2006 Dries Verachtert <dries@ulyssis.org> - 0.47-1
- Initial package.
