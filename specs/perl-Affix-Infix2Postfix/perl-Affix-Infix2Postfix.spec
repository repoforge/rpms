# $Id$
# Authority: dag
# Upstream: Arnar Mar Hrafnkelsson <addi$umich,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Affix-Infix2Postfix

Summary: Perl module for converting from infix notation to postfix notation
Name: perl-Affix-Infix2Postfix
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Affix-Infix2Postfix/

Source: http://www.cpan.org/authors/id/A/AD/ADDI/Affix-Infix2Postfix-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Affix-Infix2Postfix is a Perl module for converting from infix notation
to postfix notation.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Affix::Infix2Postfix.3pm*
%dir %{perl_vendorlib}/Affix/
%{perl_vendorlib}/Affix/Infix2Postfix.pm
%{perl_vendorlib}/auto/Affix/Infix2Postfix/

%changelog
* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
