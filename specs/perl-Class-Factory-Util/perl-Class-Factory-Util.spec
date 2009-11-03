# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Factory-Util

Summary: Utility methods for factory classes
Name: perl-Class-Factory-Util
Version: 1.7
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Factory-Util/

Source: http://www.cpan.org/modules/by-module/Class/Class-Factory-Util-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)

%description
This module contains utility methods for factory classes.

This package contains the following Perl module:

    Class::Factory::Util

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
%doc Changes LICENSE MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Class::Factory::Util.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Factory/
#%{perl_vendorlib}/Class/Factory/Util/
%{perl_vendorlib}/Class/Factory/Util.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.7-1
- Updated to release 1.7.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
