# $Id$
# Authority: dag
# Upstream: Kang-min Liu  C<< <gugod@gugod.org> >>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-to_yaml

Summary: Perl module that implements a to_yaml() method for all objects
Name: perl-UNIVERSAL-to_yaml
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-to_yaml/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-to_yaml-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Test::More)
BuildRequires: perl(Best)
BuildRequires: perl(YAML::Syck)
Requires: perl >= 2:5.8.0

%description
perl-UNIVERSAL-to_yaml is a Perl module that implements a to_yaml() method
for all objects.

This package contains the following Perl module:

    UNIVERSAL::to_yaml

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
%doc %{_mandir}/man3/UNIVERSAL::to_yaml.3pm*
%dir %{perl_vendorlib}/UNIVERSAL/
#%{perl_vendorlib}/UNIVERSAL/to_yaml/
%{perl_vendorlib}/UNIVERSAL/to_yaml.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
