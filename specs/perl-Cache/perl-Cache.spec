# $Id$
# Authority: dag
# Upstream: Chris Leishman <chris$leishman,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cache

Summary: Perl module that implements a Cache interface
Name: perl-Cache
Version: 2.04
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache/

Source: http://www.cpan.org/modules/by-module/Cache/Cache-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Cache is a Perl module that implements a Cache interface.

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
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Cache/
%{perl_vendorlib}/Cache.pm

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 2.04-1
- Initial package. (using DAR)
