# $Id$
# Authority: dag
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Chained

Summary: Perl module to make chained accessors
Name: perl-Class-Accessor-Chained
Version: 0.01
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Chained/

Source: http://www.cpan.org/modules/by-module/Class/Class-Accessor-Chained-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Class-Accessor-Chained is a Perl module to make chained accessors.

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
%doc %{_mandir}/man3/Class::Accessor::Chained.3pm*
%doc %{_mandir}/man3/Class::Accessor::Chained::Fast.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Accessor/
%{perl_vendorlib}/Class/Accessor/Chained/
%{perl_vendorlib}/Class/Accessor/Chained.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
