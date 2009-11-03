# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-SaveLater

Summary: Base class for tie modules that "save later"
Name: perl-Tie-SaveLater
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-SaveLater/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-SaveLater-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Base class for tie modules that "save later".

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
%doc %{_mandir}/man3/Tie::DataDumper.3pm*
%doc %{_mandir}/man3/Tie::SaveLater.3pm*
%doc %{_mandir}/man3/Tie::Storable.3pm*
%doc %{_mandir}/man3/Tie::YAML.3pm*
%dir %{perl_vendorlib}/Tie/
#%{perl_vendorlib}/Tie/Storable/
%{perl_vendorlib}/Tie/DataDumper.pm
%{perl_vendorlib}/Tie/SaveLater.pm
%{perl_vendorlib}/Tie/Storable.pm
%{perl_vendorlib}/Tie/YAML.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
