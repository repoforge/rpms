# $Id$
# Authority: dag
# Upstream: Daisuke Maki <dmaki$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI-Loader

Summary: Perl module that implements a dynamic definition of Class::DBI sub classes
Name: perl-Class-DBI-Loader
Version: 0.34
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI-Loader/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-Loader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Class-DBI-Loader is a Perl module that implements a dynamic
definition of Class::DBI sub classes.

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
%doc %{_mandir}/man3/Class::DBI::Loader.3pm*
%doc %{_mandir}/man3/Class::DBI::Loader::*.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/DBI/
%{perl_vendorlib}/Class/DBI/Loader/
%{perl_vendorlib}/Class/DBI/Loader.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.35.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Initial package. (using DAR)
