# $Id$
# Authority: dag
# Upstream: Aaron James Trevena <aaron-dot-trevena-at-gmail-dot-com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Maypole

Summary: Perl module that implements a MVC web application framework
Name: perl-Maypole
Version: 2.13
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Maypole/

Source: http://www.cpan.org/modules/by-module/Maypole/Maypole-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(DBD::SQLite2)
Requires: perl(DBD::SQLite2)

%description
Maypole is a Perl module that implements a MVC web application framework.

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
%doc AUTHORS Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/MVC.pm
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Maypole.pm
%dir %{perl_vendorlib}/CGI/Untaint/
%{perl_vendorlib}/CGI/Untaint/Maypole.pm
%{perl_vendorlib}/Maypole.pm
%{perl_vendorlib}/Maypole/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.13-1
- Updated to version 2.13.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.121-1
- Updated to release 2.121.

* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 2.11-1
- Initial package. (using DAR)
