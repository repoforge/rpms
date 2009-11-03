# $Id$
# Authority: dag
# Upstream: Eric Wilhelm <ewilhelm$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Geometry-Planar-Offset

Summary: Perl module to calculate offset polygons
Name: perl-Math-Geometry-Planar-Offset
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Geometry-Planar-Offset/

Source: http://www.cpan.org/modules/by-module/Math/Math-Geometry-Planar-Offset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
perl-Math-Geometry-Planar-Offset is a Perl module to calculate offset polygons.

This package contains the following Perl module:

    Math::Geometry::Planar::Offset

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Math::Geometry::Planar::Offset.3pm*
%dir %{perl_vendorlib}/Math/
%dir %{perl_vendorlib}/Math/Geometry/
%dir %{perl_vendorlib}/Math/Geometry/Planar/
#%{perl_vendorlib}/Math/Geometry/Planar/Offset/
%{perl_vendorlib}/Math/Geometry/Planar/Offset.pm

%changelog
* Wed Jan 02 2008 Fabian Arrotin <fabian.arrotin@arrfab.net> 
- Added a missing BuildRequires: perl(Module::Build) to build properly in Mock
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
