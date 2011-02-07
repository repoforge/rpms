# $Id$
# Authority: dag
# Upstream: Gene Sullivan <gsullivan@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAPE-Regex

Summary: Perl module that implements Yet Another Parser/Extractor for Regular Expressions
Name: perl-YAPE-Regex
Version: 4.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAPE-Regex/

Source: http://search.cpan.org/CPAN/authors/id/G/GS/GSULLIVAN/YAPE-Regex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Text::Balanced)
Requires: perl(Text::Balanced)

%filter_from_requires /^perl*/d
%filter_setup

%description
perl-YAPE-Regex is a Perl module that implements Yet Another Parser/Extractor
for Regular Expressions.

This package contains the following Perl module:

    YAPE::Regex

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
%doc %{_mandir}/man3/YAPE::Regex.3pm*
%doc %{_mandir}/man3/YAPE::Regex::Element.3pm*
%dir %{perl_vendorlib}/YAPE/
%{perl_vendorlib}/YAPE/Regex/
%{perl_vendorlib}/YAPE/Regex.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 4.00-1
- Updated to version 4.00.

* Tue Dec  8 2009 Christoph Maser <cmr@financial.com> - 3.04-1
- Updated to version 3.04.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 3.03-1
- Initial package. (using DAR)
