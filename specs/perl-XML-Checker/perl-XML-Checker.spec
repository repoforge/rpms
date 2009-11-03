# $Id$
# Authority: dag
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Checker

Summary: Perl module for validating XML
Name: perl-XML-Checker
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Checker/

Source: http://www.cpan.org/modules/by-module/XML/XML-Checker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl module for validating XML.

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
%doc %{_mandir}/man3/XML::Checker.3pm*
%doc %{_mandir}/man3/XML::Checker::*.3pm*
%doc %{_mandir}/man3/XML::DOM::ValParser.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Checker/
%{perl_vendorlib}/XML/Checker.pm
%dir %{perl_vendorlib}/XML/DOM/
%{perl_vendorlib}/XML/DOM/ValParser.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
