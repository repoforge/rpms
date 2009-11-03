# $Id$
# Authority: dag
# Upstream: Stanislaw Y. Pusep <stanis$linuxmail,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Roman

Summary: Converts roman algarism in integer numbers and the contrary, recognize algarisms
Name: perl-Text-Roman
Version: 3.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Roman/

Source: http://www.cpan.org/modules/by-module/Text/Text-Roman-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Converts roman algarism in integer numbers and the contrary,
recognize algarisms.

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
%doc MANIFEST README
%doc %{_mandir}/man3/Text::Roman.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Roman/
%{perl_vendorlib}/Text/Roman.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 3.01-1
- Initial package. (using DAR)
