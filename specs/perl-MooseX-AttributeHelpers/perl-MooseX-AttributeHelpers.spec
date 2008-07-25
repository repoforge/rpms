# $Id: perl-MooseX-AttributeHelpers.spec 6212 2008-03-14 01:19:20Z dag $
# Authority: dries
# Upstream: Shawn M Moore <sartak$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-AttributeHelpers

Summary: Extend your attribute interfaces
Name: perl-MooseX-AttributeHelpers
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-AttributeHelpers/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-AttributeHelpers-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
#BuildRequires: perl(Moose)

%description
Extend your attribute interfaces.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/MooseX::AttributeHelpers.3pm*
%doc %{_mandir}/man3/MooseX::AttributeHelpers::*3pm*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/AttributeHelpers/
%{perl_vendorlib}/MooseX/AttributeHelpers.pm

%changelog
* Fri Jul 25 2008 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
