# $Id$
# Authority: dries
# Upstream: Graciliano Monteiro Passos <gmpassos$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-IPfree

Summary: Look up the country of an ipaddress.
Name: perl-Geo-IPfree
Version: 0.8
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-IPfree/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRICAS/Geo-IPfree-0.8.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Memoize)
BuildRequires: perl(Test::More) >= 0.47
Requires: perl(Memoize)
Requires: perl(Test::More) >= 0.47

%filter_from_requires /^perl*/d
%filter_setup

%description
With this module, you can lookup the country of an ipaddress.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Geo/IPfree.pm
%{perl_vendorlib}/Geo/ipscountry.dat

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.8-1
- Updated to version 0.8.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.6-1
- Updated to version 0.6.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
