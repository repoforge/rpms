# $Id$
# Authority: dag
# Upstream: D. H. <crazyinsomniac$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-LinkExtractor

Summary: Perl module to extract *links* from an HTML document
Name: perl-HTML-LinkExtractor
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-LinkExtractor/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-LinkExtractor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Tk)

%description
perl-HTML-LinkExtractor is a Perl module to extract *links*
from an HTML document.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/HTML::LinkExtractor.3pm*
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/LinkExtractor.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
