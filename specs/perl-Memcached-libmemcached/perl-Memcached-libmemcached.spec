# $Id$
# Authority: dag
# Upstream: Tim Bunce <Tim,Bunce$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Memcached-libmemcached

Summary: Thin fast full interface to the libmemcached client API
Name: perl-Memcached-libmemcached
Version: 0.2101
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Memcached-libmemcached/

Source: http://www.cpan.org/authors/id/T/TI/TIMB/Memcached-libmemcached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README TODO responses.txt
%doc %{_mandir}/man3/Memcached::libmemcached.3pm*
%doc %{_mandir}/man3/Memcached::libmemcached::*.3pm*
%dir %{perl_vendorarch}/auto/Memcached/
%{perl_vendorarch}/auto/Memcached/libmemcached/
%dir %{perl_vendorarch}/Memcached/
%{perl_vendorarch}/Memcached/libmemcached/
%{perl_vendorarch}/Memcached/libmemcached.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.2101-1
- Initial package. (using DAR)
