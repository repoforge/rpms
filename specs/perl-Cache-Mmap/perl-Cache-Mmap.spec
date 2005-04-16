# $Id$
# Authority: dries
# Upstream: Peter Haworth <pmh$edison,ioppublishing,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cache-Mmap

Summary: Shared data cache using memory mapped files
Name: perl-Cache-Mmap
Version: 0.081
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache-Mmap/

Source: http://search.cpan.org/CPAN/authors/id/P/PM/PMH/Cache-Mmap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module provides a shared cache, using a memory mapped file. Very useful
for mod_perl applications. If routines are provided which interact with the
underlying data, access to the cache is completely transparent, and the module
handles all the details of refreshing cache contents, and updating underlying
data, if necessary.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Cache/Mmap.pm
%{perl_vendorarch}/auto/Cache/Mmap

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.081-1
- Initial package.
