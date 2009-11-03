# $Id$
# Authority: dag
# Upstream: Chia-liang Kao <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Hierarchy

Summary: Perl module to handle data in a hierarchical structure
Name: perl-Data-Hierarchy
Version: 0.34
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Hierarchy/

Source: http://www.cpan.org/modules/by-module/Data/Data-Hierarchy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Data-Hierarchy is a Perl module to handle data in a hierarchical structure.

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/Data::Hierarchy.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/Hierarchy/
%{perl_vendorlib}/Data/Hierarchy.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.34-1
- Initial package. (using DAR)
