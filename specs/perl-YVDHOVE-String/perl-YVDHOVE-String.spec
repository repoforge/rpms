# $Id$
# Authority: dag
# Upstream: Yves Van den Hove <yvdhove$users,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YVDHOVE-String

Summary: Perl module that implements useful String functions
Name: perl-YVDHOVE-String
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YVDHOVE-String/

Source: http://www.cpan.org/authors/id/Y/YV/YVDHOVE/YVDHOVE-String-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 3:5.8.7
Requires: perl >= 3:5.8.7

%description
perl-YVDHOVE-String is a Perl module that implements a library of useful
String functions.

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
%doc %{_mandir}/man3/YVDHOVE::String.3pm*
%dir %{perl_vendorlib}/YVDHOVE/
#%{perl_vendorlib}/YVDHOVE/String/
%{perl_vendorlib}/YVDHOVE/String.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
