# $Id$
# Authority: dries
# Upstream: Oliver Gorwits <oliver,gorwits$oucs,ox,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Fast-Contained

Summary: Fast accessors with data containment
Name: perl-Class-Accessor-Fast-Contained
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Fast-Contained/

Source: http://www.cpan.org/modules/by-module/Class/Class-Accessor-Fast-Contained-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
Requires: perl >= 2:5.8.1

%description
Fast accessors with data containment.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Class::Accessor::Fast::Contained.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Accessor/
%dir %{perl_vendorlib}/Class/Accessor/Fast/
#%{perl_vendorlib}/Class/Accessor/Fast/Contained/
%{perl_vendorlib}/Class/Accessor/Fast/Contained.pm

%changelog
* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
