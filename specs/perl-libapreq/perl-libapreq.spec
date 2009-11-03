# $Id$
# Authority: dries
# Upstream: Stas Bekman <stas$stason,org>

# FIXME: this needs an older mod_perl (< 1.99)

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name libapreq
%define real_version 2.04_03

Summary: Apache Request C Library
Name: perl-libapreq
Version: 2.04
Release: 0.03.1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/libapreq/

#The version at cpan is very old
#Source: http://www.cpan.org/modules/by-module/libapreq/libapreq-%{version}.tar.gz
Source: http://www.cpan.org/authors/id/S/ST/STAS/libapreq-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: httpd-devel
BuildRequires: mod_perl
BuildRequires: perl-ExtUtils-XSBuilder

%description
This package contains modules for manipulating client request data via
the Apache API with Perl and C.  Functionality includes:
 - parsing of application/x-www-form-urlencoded data
 - parsing of multipart/form-data
 - parsing of HTTP Cookies

%prep
%setup -n %{real_name}2-%{version}-dev

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
#%{perl_vendorlib}/libapreq.pm
#%{perl_vendorlib}/libapreq/*

%changelog
* Mon Apr 18 2005 Dries Verachtert <dries@ulyssis.org> - 2.04-0.03.1
- Update.

* Fri Jan  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.33-1
- Initial package.

