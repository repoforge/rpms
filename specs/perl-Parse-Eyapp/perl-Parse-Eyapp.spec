# $Id$
# Authority: dag
# Upstream: Casiano Rodriguez-Leon <casiano$ull,es>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-Eyapp

Summary: Extensions for Parse::Yapp
Name: perl-Parse-Eyapp
Version: 1.098
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-Eyapp/

Source: http://www.cpan.org/modules/by-module/Parse/Parse-Eyapp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Extensions for Parse::Yapp.

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
%doc Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man1/eyapp.1*
%doc %{_mandir}/man1/treereg.1*
#%doc %{_mandir}/man3/Parse::Eyapp.3pm*
#%doc %{_mandir}/man3/Parse::Eyapp::*.3pm*
%{_bindir}/eyapp
%{_bindir}/treereg
%dir %{perl_vendorlib}/Parse/
%{perl_vendorlib}/Parse/Eyapp/
%{perl_vendorlib}/Parse/Eyapp.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.098-1
- Initial package. (using DAR)
