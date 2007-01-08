# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cache-Simple-TimedExpiry

Summary: Cache with simple timed expiry
Name: perl-Cache-Simple-TimedExpiry
Version: 0.27
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache-Simple-TimedExpiry/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/Cache-Simple-TimedExpiry-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides a cache with a simple timed expiry.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Cache/Simple/TimedExpiry.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Updated to release 0.27.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.
