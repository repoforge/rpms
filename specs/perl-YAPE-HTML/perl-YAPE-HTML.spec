# $Id$
# Authority: dag
# Upstream: Jeff Pinyan <japhy,734+CPAN$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAPE-HTML

Summary: Perl module that implements Yet Another Parser/Extractor for HTML
Name: perl-YAPE-HTML
Version: 1.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAPE-HTML/

Source: http://www.cpan.org/authors/id/P/PI/PINYAN/YAPE-HTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-YAPE-HTML is a Perl module that implements Yet Another Parser/Extractor
for HTML.

This package contains the following Perl module:

    YAPE::HTML

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
%doc %{_mandir}/man3/YAPE::HTML.3pm*
%doc %{_mandir}/man3/YAPE::HTML::Element.3pm*
%dir %{perl_vendorlib}/YAPE/
%{perl_vendorlib}/YAPE/HTML/
%{perl_vendorlib}/YAPE/HTML.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.11-1
- Initial package. (using DAR)
