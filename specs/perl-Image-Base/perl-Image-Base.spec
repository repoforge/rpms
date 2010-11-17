# $Id$
# Authority: dries
# Upstream: Mark Summerfield <summer$qtrac,eu>

### EL6 ships with perl-Image-Base-1.07-14.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Base

Summary: Base class for loading, manipulating and saving images
Name: perl-Image-Base
Version: 1.07
Release: 2.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Base/

Source: http://www.cpan.org/modules/by-module/Image/Image-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a base class for loading, manipulating and saving images.

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
%doc MANIFEST README
%doc %{_mandir}/man3/Image::Base.3pm*
%dir %{perl_vendorlib}/Image/
#%{perl_vendorlib}/Image/Base/
%{perl_vendorlib}/Image/Base.pm

%changelog
* Tue Oct 05 2004 Dries Verachtert <dries@ulyssis.org> - 1.07-2
- Rebuild.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.
