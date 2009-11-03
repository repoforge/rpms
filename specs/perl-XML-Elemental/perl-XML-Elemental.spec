# $Id$
# Authority: dag
# Upstream: Timothy Appnel <cpan$timaoutloud,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Elemental

Summary: Perl module implements simplistic and perlish handling of XML data
Name: perl-XML-Elemental
Version: 2.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Elemental/

Source: http://www.cpan.org/modules/by-module/XML/XML-Elemental-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-XML-Elemental is a Perl module implements simplistic
and perlish handling of XML data.

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
%doc %{_mandir}/man3/XML::Elemental.3pm*
%doc %{_mandir}/man3/XML::Elemental::*.3pm*
%doc %{_mandir}/man3/XML::Parser::Style::Elemental.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Elemental/
%{perl_vendorlib}/XML/Elemental.pm
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Parser/
%dir %{perl_vendorlib}/XML/Parser/Style/
%{perl_vendorlib}/XML/Parser/Style/Elemental.pm

%changelog
* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 2.1-1
- Updated to version 2.1.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
