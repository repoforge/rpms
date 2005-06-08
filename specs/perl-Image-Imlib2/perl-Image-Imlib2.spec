# $Id$
# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Imlib2

Summary: Interface to the Imlib2 image library
Name: perl-Image-Imlib2
Version: 1.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Imlib2/

Source: http://www.cpan.org/modules/by-module/Image/Image-Imlib2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, imlib2-devel, perl-Module-Build, zlib-devel

%description
Image::Imlib2 is a Perl port of Imlib2, a graphics library that does
image file loading and saving as well as manipulation, arbitrary polygon
support, etc. It does ALL of these operations FAST. It allows you to
create colour images using a large number of graphics primitives, and
output the images in a range of formats.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Image/
%{perl_vendorarch}/Image/Imlib2.pm
%dir %{perl_vendorarch}/auto/Image/
%{perl_vendorarch}/auto/Image/Imlib2

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
