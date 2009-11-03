# $Id$
# Authority: dag
# Upstream: Chunzi <chunzi$perlchina,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI-Loader-Relationship

Summary: Perl module that implements an easier relationship specification in CDBI::Loader
Name: perl-Class-DBI-Loader-Relationship
Version: 1.2
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI-Loader-Relationship/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-Loader-Relationship-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Class-DBI-Loader-Relationship is a Perl module that implements an easier
relationship specification in CDBI::Loader.

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
%doc %{_mandir}/man3/Class::DBI::Loader::Relationship.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/DBI/
%dir %{perl_vendorlib}/Class/DBI/Loader/
%{perl_vendorlib}/Class/DBI/Loader/Relationship.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
