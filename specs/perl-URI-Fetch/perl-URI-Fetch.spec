# $Id$
# Authority: dag
# Upstream: Benjamin Trott <ben+cpan$stupidfool,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Fetch

Summary: Smart URI fetching/caching
Name: perl-URI-Fetch
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Fetch/

Source: http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/URI-Fetch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::ErrorHandler)
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(LWP)
BuildRequires: perl(Storable)
BuildRequires: perl(URI)
BuildRequires: perl >= v5.8.1
Requires: perl(Class::ErrorHandler)
Requires: perl(Compress::Zlib)
Requires: perl(Filter::Util::Call)
Requires: perl(LWP)
Requires: perl(Storable)
Requires: perl(URI)
Requires: perl >= v5.8.1

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Smart URI fetching/caching.

This package contains the following Perl module:

    URI::Fetch

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc %{_mandir}/man3/URI::Fetch.3pm*
%doc %{_mandir}/man3/URI::Fetch::Response.3pm*
%dir %{perl_vendorlib}/URI/
%{perl_vendorlib}/URI/Fetch/
%{perl_vendorlib}/URI/Fetch.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.09-1
- Updated to version 0.09.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
