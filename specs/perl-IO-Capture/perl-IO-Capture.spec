# $Id$
# Authority: dag
# Upstream: Mark Reynolds <msreynolds$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Capture

Summary: Perl module implements an abstract Base Class to build modules to capture output
Name: perl-IO-Capture
Version: 0.05
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Capture/

Source: http://www.cpan.org/modules/by-module/IO/IO-Capture-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
IO-Capture module for perl.

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
%doc BUGS Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/Capture/
%{perl_vendorlib}/IO/Capture.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
