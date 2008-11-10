# $Id$
# Authority: dag
# Upstream: Marc Liyanage <liyanage$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geometry-AffineTransform

Summary: Affine Transformation to map 2D coordinates to other 2D coordinates
Name: perl-Geometry-AffineTransform
Version: 1.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geometry-AffineTransform/

Source: http://www.cpan.org/authors/id/L/LI/LIYANAGE/Geometry-AffineTransform-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Affine Transformation to map 2D coordinates to other 2D coordinates.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Geometry::AffineTransform.3pm*
%dir %{perl_vendorlib}/Geometry/
#%{perl_vendorlib}/Geometry/AffineTransform/
%{perl_vendorlib}/Geometry/AffineTransform.pm

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
