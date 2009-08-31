# $Id: perl-Data-Validate-IP.spec 6205 2008-03-08 23:37:36Z shuff $
# Authority: shuff
# Upstream: Neil A. Neely <neil$neely,cx>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Validate-IP

Summary: IP validation methods
Name: perl-Data-Validate-IP
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Validate-IP/

Source: http://www.cpan.org/modules/by-module/Data/Data-Validate-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
#BuildRequires: perl(Test::More)
BuildRequires: perl(Net::Netmask)
Requires: perl
Requires: perl(Net::Netmask)

%description
This module collects IP validation routines to make input validation,
and untainting easier and more readable.

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
%doc %{_mandir}/man3/Data::Validate::IP.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Validate/
%{perl_vendorlib}/Data/Validate/IP.pm

%changelog
* Wed Aug 26 2009 Steve Huff <shuff@vecna.org> - 0.10-1
- Initial package. (using DAR)
