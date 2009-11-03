# $Id$
# Authority: dag
# Upstream: Dan Brook <mr,daniel,brook$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Locate

Summary: Perl module to locate modules in the same fashion as require and use
Name: perl-Module-Locate
Version: 1.7
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Locate/

Source: http://www.cpan.org/modules/by-module/Module/Module-Locate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Module-Locate is a Perl module to locate modules in the same fashion
as require and use.

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
%doc %{_mandir}/man3/Module::Locate.3pm*
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/Locate.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.7-1
- Initial package. (using DAR)
