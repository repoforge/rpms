# $Id$

# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define real_name Image-Imlib2
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to the Imlib2 image library
Name: perl-Image-Imlib2
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Imlib2/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/Image-Imlib2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, imlib2-devel, perl-Module-Build

%description
Image::Imlib2 is a Perl port of Imlib2, a graphics library that does
image file loading and saving as well as manipulation, arbitrary polygon
support, etc. It does ALL of these operations FAST. It allows you to
create colour images using a large number of graphics primitives, and
output the images in a range of formats.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
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
%{perl_vendorarch}/Image/Imlib2.pm
%{perl_vendorarch}/auto/Image/Imlib2

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
