# $Id$
# Authority: dag
# Upstream: Tim Bunce <Tim,Bunce$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Memcached-libmemcached

Summary: Thin fast full interface to the libmemcached client API
Name: perl-Memcached-libmemcached
Version: 0.3102
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Memcached-libmemcached/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/Memcached-libmemcached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: memcached
Requires: memcached

%description
Thin fast full interface to the libmemcached client API.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Memcached::libmemcached.3pm*
%doc %{_mandir}/man3/Memcached::libmemcached::*.3pm*
%dir %{perl_vendorarch}/auto/Memcached/
%{perl_vendorarch}/auto/Memcached/libmemcached/
%dir %{perl_vendorarch}/Memcached/
%{perl_vendorarch}/Memcached/libmemcached/
%{perl_vendorarch}/Memcached/libmemcached.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.3102-1
- Updated to version 0.3102.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.2101-1
- Initial package. (using DAR)
