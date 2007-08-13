# $Id$
# Authority: dries
# Upstream: Tony Cook <tony$develop-help,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Imager

Summary: Extension for generating 24 bit images
Name: perl-Imager
Version: 0.55
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Imager/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TONYC/Imager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, libpng-devel, pkgconfig, freetype-devel, libungif-devel, libtiff-devel
BuildRequires: libjpeg-devel, perl(ExtUtils::MakeMaker)

%description
Perl extension for Generating 24 bit Images.

%prep
%setup -n %{real_name}-%{version}

%build
echo y | CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

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
