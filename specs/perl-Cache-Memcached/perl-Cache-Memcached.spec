# $Id$
# Authority: dag
# Upstream: Alan Kasindorf <dormando@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cache-Memcached

Summary: Perl module implements a client library for memcached
Name: perl-Cache-Memcached
Version: 1.29
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache-Memcached/

Source: http://search.cpan.org/CPAN/authors/id/D/DO/DORMANDO/Cache-Memcached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Encode)
BuildRequires: perl(Storable)
BuildRequires: perl(String::CRC32)
BuildRequires: perl(Time::HiRes)
Requires: perl(Encode)
Requires: perl(Storable)
Requires: perl(String::CRC32)
Requires: perl(Time::HiRes)

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-Cache-Memcached is a Perl module implements a client library
for memcached.

This package contains the following Perl module:

    Cache::Memcached

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/Cache::Memcached.3pm*
%dir %{perl_vendorlib}/Cache/
%{perl_vendorlib}/Cache/Memcached/
%{perl_vendorlib}/Cache/Memcached.pm

%changelog
* Mon Oct 11 2010 Christoph Maser <cmaser@gmx.de> - 1.29-1
- Updated to version 1.29.

* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 1.28-1
- Updated to version 1.28.

* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 1.24-1
- Initial package. (using DAR)
