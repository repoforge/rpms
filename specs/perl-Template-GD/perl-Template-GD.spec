# $Id$
# Authority: dag
# Upstream: Andy Wardley <cpan$wardley,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-GD

Summary: Perl module that implements GD plugin(s) for the Template Toolkit
Name: perl-Template-GD
Version: 2.66
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-GD/

Source: http://www.cpan.org/modules/by-module/Template/Template-GD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Template-Plugin-GD is a Perl module that implements GD plugin(s)
for the Template Toolkit.

%prep
%setup -n Template-GD-%{version}

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Template/
%dir %{perl_vendorlib}/Template/Plugin/
%{perl_vendorlib}/Template/Plugin/GD/
%{perl_vendorlib}/Template/Plugin/GD.pm

%changelog
* Sat Oct 06 2007 Dag Wieers <dag@wieers.com> - 2.66-1
- Initial package. (using DAR)
