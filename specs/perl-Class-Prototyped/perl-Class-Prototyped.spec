# $Id$
# Authority: dag
# Upstream: Written by Ned Konz, perl$bike-nomad,com and Toby Ovod-Everett, toby$ovod-everett,org, 5,005_03 porting by chromatic,

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Prototyped

Summary: Fast prototype-based OO programming in Perl
Name: perl-Class-Prototyped
Version: 1.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Prototyped/

Source: http://www.cpan.org/modules/by-module/Class/Class-Prototyped-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Fast prototype-based OO programming in Perl.

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Prototyped/
%{perl_vendorlib}/Class/Prototyped.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 1.10-1
- Initial package. (using DAR)
