# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-ReturnValue

Summary: Return-value object
Name: perl-Class-ReturnValue
Version: 0.55
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-ReturnValue/

Source: http://www.cpan.org/modules/by-module/Class/Class-ReturnValue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A return-value object that lets you treat it as as a boolean, array or object.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml
%doc %{_mandir}/man3/Class::ReturnValue.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/ReturnValue/
%{perl_vendorlib}/Class/ReturnValue.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Initial package.
