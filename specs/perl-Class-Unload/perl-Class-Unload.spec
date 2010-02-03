# $Id$
# Upstream: Dagfinn Ilmari Mannsaker <ilmari+cpan@ilmari.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Class-Unload

Summary: Class::Unload - Unload a class
Name: perl-Class-Unload
Version: 0.05
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Unload

Source: http://search.cpan.org/CPAN/authors/id/I/IL/ILMARI/Class-Unload-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.005
Requires: perl(Class::Inspector)
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup

%description
Unloads the given class by clearing out its symbol table and removing it from %INC.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__make} test

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Class::Unload.3pm*
%{perl_vendorlib}/Class/Unload.pm

%changelog
* Wed Feb 03 2010 Chrisoph Maser <cmr@financial.com> 0.05-1
- initial package
