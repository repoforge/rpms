# $Id$
# Authority: dag
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Authorization-Roles

Summary: Role based authorization for Catalyst based on Catalyst::Plugin::Authentication
Name: perl-Catalyst-Plugin-Authorization-Roles
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Authorization-Roles/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Authorization-Roles-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
Requires: perl >= 2:5.8.0

%description
Role based authorization for Catalyst based on Catalyst::Plugin::Authentication.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Catalyst::Plugin::Authorization::Roles.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Authorization/
#%{perl_vendorlib}/Catalyst/Plugin/Authorization/Roles/
%{perl_vendorlib}/Catalyst/Plugin/Authorization/Roles.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
