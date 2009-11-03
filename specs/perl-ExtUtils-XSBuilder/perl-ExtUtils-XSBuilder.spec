# $Id$
# Authority: dag
# Upstream: Gerald Richter <richter$ecos,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-XSBuilder

Summary: Perl module that implements an automatic Perl XS glue code generator
Name: perl-ExtUtils-XSBuilder
Version: 0.28
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-XSBuilder/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-XSBuilder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
ExtUtils-XSBuilder is a Perl module that implements an automatic
Perl XS glue code generator.

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/ExtUtils/
%{perl_vendorlib}/ExtUtils/XSBuilder/
%{perl_vendorlib}/ExtUtils/XSBuilder.pm
%{perl_vendorlib}/ExtUtils/XSBuilder.pod
%{perl_vendorlib}/ExtUtils/xsbuilder.osc2002.pod

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.28-1
- Initial package. (using DAR)
