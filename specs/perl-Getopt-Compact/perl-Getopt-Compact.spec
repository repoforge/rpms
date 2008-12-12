# $Id$
# Authority: cmr

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Compact

Summary: getopt processing in a compact statement with both long and short options, and usage functionality
Name: perl-Getopt-Compact
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Compact/

Source: http://www.cpan.org/modules/by-module/Getopt/Getopt-Compact-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
getopt processing in a compact statement with both long and short options,
and usage functionality.

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
%doc %{_mandir}/man3/Getopt::Compact.3pm*
%doc %{_mandir}/man3/Getopt::Compact::PodMunger.3pm*
%dir %{perl_vendorlib}/Getopt/
%dir %{perl_vendorlib}/Getopt/Compact/
%{perl_vendorlib}/Getopt/Compact/PodMunger.pm
%{perl_vendorlib}/Getopt/Compact.pm

%changelog
* Fri Dec 12 2008 Christoph Maser <cmr@financial.com> - 0.04-1
- Initial package. (using DAR)
