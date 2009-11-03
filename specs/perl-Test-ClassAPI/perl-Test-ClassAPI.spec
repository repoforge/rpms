# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-ClassAPI

Summary: Provides basic first-pass API testing for large class trees
Name: perl-Test-ClassAPI
Version: 1.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-ClassAPI/

Source: http://www.cpan.org/modules/by-module/Test/Test-ClassAPI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.6.0
BuildRequires: perl(Class::Inspector) >= 1.12
BuildRequires: perl(Config::Tiny) >= 2.00
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(File::Spec) >= 0.83
BuildRequires: perl(Params::Util) >= 1.00
BuildRequires: perl(Test::More) >= 0.47 
Requires: perl >= 5.6.0

%description
For many APIs with large numbers of classes, it can be very useful to be
able to do a quick once-over to make sure that classes, methods, and
inheritance is correct, before doing more comprehensive testing. This
module aims to provide such a capability.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Test::ClassAPI.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/ClassAPI.pm

%changelog
* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.06-1
- Updated to version 1.06.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Sun Jan 16 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
