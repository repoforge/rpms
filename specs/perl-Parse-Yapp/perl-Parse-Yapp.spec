# $Id$
# Authority: dag
# Upstream: Francois Desarmenien <francois$fdesar,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-Yapp
%define real_version undef

Summary: Perl module for generating and using LALR parsers
Name: perl-Parse-Yapp
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-Yapp/

Source: http://www.cpan.org/modules/by-module/Parse/Parse-Yapp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Parse-Yapp is a Perl module for generating and using LALR parsers.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man1/yapp.1*
%doc %{_mandir}/man3/Parse::Yapp.3*
%{_bindir}/yapp
%dir %{perl_vendorlib}/Parse/
%{perl_vendorlib}/Parse/Yapp/
%{perl_vendorlib}/Parse/Yapp.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
