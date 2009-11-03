# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Log4perl

Summary: test log4perl
Name: perl-Test-Log4perl
Version: 0.1001
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Log4perl/

Source: http://www.cpan.org/modules/by-module/Test/Test-Log4perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Builder::Tester) >= 0.9
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)

%description
test log4perl.

This package contains the following Perl module:

    Test::Log4perl

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
%doc %{_mandir}/man3/Test::Log4perl.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Log4perl/
%{perl_vendorlib}/Test/Log4perl.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.1001-1
- Initial package. (using DAR)
