# $Id$
# Authority: dag
# Upstream: GomoR <perl$gomor,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Gomor

Summary: Perl module that implements another class and object builder
Name: perl-Class-Gomor
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Gomor/

Source: http://www.cpan.org/modules/by-module/Class/Class-Gomor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Class-Gomor is a Perl module that implements another class and object builder.

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
%doc Changes LICENSE LICENSE.Artistic MANIFEST META.yml README examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Gomor/
%{perl_vendorlib}/Class/Gomor.pm

%changelog
* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 1.02-1
- Updated to version 1.02.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
