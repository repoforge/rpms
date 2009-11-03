# $Id: $
# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Lvalue

Summary: Creates Lvalue accessors
Name: perl-Class-Accessor-Lvalue
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Lvalue/

Source: http://www.cpan.org/modules/by-module/Class/Class-Accessor-Lvalue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module you can create Lvalue accessors.

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
%doc Changes NINJA README
%doc %{_mandir}/man3/Class::Accessor::Lvalue*
%{perl_vendorlib}/Class/Accessor/Lvalue.pm
%{perl_vendorlib}/Class/Accessor/Lvalue/
%dir %{perl_vendorlib}/Class/Accessor/

%changelog
* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
