# $Id$
# Authority: dag
# Upstream: Rob Mueller <cpan$robm,fastmail,fm>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cache-FastMmap

Summary: Uses an mmap'ed file to act as a shared memory interprocess cache
Name: perl-Cache-FastMmap
Version: 1.28
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache-FastMmap/

Source: http://www.cpan.org/modules/by-module/Cache/Cache-FastMmap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Uses an mmap'ed file to act as a shared memory interprocess cache.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Cache::FastMmap.3pm*
%doc %{_mandir}/man3/Cache::FastMmap::CImpl.3pm*
%dir %{perl_vendorarch}/auto/Cache/
%{perl_vendorarch}/auto/Cache/FastMmap/
%dir %{perl_vendorarch}/Cache/
%{perl_vendorarch}/Cache/FastMmap/
%{perl_vendorarch}/Cache/FastMmap.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.28-1
- Updated to release 1.28.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.27-1
- Updated to release 1.27.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 1.24-1
- Initial package. (using DAR)
