# $Id$
# Authority: dries
# Upstream: Jan Pazdziora <adelton$fi,muni,cz>

### EL6 ships with perl-TeX-Hyphen-0.140-9.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name TeX-Hyphen

Summary: Hyphenate words using TeX's patterns
Name: perl-TeX-Hyphen
Version: 0.140
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TeX-Hyphen/

Source: http://www.cpan.org/modules/by-module/TeX/TeX-Hyphen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is the README file for the TeX::Hyphen module. This module uses
TeX style hyphenation patterns to find places in words to hyphenate.
You can supply any hyphenation file you like.

This package contains the following Perl module:

    TeX::Hyphen

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
%doc %{_mandir}/man3/TeX::Hyphen.3pm*
%doc %{_mandir}/man3/TeX::Hyphen::czech.3pm*
%doc %{_mandir}/man3/TeX::Hyphen::german.3pm*
%dir %{perl_vendorlib}/TeX/
%{perl_vendorlib}/TeX/Hyphen/
%{perl_vendorlib}/TeX/Hyphen.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.140-1
- Initial package.
