# $Id$
# Authority: dries
# Upstream: Tony Cook <tony$develop-help,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Imager

Summary: Extension for generating 24 bit images
Name: perl-Imager
Version: 0.59
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Imager/

Source: http://www.cpan.org/modules/by-module/Imager/Imager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libpng-devel
BuildRequires: pkgconfig
BuildRequires: freetype-devel
BuildRequires: libungif-devel
BuildRequires: libtiff-devel
BuildRequires: libjpeg-devel
BuildRequires: perl(ExtUtils::MakeMaker)

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Imager.pm
%{perl_vendorarch}/Imager/
%{perl_vendorarch}/auto/Imager/

%changelog
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
