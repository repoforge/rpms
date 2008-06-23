# $Id$
# Authority: dries
# Upstream: Armin Obersteiner <armin$xos,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CDDB_get

Summary: Reads the CDDB entry for an audio CD in your drive
Name: perl-CDDB_get
Version: 2.27
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CDDB_get/

Source: http://www.cpan.org/authors/id/F/FO/FONKIE/CDDB_get-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module/script gets the CDDB info for an audio cd. You need
LINUX, SUNOS or *BSD, a cdrom drive and an active internet connection
in order to do that.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{_bindir}/cddb.pl
%{perl_vendorlib}/CDDB_get.pm
%{perl_vendorlib}/auto/CDDB_get/
%{perl_vendorlib}/auto/CDDB_cache/
%{perl_vendorlib}/cddb.pl
%{perl_vendorlib}/CDDB_cache.pm

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.27-1
- Updated to release 2.27.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.25-1
- Updated to release 2.25.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.23-1
- Initial package.
