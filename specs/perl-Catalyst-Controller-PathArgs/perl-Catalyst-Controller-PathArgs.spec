# $Id$
# Authority: dries
# Upstream: Zbigniew Lukasiak <tmp$zby,aster,net,pl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Controller-PathArgs

Summary: Syntactic sugar for Catalyst::DispatchType::Chained
Name: perl-Catalyst-Controller-PathArgs
Version: 0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Controller-PathArgs/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Controller-PathArgs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Syntactic sugar for Catalyst::DispatchType::Chained.

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
%doc Changes LICENSE MANIFEST META.yml README Todo examples/
%doc %{_mandir}/man3/Catalyst::Controller::PathArgs.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Controller/
#%{perl_vendorlib}/Catalyst/Controller/PathArgs/
%{perl_vendorlib}/Catalyst/Controller/PathArgs.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Updated to release 0.2.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
