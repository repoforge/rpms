# $Id$
# Authority: dag
# Upstream: Atsushi Kobayashi <nekokak$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Fetch-SimpleCache

Summary: Perl module that implements URI::Fetch extension with local cache
Name: perl-URI-Fetch-SimpleCache
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Fetch-SimpleCache/

Source: http://www.cpan.org/modules/by-module/URI/URI-Fetch-SimpleCache-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-Fetch-SimpleCache is a Perl module that implements
URI::Fetch extension with local cache.

This package contains the following Perl module:

    URI::Fetch::SimpleCache

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
%doc %{_mandir}/man3/URI::Fetch::SimpleCache.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/Fetch/
#%{perl_vendorlib}/URI/Fetch/SimpleCache/
%{perl_vendorlib}/URI/Fetch/SimpleCache.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
