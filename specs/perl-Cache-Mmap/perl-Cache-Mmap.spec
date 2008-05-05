# $Id$
# Authority: dries
# Upstream: Peter Haworth <pmh$edison,ioppublishing,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cache-Mmap

Summary: Shared data cache using memory mapped files
Name: perl-Cache-Mmap
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache-Mmap/

Source: http://www.cpan.org/modules/by-module/Cache/Cache-Mmap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides a shared cache, using a memory mapped file. Very useful
for mod_perl applications. If routines are provided which interact with the
underlying data, access to the cache is completely transparent, and the module
handles all the details of refreshing cache contents, and updating underlying
data, if necessary.

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
%doc Changes MANIFEST META.yml README Todo
%doc %{_mandir}/man3/Cache::Mmap.3pm*
%dir %{perl_vendorarch}/auto/Cache/
%{perl_vendorarch}/auto/Cache/Mmap/
%dir %{perl_vendorarch}/Cache/
%{perl_vendorarch}/Cache/Mmap.pm

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.081-1
- Initial package.
