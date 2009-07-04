# $Id$
# Authority: dag
# Upstream: Leon Brocard <leon$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-CPAN-Packages

Summary: Parse 02packages.details.txt.gz
Name: perl-Parse-CPAN-Packages
Version: 2.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-CPAN-Packages/

Source: http://www.cpan.org/modules/by-module/Parse/Parse-CPAN-Packages-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Parse 02packages.details.txt.gz.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Parse::CPAN::Packages*.3pm*
%dir %{perl_vendorlib}/Parse/
%dir %{perl_vendorlib}/Parse/CPAN/
%{perl_vendorlib}/Parse/CPAN/Packages/
%{perl_vendorlib}/Parse/CPAN/Packages.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.31-1
- Updated to version 2.31.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 2.27-1
- Updated to release 2.27.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 2.26-1
- Initial package. (using DAR)
