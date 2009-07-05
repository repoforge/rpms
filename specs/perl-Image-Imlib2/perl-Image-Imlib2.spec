# $Id$
# Authority: dries
# Upstream: Leon Brocard <acme$astray,com>

%{?dtag: %{expand: %%define %dtag 1}}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Imlib2

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Interface to the Imlib2 image library
Name: perl-Image-Imlib2
Version: 2.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Imlib2/

Source: http://www.cpan.org/modules/by-module/Image/Image-Imlib2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: imlib2-devel
BuildRequires: perl(Module::Build), perl(ExtUtils::CBuilder)
BuildRequires: zlib-devel
%{!?_without_modxorg:BuildRequires: freetype-devel, libXext-devel}

%description
Image::Imlib2 is a Perl port of Imlib2, a graphics library that does
image file loading and saving as well as manipulation, arbitrary polygon
support, etc. It does ALL of these operations FAST. It allows you to
create colour images using a large number of graphics primitives, and
output the images in a range of formats.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Image::Imlib2.3pm*
%dir %{perl_vendorarch}/auto/Image/
%{perl_vendorarch}/auto/Image/Imlib2/
%dir %{perl_vendorarch}/Image/
%{perl_vendorarch}/Image/Imlib2.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 2.02-1
- Updated to version 2.02.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 2.01-1
- Updated to release 2.01.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 2.00-1
- Updated to release 2.00.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
