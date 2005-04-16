# $Id$
# Authority: dries
# Upstream: Armin Obersteiner <armin$xos,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CDDB_get

Summary: Reads the CDDB entry for an audio CD in your drive
Name: perl-CDDB_get
Version: 2.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CDDB_get/

Source: http://search.cpan.org/CPAN/authors/id/F/FO/FONKIE/CDDB_get-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{_bindir}/cddb.pl
%{perl_vendorlib}/CDDB_get.pm
%{perl_vendorlib}/auto/CDDB_get
%{perl_vendorlib}/cddb.pl

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.23-1
- Initial package.
