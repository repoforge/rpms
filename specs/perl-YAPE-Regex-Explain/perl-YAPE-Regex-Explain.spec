# $Id$
# Authority: dag
# Upstream: Gene Sullivan <gsullivan@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAPE-Regex-Explain

Summary: Perl module that consists of explanation of a regular expression
Name: perl-YAPE-Regex-Explain
Version: 4.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAPE-Regex-Explain/

Source: http://search.cpan.org/CPAN/authors/id/G/GS/GSULLIVAN/YAPE-Regex-Explain-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(YAPE::Regex)
Requires: perl(Test::More)
Requires: perl(YAPE::Regex)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-YAPE-Regex-Explain is a Perl module that consists of explanation
of a regular expression.

This package contains the following Perl module:

    YAPE::Regex::Explain

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
%doc %{_mandir}/man3/YAPE::Regex::Explain.3pm*
%dir %{perl_vendorlib}/YAPE/
%dir %{perl_vendorlib}/YAPE/Regex/
#%{perl_vendorlib}/YAPE/Regex/Explain/
%{perl_vendorlib}/YAPE/Regex/Explain.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 4.01-1
- Updated to version 4.01.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 3.011-1
- Initial package. (using DAR)
