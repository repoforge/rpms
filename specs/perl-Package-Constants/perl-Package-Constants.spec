# $Id$
# Authority: dag
# Upstream: Jos Boumans <kane$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Package-Constants

Summary: Perl module to list all constants declared in a package
Name: perl-Package-Constants
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Package-Constants/

Source: http://www.cpan.org/modules/by-module/Package/Package-Constants-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Package-Constants is a Perl module to list all constants
declared in a package

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
%doc %{_mandir}/man3/Package::Constants.3pm*
%dir %{perl_vendorlib}/Package/
%{perl_vendorlib}/Package/Constants.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.02-1
- Updated to version 0.02.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
